#This is a program to copy selected metadata from one .csv file to another and flag value errors with asterisks.

#Import csv library.
import csv

#Import regular expressions library.
import re

#Create a variable to hold the open file.
#Note the additional input in the open function.  This 'r' opens the file read only.
sourceFile = open('metadata_set.csv','r')

#Create a variable that will hold the csv interpreter.
sourceReader = csv.reader(sourceFile)

#See what's inside our file.
print sourceReader

#Open a writeable file to hold our output.
outputFile = open('newMetadata.csv','w')

#Create a variable to act as a csv writer.
csvWriter = csv.writer(outputFile, delimiter=',')

#Create counter to skip category header in line 0.
counter = 0

#Create a variable to hold the regular expression library for date check. Define metadata standard as YYYY.
dateCheck = re.compile('^\d\d\d\d$')

#Create another variable to hold the regular expression library for media type check. Define metadata standard as 'Sound' or 'Moving Image'.        
typeCheck = re.compile('^Sound$|^Moving\ Image$')

#Move through the file and output the data to a new file.
for line in sourceReader:
    #Create variables for categories not being checked. Categories are object identifier and title.
    objectIdentifier = line[1]
    title = line[9]
    #Check dates and flag value errors.
    lineSearchOne = dateCheck.search(line[21])
    #If date conforms to metadata standard, define 'date' as line[21].
    if lineSearchOne or counter == 0:
        date = line[21]
    #If date does not conform to metadata standard, insert 3 leading asterisks. Define 'date' as ***line[21]. 
    else:
        date = '***' + line[21]  
    #Check media types and flag value errors.
    lineSearchTwo = typeCheck.search(line[7])
    #If media type conforms to metadata standard, define 'mediaType' as line[7].
    if lineSearchTwo or counter == 0:
       mediaType = line[7]
    #If media type does not conform to metadata standard, insert 3 leading asterisks. Define 'mediaType' as ***line[7].
    else:
        mediaType = '***' + line[7]
    #Write output to new file.
    csvWriter.writerow([objectIdentifier,date,title,mediaType])
    #Stop after last entry in file.
    counter = counter + 1
    if counter >= 107:
        break

#Cleanup
sourceFile.close()
outputFile.close()