subject=["testing","python","selenium"]
print(subject)

#we add the element(value) at the end-> append
subject.append("BDD")
print(subject)

subject.insert(0,"SQL")
print(subject)

#add the value at the end of the list without using append
n=len(subject)
subject.insert(n-5,"python")
print(subject)

#demo2

subject=["testing","python","selenium"]
print(subject)

subject.insert(3,"java")
print(subject)

n=len(subject)
subject.insert(10,"C++")
print(subject)

subject.insert(3,"kava")
print(subject)

#to know the index of the given value we can use index()
print(subject.index("C++"))

print(subject.index("js")) #is not in list















