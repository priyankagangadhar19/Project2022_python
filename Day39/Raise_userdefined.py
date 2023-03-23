#creating our own exception- user defined exception -custom exception
class UserNameNotPreset(Exception):
    pass



def automation_script1():
    print('Open the browser')
    print('Enter the url')
    print('Enter UN')
    raise UserNameNotPreset('UserName Text Box is not present')


automation_script1()