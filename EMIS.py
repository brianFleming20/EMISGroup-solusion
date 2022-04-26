'''
EMIS Group test for joining JSON files to a FHIR file
This is donw with the use of Pandas and
'''

import pandas as pd
import os

path = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\exa-data-eng-assessment-main", "")
print(path)

base_dir = os.path.dirname(path)
data_dir = os.path.join(base_dir,"data")
my_dataframe = []

for filename in os.listdir(data_dir):
    print(filename)
    # get the path of each of the data files
    json_path = os.path.join(data_dir,filename)

    this_df = pd.read_json(json_path)
    #print(this_df.head())
    # this is the dataframe that appends the each data file in
    my_dataframe.append(this_df)
    # this is all of the data in one data frame
    my_entire_dataframe = pd.concat(my_dataframe)
    print(my_entire_dataframe.head(n=2))
    # prints 2 of each of the head of the data files from the whole data frame

    # create a new complete data frame
    cashe_dir = os.path.join(base_dir,"cashe")
    os.makedirs(cashe_dir,exist_ok=True)







