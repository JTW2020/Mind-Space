from itertools import count


#This function will be used to automatically populate the database with an entry for each reassembly rule that the context file, represented by the context variable, has.
#For now all it does is count the number of reassembly rules.

def countReassemblies(context):
    count = 0
    with open(context) as file:
        for line in file:
            if not line.strip():
                continue

            tag = line.split(':')[0].strip()

            if tag == 'reasmb':
                count += 1
    
    print(count)

#This is where the function is actually called, so it is the entry point.

countReassemblies("depressed.txt")
countReassemblies("disorder.txt")
countReassemblies("inbetween.txt")
countReassemblies("anger.txt")
countReassemblies("anxiexty.txt")
