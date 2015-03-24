	#Open the zodiac file

def ZodiacSetup():
    zodiacText = open('zodiacDescriptions2.txt')
    #for line in zodiacText:
    #    print line
    
    #Load into a list
    zodiacList = []
    for line in zodiacText:
        zodiacList.append(line)
        
    zodiacText.close()
    
    return zodiacList

def ZodiacFigure():
    #Ask user for input (year)
    try:
        birthYear=int(raw_input('What year were you born: '))
        #Take year and use as a conditional (later we'll just access the dictionary directly)
        listIndex = (birthYear - 4) % 12
        print listIndex
        
        #Return character
        print "You are a ",
        print zodiacList[listIndex]
        
    except ValueError:
        print "You did not enter an integer"
        birthYear = "Stop"
        
    return birthYear

#Repeat
zodiacList = ZodiacSetup()

birthYear=0
while type(birthYear) is int:
    birthYear = ZodiacFigure()
    #print type(birthYear)
