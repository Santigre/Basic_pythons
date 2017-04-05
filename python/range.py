
numbers= [0,1,2,3]
length = len(numbers)

print("\nCount length")
def count(numbers,length):
    for i in range (length):
        print(numbers[i],)
    print("\nCount length backwards")
    backwards(numbers,length)
def backwards(numbers,length):
    for i in reversed(numbers):
        print(numbers[i])
    print("\nCount length backwards *2 +2")
    double(numbers,length)
def double(numbers,length):
    for i in range(length):
        print(numbers[i]*2+2)
            

    

count(numbers,length)
