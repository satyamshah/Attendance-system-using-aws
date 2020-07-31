# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("attendance.csv")

# sorting by first name


# dropping ALL duplicte values
data.drop_duplicates(subset ="Name",
					keep = False, inplace = True)

# displaying data
data
