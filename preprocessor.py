import os
import csv

raw_data_directory = os.path.join("data-raw/")
formatted_data_directory = os.path.join("data-formatted/")

country_codes = ["BRN", "KHM", "IDN", "LAO", "MYS", "MMR", "PHL", "SGP", "THA", "VNM", "WLD"]

def limit_csv():
	print("Generating limited csv file.")

	raw_idc = open("{0}{1}".format(raw_data_directory, "indicators.csv"), 'r')
	raw_reader = csv.reader(raw_idc)

	codes_idc = open("{0}{1}".format(formatted_data_directory, "indicator-codes.csv"), 'r')
	codes_reader = csv.reader(codes_idc)
	codes = [i[0] for i in codes_reader]
	codes_idc.close()

	out_idc = open("{0}{1}".format(formatted_data_directory, "indicators.csv"), 'w', newline='')
	out_writer = csv.writer(out_idc)

	for i in raw_reader:
		if i[1] in country_codes and i[3] in codes:
			out_writer.writerow(i)

	raw_idc.close()
	out_idc.close()

def run():
	limit_csv()

if __name__ == "__main__":
	run()