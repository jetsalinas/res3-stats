import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl

import os

formatted_data_directory = os.path.join("data-formatted/")

def analyze():

	indicators = pd.read_csv("{0}{1}".format(formatted_data_directory, "indicators.csv"))
	print(indicators.tail())

def run():
	analyze()

if __name__ == "__main__":
	run()