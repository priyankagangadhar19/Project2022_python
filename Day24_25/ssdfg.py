def test1(name='bhanu'):
    print(name)

test1()
test1('Ravi')
def test2(city,name='bhanu',ph=123):
    print(city)
    print(name)
    print(ph)

test2('Delhi') #Delhi bhabu 123
test2('Pune','Ravi') #Pune Ravi 123
test2('Agra','Suray',456)#Agra Suraya 456