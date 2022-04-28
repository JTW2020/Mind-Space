
import commented_eliza
import pytest
#test 1
def test_ContextSwitchDepressed(): #tests if eliza successfully switched contexts from inbetween.txt to depressed.txt
    el = commented_eliza.Eliza()
    el.load("inbetween.txt")
    #"I am depressed."
    assert el.respond("I am depressed") == "I see. Please, tell me about how you've been feeling down."
#test 2
def test_DepressedContext(): #tests if eliza successfully realizes that it is in the depressed context.
    el = commented_eliza.Eliza()
    el.load("depressed.txt")
    #'I am depressed'
    assert el.respond("I am depressed") == "I already know that you are depressed."
#test 3
def test_ContextSwitchAnxious(): #tests if eliza successfully switched contexts from inbetween.txt to anxious.txt
    el = commented_eliza.Eliza()
    el.load("inbetween.txt")
    "I am anxious."
    assert el.respond("I am anxious") == "I see. Tell me about how you've been feeling on edge, please."
#test 4
def test_AnxiousContext(): # tests if eliza is sucessfully referencing the anxious context
    el = commented_eliza.Eliza()
    el.load("anxious.txt")
    assert el.respond("I am anxious") == "I already know that you are anxious. Can you explain more of what makes you feel this way ?"
#test 5
def test_ContextSwitchDisorder(): #tests if eliza successfully switched contexts from inbetween.txt to disorder.txt via string matching.
    el = commented_eliza.Eliza()
    el.load("inbetween.txt")
    assert el.respond("I think I have a Disorder") == "I see. Please, tell me about why you've been feeling this way."
# #test 6
# def test_DisordeContext():     #Cannot test disorder context because there is no unique response given when keyword is recieved from user input that triggers the context confirmation
#    el = commented_eliza.Eliza()
#    el.load('disorder.txt')
#    assert el.respond("I am hungry") == "I see. Please, tell me about why you've been feeling this way."
#test 7
def test_ContextSwitchAnger(): #tests if eliza successfully switched contexts from inbetween.txt to anger.txt via string matching.
    el = commented_eliza.Eliza()
    el.load('inbetween.txt')
    assert el.respond("I am angry") == "Understood. Please tell me about how you've been having your temper challenged."
#test 8
def test_AngerContext(): #confirms if eliza recognizes it is using the anger context via string matching.
    el = commented_eliza.Eliza()
    el.load("anger.txt")
    assert el.respond("I feel anger") == "we will not talk about your anger"
#test 9
def test_ElizaExit(): #tests if eliza exits correctly via string matching.
    el = commented_eliza.Eliza()
    el.load("inbetween.txt")
    assert el.respond("goodbye") == None

def test_DepressionConversation():
    el = commented_eliza.Eliza()
    el.load("inbetween.txt")
    assert el.respond("I am feeling depressed") == "I see. Please, tell me about how you've been feeling down."
    assert el.respond("My dog died recently") == "I am so sorry to hear that. So have you been feeling this way only since then, or at all before ?"
    assert el.respond("I have felt this way since my dog died ") == "Are you comfortable talking about this directly ? Or would you just like for us to focus on helping you feel better ?"
    assert el.respond("goodbye") == None
def test_ElizaForeign():
    el = commented_eliza.Eliza()
    el.load("depressed.txt")
    assert el.respond("hablas espanol ?") == "I speak only English."
    assert el.respond("Sprichst du Deutsch ?") == "I speak only English."
    assert el.respond("parli italiano ?") == "I speak only English."
    assert el.respond("Est-ce que tu parles francais?") == "I speak only English."

def test_punctuation_decomp():
    el = commented_eliza.Eliza()
    el.load("depressed.txt")
    assert el.respond("I am who I am.") == "I see. Can you tell me about the thoughts that are troubling you ?"
    assert el.respond("oh, my.") == 'What makes you say, "oh my" ?'
    assert el.respond("can i?") == "What do you think would allow you to do that ?"