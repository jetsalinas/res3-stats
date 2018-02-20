from scipy.stats import *
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
			print("Found csv files: " + names.__str__())
		except FileNotFoundError:
			print("No csv files found")
			return None
	else:
		try:
			csv_files.append(open("{0}/{1}".format(csv_directory, name), mode='r'))
			print("Found csv files: " + name)
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

def run_stats():
	csv_files = load_csv()

if __name__ == "__main__":
	run_stats()