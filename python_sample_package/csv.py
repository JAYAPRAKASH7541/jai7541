import csv
with open("python_sample_package/names.csv",'r') as csv_file:
	reader = csv.reader(csv_file)
print(reader)
