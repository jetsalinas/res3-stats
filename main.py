from scipy.stats import *
import numpy
import csv

import os


csv_directory = os.path.join("data-formatted")

def load_csv(name = None):
	csvfiles = []
	if name is None:
		names = os.listdir(csv_directory)
		try:
			for name in names:
				csvfiles.append(open("{0}/{1}".format(csv_directory, name), mode='r'))
				print("Found csv files: " + names.__str__())
		except FileNotFoundError:
			print("No csv files found")
			return None
	else:
		try:
			csvfiles.append(open("{0}/{1}".format(csv_directory, name), mode='r'))
			print("Found csv files: " + name)
		except:
			print("No csv file found")
			return None
	return csvfiles

def debug():
	print("Debug function running")

if __name__ == "__main__":
	load_csv()