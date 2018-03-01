import os
import csv

raw_data_directory = os.path.join("data-raw/")
formatted_data_directory = os.path.join("data-formatted/")

country_codes = ["BRN", "KHM", "IDN", "LAO", "MYS", "MMR", "PHL", "SGP", "THA", "VNM", "WLD"]

def limit_countries():
	raw_idc = open("{0}{1}".format(raw_data_directory, "indicators.csv"), 'r')
	raw_reader = csv.reader(raw_idc)

	out_idc = open("{0}{1}".format(formatted_data_directory, "indicators-sea.csv"), 'w', newline='')
	out_writer = csv.writer(out_idc)

	for i in raw_reader:
		if i[1] in country_codes:
			out_writer.writerow(i)

	raw_idc.close()
	out_idc.close()

def limit_countries_and_indicators():
	
	limit_countries()

	codes_idc = open("{0}{1}".format(formatted_data_directory, "indicator-codes.csv"), 'r')
	codes_reader = csv.reader(codes_idc)
	codes = []
	for i in codes_reader:
		codes.append(i[0])
	codes_idc.close()

	sea_idc = open("{0}{1}".format(formatted_data_directory, "indicators-sea.csv"), 'r')
	sea_reader = csv.reader(sea_idc)

	out_idc = open("{0}{1}".format(formatted_data_directory, "indicators-sea-limited.csv"), 'w', newline='')
	out_writer = csv.writer(out_idc)

	for i in sea_reader:
		if i[3] in codes:
			out_writer.writerow(i)

	sea_idc.close()
	out_idc.close()

if __name__ == "__main__":
	limit_countries_and_indicators()