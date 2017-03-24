from dictionary import programmer_dict
personsName = raw_input('Please eneter a name: ').lower()
runAgain = True

while runAgain == True:
    def searchPerson(personsName):
        try:
            personsInfo = programmer_dict[personsName]
            print 'Name: ' + personsName.title()
            print 'Email: ' + personsInfo[0]
            print 'Number: ' + str(personsInfo[1])
        except:
            print 'No one by this name'
        
        runAgain = True
while runAgain == True:
    personsName = raw_input('Please eneter a name: ').lower()
    searchPerson(personsName)
    runAgain = False
    
searchAgain = raw_input('Search Again? (y,n)')

if searchAgain == 'y':
    runAgain = True

else:
    print 'lets quit'
    runAgain = False
