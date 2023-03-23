print("".isalpha())

print("abc".isdigit())
print("abc".isalpha())
print("A1234".isalnum())


a="abcd"
print(a.isalpha()) #does it contains only alphabets
print("".isalpha())
print("A123".isalpha())
print("Abc ".isalpha())
print("A&".isalpha())

print("123".isdigit())#does it contains only digits
print("A123".isdigit())#does it contains only digits
print("12.34".isdigit())#does it contains only digits-0 to 9
print("".isdigit())

print("123".isnumeric())
print("12.346".isnumeric())
print("A123".isnumeric())
print("".isnumeric())

print("A123".isalnum())
print("ABC".isalnum())
print("123".isalnum())
print("A 1".isalnum())
print("@#$%".isalnum())
print("".isalnum())