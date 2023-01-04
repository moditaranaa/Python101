# An array can have (n-1) elements, where n is the length of the array.
# The elements can be in range of 1 to n 

#The sum method -

def findMissing(arr,n):
    #n*(n+1)/2, 100*101/2 = 5050
    expectedSum = n* (n+1)/2
    actualSum = sum(arr)
    return expectedSum - actualSum

arr =[]
n= int(input("Enter the length of the array : "))
for i in range (n-1):
    m = int(input("Enter a number between 1 to " + str(n) + " : "))
    arr.append(m)

missingNumber = findMissing(arr,n)
print("The missing number is : ", missingNumber)