import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl

import os

formatted_data_directory = os.path.join("data-formatted/")

def get_data():
	data = pd.read_csv("{0}{1}".format(formatted_data_directory, "indicators.csv"))
	#headers: country_name country_code indicator_name indicator_code year value
	return data

def run():
	analyze()

if __name__ == "__main__":
	run()