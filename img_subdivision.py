import csv
import os
import shutil

with open(".\CelebA\Anno\list_attr_celeba.csv", 'r') as f:
	reader = csv.DictReader(f,delimiter=';')

	reader2 = csv.reader(open(".\CelebA\Eval\list_eval_partition.txt"), delimiter=" ")
	data = list(reader2)

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img' 
	if not os.path.exists(newpath):
		os.makedirs(newpath)	

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\train' 
	if not os.path.exists(newpath):
		os.makedirs(newpath)  

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\train\male' 
	if not os.path.exists(newpath):
		os.makedirs(newpath) 

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\train\female' 
	if not os.path.exists(newpath):
		os.makedirs(newpath) 

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\validation' 
	if not os.path.exists(newpath):
		os.makedirs(newpath) 

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\validation\male' 
	if not os.path.exists(newpath):
		os.makedirs(newpath)

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\validation\female' 
	if not os.path.exists(newpath):
		os.makedirs(newpath)

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\test' 
	if not os.path.exists(newpath):
		os.makedirs(newpath) 

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\test\male' 
	if not os.path.exists(newpath):
		os.makedirs(newpath)

	newpath = r'C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\test\female' 
	if not os.path.exists(newpath):
		os.makedirs(newpath)

	i = 0
	for row in reader:
		print(row["ï»¿File_name"])
		src_path = r"C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\CelebA\Img\img_align_celeba\{img_name}".format(img_name=row["ï»¿File_name"])

		if row["Male"] == "1":
			if data[i][1] == "0":		
				dst_path = r"C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\train\male\{img_name}".format(img_name=row["ï»¿File_name"])
			if data[i][1] == "1":
				dst_path = r"C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\validation\male\{img_name}".format(img_name=row["ï»¿File_name"])
			if data[i][1] == "2":
				dst_path = r"C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\test\male\{img_name}".format(img_name=row["ï»¿File_name"])
			shutil.copy(src_path, dst_path)
		else:
			if data[i][1] == "0":		
				dst_path = r"C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\train\female\{img_name}".format(img_name=row["ï»¿File_name"])
			if data[i][1] == "1":
				dst_path = r"C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\validation\female\{img_name}".format(img_name=row["ï»¿File_name"])
			if data[i][1] == "2":
				dst_path = r"C:\Users\andro\Desktop\Uni Magistrale\DLA\Progetto\img\test\female\{img_name}".format(img_name=row["ï»¿File_name"])
			shutil.copy(src_path, dst_path)


		i = i + 1
