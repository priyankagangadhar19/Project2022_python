def test2(city,name='bhanu',ph=123):
    print(city)
    print(name)
    print(ph)

test2('Pune',ph=567)
test2(ph=567,city='Pune')

test2(name='Ravi',city='Delhi')

def test2(city,name=None,ph=None):
    print(city)
    print(name)
    print(ph)

test2('Tumkur')











