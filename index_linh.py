from utils_linh import *
from utils_db_linh import *
from multiprocessing import Pool
from peewee import *
from peewee import chunked

def job(sbd):
	toan,van,anh = get_score(sbd)
	is_run = 1

data_source = [
	f'020{i}'
	for i in range (10000,89000)
]
# for sbd in data_source():
# 	toan,van,anh = get_score(sbd)
# 	print(sbd)

def main():
	p = Pool(4)
	kq = p.map_async(job,data_source)
	print(kq.get())
	p.close()
	p.join()
	print('đã chạy xong')

if __name__=="__main__":
	main()
