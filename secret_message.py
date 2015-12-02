import os

def rename_files(path):
	# get a list of file names from a folder
	os.chdir(path)
	file_list = os.listdir(path)
	
	# for each file, rename filename
	for file_name in file_list:
		new_file_name = file_name.translate(None, "0123456789")
		os.rename(file_name, new_file_name)


rename_files("/Users/ruyi/Udacity_HW/mini_project/alphabet")