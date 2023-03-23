list=input('Enter a word')
r= list[::-1]
print(list)
print(r)
if list==r:
    print(list,'Is palindrome')
else:
    print(list,'Is not a palindrome')