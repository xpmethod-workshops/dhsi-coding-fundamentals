#Open the zodiac file

zodiacText = open('zodiacDescriptions.txt')
#for line in zodiacText:
#    print line

#Load into a list
zodiacList = []
for line in zodiacText:
    zodiacList.append(line)

print zodiacList

#Ask user for input (year)
birthYear = raw_input("What year were you born: ")
listIndex = (birthYear - 4) % 12
print listIndex

#Return character
print "You are a ",
print zodiacList[listIndex]

#Repeat

zodiacText.close()