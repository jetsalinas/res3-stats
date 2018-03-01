import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl

from scipy import stats

import os
import csv

formatted_data_directory = os.path.join("data-formatted/")
results_directory = os.path.join("results/")

def get_data():
	data = pd.read_csv("{0}{1}".format(formatted_data_directory, "indicators.csv"))
	brn = data[(data['country_code'] == 'BRN')]
	khm = data[(data['country_code'] == 'KHM')]
	idn = data[(data['country_code'] == 'IDN')]
	lao = data[(data['country_code'] == 'LAO')]
	mys = data[(data['country_code'] == 'MYS')]
	mmr = data[(data['country_code'] == 'MMR')]
	phl = data[(data['country_code'] == 'PHL')]
	sgp = data[(data['country_code'] == 'SGP')]
	tha = data[(data['country_code'] == 'THA')]
	vnm = data[(data['country_code'] == 'VNM')]

	data = {"BRN": brn, "KHM": khm, "IDN": idn, "LAO": lao, "MYS": mys, "MMR": mmr, "PHL": phl, "SGP": sgp, "THA": tha, "VNM": vnm}
	return data

def linear_regression(country_code):

	codes_idc = open("{0}{1}".format(formatted_data_directory, "indicator-desc.csv"), 'r')
	codes_reader = csv.reader(codes_idc)
	codes = [i[0] for i in codes_reader]

	linear_file = open("{0}regression-{1}.csv".format(results_directory, country_code), 'w', newline='')
	linear_writer = csv.writer(linear_file)

	data = get_data()[country_code]

	linear_writer.writerow(['country_code', 'indicator_code_0', 'indicator_code_1', 'slope', 'intercept', 'r_value', 'p_value', 'std_err'])
	for i in codes:
		for j in codes:
			if i == j:
				pass

			x = data[data['indicator_code'] == i].sort_values(by='year')
			y = data[data['indicator_code'] == j].sort_values(by='year')

			try:
				slope, intercept, r_value, p_value, std_err = stats.linregress(x['value'], y['value'])
				linear_writer.writerow([country_code.lower(), i, j, slope, intercept, r_value, p_value, std_err])
			except Exception as e:
				print("Skipping indicators : {0} {1}".format(i, j))

	codes_idc.close()
	linear_file.close()

def run():
	linear_regression("PHL")

if __name__ == "__main__":
	run()