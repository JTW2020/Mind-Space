import tablib

#This is the function that creates the spreadsheet.
#It uses tablib to create a csv file holding the keywords and priorities of a context file, represented as the context variable, and saves this csv file as filename

def makeSpreadsheet(context, filename):

    data = tablib.Dataset()
    data.headers = ('Keyword', 'Priority')
    
    with open(context) as file:
        for line in file:
            if not line.strip():
                continue

            tag, content = [part.strip() for part in line.split(':')]

            if tag == 'key':
                parts = content.split(' ')
                word = parts[0]
                weight = int(parts[1]) if len(parts) > 1 else 1
                data.append((word, weight))

    with open(filename, "w", newline='') as file:
        file.write(data.csv)

#This is where the function is actually run, the entry point of the program.

makeSpreadsheet('anxious.txt', 'priorities.csv')


