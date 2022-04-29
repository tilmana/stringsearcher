import os

searchQuery = input("What text are you searching for? ")
fileExtension = input("What file extensions are being searched through? ")
directory = input("Directory to search through? ")
recursive = input("Recursive? Y/N: ")

if recursive.lower() == "y":
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            try:
                file_read = open(os.path.join(subdir, file), "r")
            except Exception as e:
                continue
            try:
                line_content = file_read.readlines()
            except Exception as e:
                continue
            lineTotal = 0
            for line in line_content:
                lineTotal += 1
                if line.strip("\n") == searchQuery:
                    print("Found " + str(searchQuery) + " on line " + str(lineTotal) + " in file: '" + line.strip(
                        "\n") + "'!")
            file_read.close()
else:
    for file in os.listdir(directory):
        try:
            file_read = open(file, "r")
        except Exception as e:
            continue
        line_content = file_read.readlines()
        lineTotal = 0
        for line in line_content:
            lineTotal += 1
            if line.strip("\n") == searchQuery:
                print("Found " + str(searchQuery) + " on line " + str(lineTotal) + " in file: '" + line.strip(
                    "\n") + "'!")
        file_read.close()
