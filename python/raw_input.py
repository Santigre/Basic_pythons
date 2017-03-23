import dictionary
personsName = input('Please eneter a name: ')
personsInfo = dictionary.programmer_dict[personsName]

try:
    dictionary.programmer_dict[personsName]
    print (personsInfo)

except:
    print ('sdfgh')
'''if personsInfo == dictionary.programmer_dict[personsName]:
    print (personsInfo)

else:
    print('No one by this name')'''
'''print (personsName)
print (personsInfo)'''
