import os
import csv

formatted_data_directory = os.path.join("data-formatted/")

def create_formatted_outputs():
	print("{0}{1}".format(formatted_data_directory, "manifest.csv"))
	f_manifest = open("{0}{1}".format(formatted_data_directory, "manifest.csv"))
	f_reader = csv.reader(f_manifest)

	for i in f_reader:
		try:
			new_file = open("{0}{1}".format(formatted_data_directory, i[0]), 'x')
		except:
			print("File already exists")

	f_manifest.close()


print("Henlo there")
create_formatted_outputs()