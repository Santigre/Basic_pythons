'''
python item 36
'''


# contains integar, string, float variable
'''
int_var = 100 #integer variable
string_var = "Hello world!" #String variable
float_var = 1.5 #float variable

print int_var
print string_var
print float_var
'''


#contains a format notation,if,elif,else

def bla(name= ""):
    name = office(name)

def office(name):
    if name != "":
        print ('Welcome to {} office').format(name)
    else:
        while name == "":
            name = raw_input('\nYour new here! What is your name? ').capitalize()
            print ('\nWelcome to the office {}').format(name)
            print ('\nSee you around!').capitalize()
            end_day(name)
    return name
def end_day(name):
    out = raw_input("ready to go home? yes/no ")
    if out == "yes":
        print("okay lets get out of here")
    elif out == "no":
        print("To bad its time to go")
    elif out == "quit":
        print("Sad to se you leave")    
    exit()
    
    
bla()

#math operators
'''
x = 5
x += 1
y = 7
a = 1
b = 3
c = 5
d = 9
e = 10
t = 0
'''
'''
print (a+b)
print(e-b)
print(d*e)
print(d/b)
print(b%d)
print(x)
print(y)
'''
# and or not operators(uses values for math operators)
'''
if x and y > 1:
    print True
else:
    print False

if y or t:
    print True
else:
    print False
    
if not y > 1:
    print True
else:
    print False
    '''

#The loops
'''
string = "the panda"

for x in string:
    print x
while string == "the panda":
    print ('its a panda')
    string = string + " is red"
print(string)
'''
# The list iteration
'''
animals = ["cat", "dog", "pig", "racoon"]

for animal in animals:
    print "Look at the ", animal
print "So cute!"
'''

# The tuple iteration
'''
colors = ("red", "blue", "green", "orange")

for color in colors:
    print "My favorite color is",color
print ('yes all of them')
'''




    
    











