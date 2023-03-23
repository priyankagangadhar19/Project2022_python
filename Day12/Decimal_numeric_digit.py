msg="123" #only numbers
print(msg)
print(msg.isdecimal())
print(msg.isdigit())
print(msg.isnumeric())

msg='2\u00b2' #numbers with index - Superscript
print(msg)
print(msg.isdecimal())
print(msg.isdigit())
print(msg.isnumeric())

msg='10\u2082' #numbers with subscript/base/radix
print(msg)
print(msg.isdecimal())
print(msg.isdigit())
print(msg.isnumeric())

msg='10\u2153' #numbers with Vulgar Fraction
print(msg)
print(msg.isdecimal())
print(msg.isdigit())
print(msg.isnumeric())
