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
try:
    birthYear=int(raw_input('What year were you born: '))
    listIndex = (birthYear - 4) % 12
    print listIndex
    
    #Return character
    print "You are a ",
    print zodiacList[listIndex]
    
except ValueError:
    print "You did not enter a number"


    

#Repeat

zodiacText.close()