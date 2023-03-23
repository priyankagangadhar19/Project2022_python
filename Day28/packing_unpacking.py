# def print_city(*allcity):
#     for city in allcity:
#         print(city)
#

#packing and unpacking
#this is procedural program-->

def print_city(*allcity):
    for city in allcity:
        print(city)

print_city('Agra')
print_city('Agra','Banaras')
print_city('Agra','Banaras','Chennai')

def print_address(city,area,pin):
    print(city,area,pin)

print_address('BNG','MG Road',1234)

list1=['BNG','MG Road',1234]
# print_address(list1[0],list1[1],list1[2])
print_address(*list1)

t=('MYS','MG Road',1234)
# print_address(list1[0],list1[1],list1[2])
print_address(*t)

s={'TMK','MG Road',1234}
print_address(*s)

d={'city':'TMK','area':'Jayanagar','pin':123}
print_address(*d)

