def connectdb(m):
    print('Connet to DB')
    return m

@connectdb
def db_insert_data():
    print('inser data to emp')

db_insert_data()

@connectdb
def db_get_data():
    print('get data from emp')

db_get_data()

@connectdb
def db_update_data():
    print('update data in emp')

db_update_data()

@connectdb
def db_deleter_data():
    print('delete data in emp')

db_deleter_data()
