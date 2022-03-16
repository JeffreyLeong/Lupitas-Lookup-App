# Jeffrey Leong, 2022

import json

# relative path
pathToFile = "D:/Programming Practice/Python/Lupitas-Lookup-App/birthday.json"

# try to open a file and throw a error if it is not found
try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)

# read the whole json file into a variable
birthdayList = json.load(jsonFile)

# create an empty dictionary
birthdayDictionary = {}

# loop json list of data and put each name and birthday into a dictionary
for elem in birthdayList:
    # fetch name and birthday
    name = elem["name"]
    birthday = elem["birthday"]
    birthdayDictionary[name] = birthday

# to print a value in the dictionary by giving it a string with the name as the key
# print("Jocelyn Jones's birthday is: " + birthdayDictionary["Jocelyn Jones"])


# to get user input
name = input("Enter a name: ")
if name in birthdayDictionary:
    print("-----------------------------\n"+"Name\n"+"-----------------------------")
    print('{}\'s birthday is {}.'.format(name, birthdayDictionary[name]))
    # print("Lupe's friends that match " + name + " are: " )
    # print(name + "'s birthday is " + birthdayDictionary[name])
else:
    print("Lupe does not have any friends that match the name {}".format(name))
    # print("Lupe does not have any friends that match the name " + name + ".")
