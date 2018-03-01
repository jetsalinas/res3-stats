import os
import csv

raw_data_directory = os.path.join("data-raw/")
formatted_data_directory = os.path.join("data-formatted/")

def create_formatted_outputs():
	print("Initializing project files.")

	f_manifest = open("{0}{1}".format(formatted_data_directory, "manifest.csv"))
	f_reader = csv.reader(f_manifest)

	for i in f_reader:
		try:
			new_file = open("{0}{1}".format(formatted_data_directory, i[0]), 'x')
		except:
			print("Unable to create file. File already exists: " + i[0])

	f_manifest.close()

def describe_codes():
	print("Adding indicator descriptions")

	codes_idc = open("{0}{1}".format(raw_data_directory, "series.csv"), 'r')
	codes_reader = csv.reader(codes_idc)

	codes_formatted_idc = open("{0}{1}".format(formatted_data_directory, "indicator-codes.csv"), 'r')
	codes_formatted_reader = csv.reader(codes_formatted_idc)

	codes_formatted = []
	for i in codes_formatted_reader:
		codes_formatted.append(i[0])

	codes_formatted_idc.close()

	codes_desc_idc = open("{0}{1}".format(formatted_data_directory, "indicator-desc.csv"), 'w', newline='')
	codes_desc_writer = csv.writer(codes_desc_idc)

	for i in codes_reader:
		if i[0] in codes_formatted:
			codes_desc_writer.writerow(i)

def run():
	create_formatted_outputs()
	describe_codes()

if __name__ == "__main__":
	run()