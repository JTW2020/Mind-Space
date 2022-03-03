import logging
import random
import re
import os.path as path
from collections import namedtuple

# Fix Python2/Python3 incompatibility
try:
    input = raw_input
except NameError:
    pass

# this creates a logger with which to log messages
# this line sets the logger to output debug information to the console, it should be commented out when debugging is not being done

# logging.basicConfig(level=logging.NOTSET)

# this creates the logger with which to log messages

log = logging.getLogger(__name__)

'''
This is the Key class.
It contains a keyword, that is, a word that is to be associated with certain decomposition rules.
It contains a weight value which is used to determine the priority of this keyword, the higher the number, the higher the priority
It contains decomps, which is a list of instances of the Decomp class.
'''


class Key:
    def __init__(self, word, weight, decomps):
        self.word = word
        self.weight = weight
        self.decomps = decomps


'''
This is the Decomp class.
It contains a list, called parts, of strings that make up the individual parts of a decomposition rule
The boolean value, save, is true if this decomposition should be saved to memory instead of immediately output.
The list, reasmbs, contains all of the reassembly rules associated with the given decomposition rule
These rules are cycled through when the same decomposition rule is used multiple times, and the next_reasmb_index value fascilitates this
'''


class Decomp:
    def __init__(self, parts, save, reasmbs):
        self.parts = parts
        self.save = save
        self.reasmbs = reasmbs
        self.next_reasmb_index = 0


'''
This is the ELiza class. Along with all of its methods are its fields.
initials is a list of initial greetings that Eliza can provide when it first begins.
finals is a list of phrases that Eliza can use when terminating.
quits is a list of strings that Eliza will interpret as the user indicating that they wish to end the session.
pres is a dictionary that contains substitutions that are to be made before the input string is transformed according to a decomposition and assembly rule
posts is a dictionary that contains substitutions that are to be made after the input string is transformed according to a decomposition and assembly rule
synons is a dictionary that contains synonyms for various words that Eliza may encounter
keys is a dictionary that contains objects of the Key class
memory is a list of phrases for Eliza to use in the event that it cannot match any words in the input to any keywords, this list should be added on to during execution so the program can refer to previous topics
'''


class Eliza:
    def __init__(self):
        self.initials = []
        self.finals = []
        self.quits = []
        self.pres = {}
        self.posts = {}
        self.synons = {}
        self.keys = {}
        self.memory = []

    # The load method loads in information for all of ELiza's attributes from a text file formatted like the provided file 'doctor.txt'.

    def load(self, path):
        key = None
        decomp = None
        with open(path) as file:

            # The lines of the file are processed one-by-one, and blank lines (or ones consisting of only whitespace) are ignored.

            for line in file:
                if not line.strip():
                    continue

                # Within the file the tag, or the text before the colon, denotes the type of information while the text after it is the information itself, these two are separated into tag and content variables

                tag, content = [part.strip() for part in line.split(':')]

                # If the information is of type intitial, final, or quit it is simply added to the appropriate list.

                if tag == 'initial':
                    self.initials.append(content)
                elif tag == 'final':
                    self.finals.append(content)
                elif tag == 'quit':
                    self.quits.append(content)

                # If the information is of type pre or post, the key into the appropriate dictionary is the first word in content and said key will point to the remaining words.

                elif tag == 'pre':
                    parts = content.split(' ')
                    self.pres[parts[0]] = parts[1:]
                elif tag == 'post':
                    parts = content.split(' ')
                    self.posts[parts[0]] = parts[1:]

                # If the information is of type synon, the key into the dictionary is the first word of the content and said key will point to all words in the content.

                elif tag == 'synon':
                    parts = content.split(' ')
                    self.synons[parts[0]] = parts

                # If the information is of type key then the first part of the content is the keyword, the second part is the weight (which is set to 1 if it does not exist),
                # an instance of the Key class is created with this information and it is then inserted into the keys dictionary, and it will be retrieved using the keyword.

                elif tag == 'key':
                    parts = content.split(' ')
                    word = parts[0]
                    weight = int(parts[1]) if len(parts) > 1 else 1
                    key = Key(word, weight, [])
                    self.keys[word] = key

                # If the information is of type decomp then the content is split into parts. If the first part is a dollar sign then this decomp will have save set to true, and the remaining parts will be considered.
                # The decomp is then instantiated and then added to the list of decomps belonging to the previously added key.

                elif tag == 'decomp':
                    parts = content.split(' ')
                    save = False
                    if parts[0] == '$':
                        save = True
                        parts = parts[1:]
                    decomp = Decomp(parts, save, [])
                    key.decomps.append(decomp)

                # If the information is of type resmb then the content is split into parts which are then appended to the previously added decomp's reasmbs list.

                elif tag == 'reasmb':
                    parts = content.split(' ')
                    decomp.reasmbs.append(parts)

    # This method simply clears the Eliza script information and loads in another script, therefore completing a context switch.

    def context_switch(self, context):
        self.initials = []
        self.finals = []
        self.quits = []
        self.pres = {}
        self.posts = {}
        self.synons = {}
        self.keys = {}
        self.memory = []

        self.load(context)

    # This method recursively attemps to match parts of a decomposition rule to input words.

    def _match_decomp_r(self, parts, words, results):

        # If there are no parts and no words remaining, the match is successful. Return true.

        if not parts and not words:
            return True

        # Otherwise, if there are no parts remaining, or if there are no words remaining and there is not only one remnant part which is an asterisk, the match has failed. Return false.

        if not parts or (not words and parts != ['*']):
            return False

        '''
        If the first part of the decomposition rule is an asterisk, any number of words from the left side could match it.
        Due to this, each possible match is attempted.
        The words assumed to match the asterisk are added to the output, with the remaining words (if any) and remaining rule parts (if any) passed along so that they in turn can be tested for matching.
        If a match is found, return true. If not, pop the last addition to the results and try the next number of words.
        If no match is found after all possible attempts, return false.
        '''

        if parts[0] == '*':
            for index in range(len(words), -1, -1):
                results.append(words[:index])
                if self._match_decomp_r(parts[1:], words[index:], results):
                    return True
                results.pop()
            return False

        # If an @ begins a part then that means that the corresponding word must be a synonym of the word that comes directly after the @ in the rule part.
        # Root is that word, the one after the @.
        # If root is not in the synons dictionary there is a value error.
        # If the corresponding word is not listed as a synonym for root then the match fails, return false.
        # If it is a synonm for root, add it to the results and run this method on the remaining rule parts and words.

        elif parts[0].startswith('@'):
            root = parts[0][1:]
            if not root in self.synons:
                raise ValueError("Unknown synonym root {}".format(root))
            if not words[0].lower() in self.synons[root]:
                return False
            results.append([words[0]])
            return self._match_decomp_r(parts[1:], words[1:], results)

        # If the rule part and the corresponding word are not the same (ignoring case) then the match fails. Return false.

        elif parts[0].lower() != words[0].lower():
            return False

        # If the rule part and the corresponding word are the same, run this method on the remaining rule parts and words.

        else:
            return self._match_decomp_r(parts[1:], words[1:], results)

    '''
    This method attempts to match the parts of a decomposition rule to input words.
    It calls upon the recursive method, _match_decomp_r.
    '''

    def _match_decomp(self, parts, words):
        results = []
        if self._match_decomp_r(parts, words, results):
            return results
        return None

    '''
    This method returns the next reassembly rule to be used for a given decomposition rule.
    This is determined by using the index.
    The index is then incremented by one so that, over several uses of the same decomposition rule,
    it will cycle through its reassembly rules in order, and thus never use the same one consecutively unless there is only one in total.
    '''

    def _next_reasmb(self, decomp):
        index = decomp.next_reasmb_index
        result = decomp.reasmbs[index % len(decomp.reasmbs)]
        decomp.next_reasmb_index = index + 1
        return result

    # This method returns the output created by applying a given reassembly rule to some words which are results from the _match_key method.

    def _reassemble(self, reasmb, results):
        output = []

        # This loop is run for every word in the reassembly rule.

        for reword in reasmb:

            # If the word is empty, do nothing and continue.

            if not reword:
                continue

            # If the word begins with ( and ends with ) then it is a 1-indexed number specifying which part of the results should replace it.
            # If the index is less than one or greater than the highest index possible for the results there is a value error.
            # Otherwise, insert becomes the result part that is to replace this word of the reassembly rule.
            # This is done while accounting for the fact that Python lists are 0-indexed, not 1-indexed.

            if reword[0] == '(' and reword[-1] == ')':
                index = int(reword[1:-1])
                if index < 1 or index > len(results):
                    raise ValueError("Invalid result index {}".format(index))
                insert = results[index - 1]

                # If a comma, period, question mark, or semicolon is in insert, then only content that precedes any of these punctuations remains.

                for punct in [',', '.', ';', '?']:
                    if punct in insert:
                        insert = insert[:insert.index(punct)]

                # Add insert to the output.

                output.extend(insert)

            # If the word is not a number between opening and closing parentheses, simply add it to the output.

            else:
                output.append(reword)
        return output

    '''
    This method substitutes words in the input text that are keys in the supplied sub dictionary with the value each key corresponds to.
    Words that are not keys in the sub dictionary are left alone.
    Case is ignored when checking if a word is a key in the sub dictionary.
    '''

    def _sub(self, words, sub):
        output = []
        for word in words:
            word_lower = word.lower()
            if word_lower in sub:
                output.extend(sub[word_lower])
            else:
                output.append(word)
        return output

    # This method will attempt to match input words to one of the provided key's decomposition rules.

    def _match_key(self, words, key):
        for decomp in key.decomps:
            results = self._match_decomp(decomp.parts, words)

            # If a decomposition rule does not match the words, immediately try the next rule.

            if results is None:

                # Viewing the messages that are produced with this debug method would be useful.
                # However, I have not found how to do this yet.

                # This method produces some output to be viewed for the purpose of debugging

                log.debug('Decomp did not match: %s', decomp.parts)
                continue

            # If a decomposition rule matches, then perform the post-substitutions on the results.

            log.debug('Decomp matched: %s', decomp.parts)
            log.debug('Decomp results: %s', results)
            results = [self._sub(words, self.posts) for words in results]
            log.debug('Decomp results after posts: %s', results)

            # From there, find out which reassembly rule is to be used.

            reasmb = self._next_reasmb(decomp)
            log.debug('Using reassembly: %s', reasmb)

            # If the reassembly rule says to go to another key, use that key to process the input words instead.
            # If the key it directs you to does not exist, raise a value error.

            if reasmb[0] == 'goto':
                goto_key = reasmb[1]
                if not goto_key in self.keys:
                    raise ValueError("Invalid goto key {}".format(goto_key))
                log.debug('Goto key: %s', goto_key)
                return self._match_key(words, self.keys[goto_key])

            # If the reassembly rule says to switch contexts, the word after switch will be the file name without the extension.
            # Any following words will serve as the output, so they are saved and returned after the context switch is attempted.
            # If the file specified does not exist, raise a value error.

            elif reasmb[0] == 'switchto':

                output = reasmb[2:]

                context = "{}.txt".format(reasmb[1])

                if path.exists(context):
                    self.context_switch(context)
                else:
                    raise ValueError(
                        "Unknown context file: {}".format(context))

                return output

            # Get the ouput by using the previously selected reassembly rule on the results obtained earlier.

            output = self._reassemble(reasmb, results)

            # If the decomposition rule says to save the output, add it to Eliza's memory list, then continue attempting to match the input words to the remaining decomposition rules.

            if decomp.save:
                self.memory.append(output)
                log.debug('Saved to memory: %s', output)
                continue

            # Otherwise, return the ouput.

            return output

        # If no decomposition rules match the input words, return nothing.

        return None

    # This is the method that returns a response after processing some input text.

    # Note to self, USE THIS METHOD FOR INPUT AND RESPONSE
    # DELETE AFTER DONE
    def respond(self, text):

        # Ignoring capitalization, if the input text matches a quit phrase, nothing is returned so that the execution look will break and the session will be terminated.

        if text.lower() in self.quits:
            return None

        # The input text is cleaned up by replacing matching patterns with standard text.
        # Any number of spaces, followed by at least one period, followed by any number of spaces, is replaced with a space, a period, and one more space.
        # The same transformation is applied except with commas, question marks, and then semicolons.

        text = re.sub(r'\s*\.+\s*', ' . ', text)
        text = re.sub(r'\s*,+\s*', ' , ', text)
        text = re.sub(r'\s*;+\s*', ' ; ', text)
        text = re.sub(r'\s*\?+\s*', ' ? ', text)

        log.debug('After punctuation cleanup: %s', text)

        # The words in the input are separated via spaces into entries in a list.

        words = [w for w in text.split(' ') if w]
        log.debug('Input: %s', words)

        # The pre-substitutions are made.

        words = self._sub(words, self.pres)
        log.debug('After pre-substitution: %s', words)

        # The keys corresponding to all of the detected keywords are gathered then sorted in descending order by weight.

        keys = [self.keys[w.lower()] for w in words if w.lower() in self.keys]
        keys = sorted(keys, key=lambda k: -k.weight)
        log.debug('Sorted keys: %s', [(k.word, k.weight) for k in keys])

        output = None

        # Try to match the input words to each key, in priority order.
        # If a match is found, the loop immediately ends and the output is returned.
        # If no match is found after all keys are tried, and if the memory list is not empty, randomly select an entry from it, remove the entry from the memory list, and return it as the output.
        # If the memory list is empty, the output will be a reassembly rule from the xnone key's only decomposition rule.
        # The reassembly rule itself can be output because, in the case of no matches, and no entries in the memory list, the response will be completely independent from user input.

        for key in keys:
            output = self._match_key(words, key)
            if output:
                log.debug('Output from key: %s', output)
                break
        if not output:
            if self.memory:
                index = random.randrange(len(self.memory))
                output = self.memory.pop(index)
                log.debug('Output from memory: %s', output)
            else:
                output = self._next_reasmb(self.keys['xnone'].decomps[0])
                log.debug('Output from xnone: %s', output)

        # Return the contents of output separated by spaces.

        return " ".join(output)

    # This method returns a random initial greeting from Eliza's list of them.

    # Think about on-page-load get for initial message
    # DELETE this after done
    def initial(self):
        return random.choice(self.initials)

    # This method returns a random goodbye message from Eliza's list of them.

    def final(self):
        return random.choice(self.finals)

    '''
    This is the method for running Eliza after all of its attributes have been loaded from a text file.
    It first prints out an initial greeting, then enters a loop of awaiting user input, generating output, and displaying said output.
    If no output is produced the loop terminates and ELiza displays a goodbye message before the session ends.
    '''

    def run(self):
        print(self.initial())

        while True:
            sent = input('> ')

            output = self.respond(sent)
            if output is None:
                break

            print(output)

        print(self.final())

    def test_output(self):
        return "Eliza has been imported and is accessible"


'''
This method instantiates an Eliza object, loads information from a text file, 
and then runs the program.
'''


def main():
    eliza = Eliza()
    eliza.load('inbetween.txt')
    eliza.run()


'''
This is where execution of the program actually begins.
The logger is set with the basic configurations and then the main method is called.
'''

if __name__ == '__main__':
    logging.basicConfig()
    main()
