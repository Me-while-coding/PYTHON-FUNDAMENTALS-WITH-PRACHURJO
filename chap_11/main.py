# file = open("notes.txt","a")
# file.write("\nno harm to old data")
# file.close()

with open("notes.txt","r") as file:
    for line in file.readlines():
        print(line.strip("\n"))

