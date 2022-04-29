import os, re

searchQuery = input("What text are you searching for? ")
fileExtension = "." + input("What file extensions are being searched through? ").replace(".", "")
directory = input("Directory to search through? ")
recursive = input("Recursive? Y/N: ")
print("------------------------")
total_files = 0
def findText(text):
    return re.compile(r'\b({0})\b'.format(text), flags=re.IGNORECASE).search

def findOffset(query, text):
    x = re.search(query, text)
    return x

def search(file):
    global total_files
    if os.path.splitext(file)[1] == fileExtension:
        file_read = open(file, "r")
        line_content = file_read.readlines()
        total_files += 1
        lineTotal = 0
        print("-> Trying file: " + str(file))
        for line in line_content:
            lineTotal += 1
            if findText(searchQuery)(line) != None:
                print("->>>Found " + str(searchQuery) + " on line " + str(lineTotal) + " in file: '" + str(file) + "'!")
                print("->>>Offset: " + str(findOffset(searchQuery, line).start()) + " and end " + str(findOffset(searchQuery, line).end()))
        file_read.close()


if recursive.lower() == "y":
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1] == fileExtension:
                search(os.path.join(root, file))
    if total_files == 1:
        print("Searched through " + str(total_files) + " files!")
    else:
        print("Searched through " + str(total_files) + " files!")
else:
    for file in os.listdir(directory):
        if os.path.splitext(file)[1] == fileExtension:
            search(file)
    if total_files == 1:
        print("Searched through " + str(total_files) + " files!")
    else:
        print("Searched through " + str(total_files) + " files!")
