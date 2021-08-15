from peewee import *

host = '149.28.145.242'
db_name = 'test_db'
db_user = 'nghiahsgs4'
db_pass = '123456'
db = MySQLDatabase(db_name,host=host,user = db_user, passwd = db_pass)

class btvn_linh(Model):
	sbd = CharField()
	toan = FloatField()
	van = FloatField()
	anh = FloatField()
	is_run = IntegerField()
	class Meta:
		database=db

if __name__=="__main__":
	# btvn_linh.create_table()
	sbd = "02010000"
	toan = 10
	van = 10
	anh = 9
	row = btvn_linh(sbd=sbd)
	row.save()
