import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl

import os

formatted_data_directory = os.path.join("data-formatted/")

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

def run():
	pass

if __name__ == "__main__":
	run()