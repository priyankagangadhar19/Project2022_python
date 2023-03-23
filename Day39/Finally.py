print('Start')
i=10
j=0

try:
    res=i/j
    print(res)
except:
    print("Some err")
finally:
    print('Thank You')


print('End')

# what is exception- unexpected event
# what happens -> we get error - execution stop
# can we prevent->No
# can we handle -yes
# how - try -except
# code which may generate exception - risky code- should be written inside try block
# code to handle the exception should be written inside except block
# for one try we can have one or more except block
# if exception occurs - it will check for the matching exception one by one (top to bottom)
# if except block is declared using Exception - it will accept any type of exception
# write it as a last block
#irrespetice of exception occured or not -if we want to run block of code then we should use finally