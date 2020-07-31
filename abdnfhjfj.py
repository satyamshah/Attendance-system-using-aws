# importing the csv module
import csv

# my data rows as dictionary objects

fields = ['Faceid','Name', 'Date']
filename = "attendance1.csv"

mydict  = {'Faceid': None, 'Name': None,'Date':None}
# field names
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerow(mydict)
