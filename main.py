from scipy import stats
import numpy
import matplotlib.pyplot
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
	"Running pearson correlation tests."
	output = []
	if csv_files is None:
		csv_files = load_csv()
	for i in csv_files:
		for j in csv_files:
			if i == j:
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

	return output

results_directory = os.path.join("results-formatted")

def pearson_save(pearson_results = None):
	print("Saving pearson correlation test results.")
	if pearson_results is None:
		pearson_results = pearson_correlate()
	with open("{0}/{1}".format(results_directory, "pearson_results.csv"), mode = 'w') as output:
		for i in pearson_results:
			output.write(",".join([str(m) for m in i]) + "\n")


images_directory = os.path.join("results-formatted\line-plots")

def plot_images(csv_files = None, years = (1960, 2017)):
	print("Saving plot images.")
	output = []
	if csv_files is None:
		csv_files = load_csv()
	lmao = 1
	for i in csv_files:
		for j in csv_files:
			if i == j:
				continue
			y1_reader = csv.reader(i)
			y2_reader = csv.reader(j)

			y1_data = []
			y2_data = []

			country_name = ""
			country_code = ""

			i_name = i.name.split("/")[1].split(".")[0]
			j_name = j.name.split("/")[1].split(".")[0]

			for y1_row, y2_row in zip(y1_reader, y2_reader):

				country_name = y1_row[0].replace(",", "")
				country_code = y2_row[1]
				
				for m in y1_row[2:]:
					try:
						x1_data.append(float(m))
					except ValueError:
						x1_data.append(None)
			
				for m in y2_row[2:]:
					try:
						y2_data.append(float(m))
					except ValueError:
						y2_data.append(None)

				x_axis = [i for i in range(years[0], years[1])]
				plt = pyplot.plot(x_axis, y1_data, 'rs', x_axis, y2_data, 'b^')
				plt.show()
				print("Saving image: {0}/{1}-{2} {3}.png".format(images_directory, i_name, j_name, country_code))
				plt.savefig("{0}/{1}-{2} {3}.png".format(images_directory, i_name, j_name, country_code))

				if lmao == 1:
					pyplot.ioff()
					lmao = 2



def run_stats():
	csv_files = load_csv()
	pearson_results = pearson_correlate(csv_files)
	pearson_save(pearson_results)
	plot_images(csv_files)

if __name__ == "__main__":
	run_stats()