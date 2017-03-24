from dictionary import programmer_dict
personsName = raw_input('Please eneter a name: ')
personsInfo = programmer_dict[personsName]

try:
    programmer_dict[personsName]
    print personsInfo
except:
    print 'No one by this name'
'''if personsInfo == dictionary.programmer_dict[personsName]:
    print (personsInfo)

else:
    print('No one by this name')'''
'''print (personsName)
print (personsInfo)'''
