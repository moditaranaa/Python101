#To check if the string is anagram 

str1 = input("Enter string 1 : ")

str2 = input("Enter string 2 : ")

if len(str1) != len(str2):
    print("Not Anagrams")
else:
    if sorted(str1) == sorted(str2):
        print("Strings are anagram!!")
    else:
        print("Not Anagrams")


