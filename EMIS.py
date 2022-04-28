'''
EMIS Group test for joining JSON files to a FHIR file
This is donw with the use of Pandas and
'''

import pandas as pd
import os


path = os.path.join("C:\\Users", os.getenv('username'), "python-dev/EMISGroup-solusion/", "")
print(path)

base_dir = os.path.dirname(path)
data_dir = os.path.join(base_dir,"data")
my_dataframe = []

for filename in os.listdir(data_dir):

    # get the path of each of the data files
    json_path = os.path.join(data_dir,filename)

    this_df = pd.read_json(json_path)

    # this is now normalized into rows and columns
    result = pd.json_normalize(this_df)
    print(result)










