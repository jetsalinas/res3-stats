import os
import csv


raw_data_directory = os.path.join("data-raw/")
formatted_data_directory = os.path.join("data-formatted/")

def limit_sea_countries():
	country_codes = ["BRN", "KHM", "IDN", "LAO", "MYS", "MMR", "PHL", "SGP", "THA", "VNM", "WLD"]
	
	raw_idc = open("".join(raw_data_directory, "indicators.csv"), 'r')
	raw_reader = csv.reader(raw_idc)

	out_idc = open("".join(formatted_data_directory, "indicators.csv"), 'w')
	out_writer = csv.writer(out_idc)

	for i in raw_reader:
		if i[1] in country_codes:
			out_writer.writerow(i)

	raw_idc.close()
	out_idc.close()



