list1=[1,2,4,6,8,9]
n=66

msg="not found"

for i in list1:
    if i ==n:
        msg="found"
        break
print(n,msg)