from scipy import stats
import numpy
import csv

import os


def debug():
	print("Debug function running.")

csv_directory = os.path.join("data-formatted")

def load_csv(name = None):
	csv_files = []
	if name is None:
		names = os.listdir(csv_directory)
		try:
			for name in names:
				csv_files.append(open("{0}/{1}".format(csv_directory, name), mode='r'))
			print("Loading csv files: " + names.__str__())
		except FileNotFoundError:
			print("No csv files found")
			return None
	else:
		try:
			csv_files.append(open("{0}/{1}".format(csv_directory, name), mode='r'))
			print("Loading csv file: " + name)
		except:
			print("No csv file found")
			return None
	return csv_files

def debug_csv(lines = 2):
	csv_files = load_csv()
	for i in csv_files:
		f = csv.reader(i)
		for j in range(lines):
			print(", ".join(f.__next__()))
		print()

def pearson_correlate(csv_files = None):
	output = []
	if csv_files is None:
		csv_files = load_csv()
	for i in csv_files:
		for j in csv_files:
			print(i.name)
			print(j.name)
			if i == j:
				print("Found same file: breaking")
				print("===========================")
				continue
			x_reader = csv.reader(i)
			y_reader = csv.reader(j)

			x_data = []
			y_data = []

			country_name = ""
			country_code = ""

			for x_row, y_row in zip(x_reader, y_reader):

				country_name = x_row[0].replace(",", "")
				country_code = x_row[1]
				
				for m in x_row[2:]:
					try:
						x_data.append(float(m))
					except ValueError:
						x_data.append(0)
			
				for m in y_row[2:]:
					try:
						y_data.append(float(m))
					except ValueError:
						y_data.append(0)

				r, p_value = stats.pearsonr(x_data, y_data)
				r = float(r)
				p_value = float(p_value)

				output.append([country_name, country_code, r, p_value])
				
			x_data = []
			y_data = []
			print("===========================")

	return output

results_directory = os.path.join("results-formatted")

def pearson_save(pearson_results = None):
	if pearson_results is None:
		pearson_results = pearson_correlate()
	with open("{0}/{1}".format(results_directory, "pearson_results.csv"), mode = 'w') as output:
		for i in pearson_results:
			output.write(",".join([str(m) for m in i]) + "\n")
			
def run_stats():
	csv_files = load_csv()
	pearson_results = pearson_correlate(csv_files)
	pearson_save(pearson_results)

if __name__ == "__main__":
	run_stats()