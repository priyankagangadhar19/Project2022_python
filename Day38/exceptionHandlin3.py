try:
    n1 = int(input('Plz enter the number'))
    n2 = int(input('Plz enter the number'))
    result=n1/n2
    print('Result of n1/n2 is', result)

except ValueError as e1:
    print('please enter only numbers')

except ZeroDivisionError as e2:
    print('2nd number should not be zero')

except Exception as e1:
    print(e1)

print('Thank You')

# n1 = int(input('Plz enter the number')) #ValueError
# n2 = int(input('Plz enter the number'))
# result = n1 / n2#ZeroDivisionError
# print('Result of n1/n2 is', result)