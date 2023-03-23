fruit=("Hello","apple","text","apple")
print(fruit.index("text"))

#to print duplicate elements index

p=fruit.index("apple")
s=fruit.index("apple",p+1)
print(s)

"""a=('api','python','cobra','python')
print(a.index('cobra')) #2

f=a.index('python')
s=a.index('python',f+1) #2nd python
print(s)

print(a.count('python')) #2

print( 'api' in a) #True

print( 'selenium' in a) #False

print(a.index('king cobra')) #not in tuple"""