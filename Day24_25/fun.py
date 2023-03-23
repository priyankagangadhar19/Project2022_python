#keyword argument

def test(name,city,ph):
    print('name',name)
    print('city',city)
    print('ph',ph)

# test('Bhanu','Bengaluru',9481787493) # we can do this or use below way

#keyword arguments
test(ph=9481787493,city='Bengaluru',name='Bhanu')
