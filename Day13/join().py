text=['hello','world!', 'can', 'we','check','the','mobile']
text2=" "
text3=text2.join(text)
print(text3)


print("_".join(text))

msg="This is Bhanu Prakash"
res=msg.split(" ",2)
print(res)


#HCL input is 'This is Bhanu' output should be 'This_is_Bhanu' without using replace
s="This is Bhanu"
res=s.replace(' ','_')
print(res)

msg1=s.split()
msg2='_'.join(msg1)
print(msg2)

print('_'.join(s.split(' '))) #1st split based on space and join back using _


msg1=['this','is','bhanu'] #list of string
msg2=" " #delimiter
msg3=msg2.join(msg1) #join the string present in list using delimiter & return string
print(msg3)

print("_".join(msg1))

print("_".join("bhanu")) #convert string to list then join back using delimiter

msg="This is Bhanu Prakash"
res=msg.split(" ",2)
print(res)








