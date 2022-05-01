'''
EMIS Group test for joining JSON files to a FHIR file
This is donw with the use of Pandas and
'''

import os

<<<<<<< HEAD
import pandas as pd
import json

path = os.path.join("C:\\Users", os.getenv('username'), "Python-dev\\EMIStest", "")
=======

path = os.path.join("C:\\Users", os.getenv('username'), "python-dev/EMISGroup-solusion/", "")
>>>>>>> origin/master
print(path)

base_dir = os.path.dirname(path)
data_dir = os.path.join(base_dir,"data")
my_dataframe = []

for filename in os.listdir(data_dir):

    # get the path of each of the data files
    json_path = os.path.join(data_dir,filename)

    this_df = pd.read_json(json_path)
<<<<<<< HEAD
    this_df.info()
    # this is the dataframe that appends the each data file in
    entry = this_df['entry'].values[0]

    entry_df = pd.DataFrame(entry)
    # print(entry_df)
    # out = os.path.join(base_dir,"out.csv")
    # entry_df.to_csv(out)
    url_out = entry_df['resource'].values[2]
    id_out = entry_df['resource'].values[1]
    meta = entry_df['resource'].values[3]
    profile = url_out['profile']

    text = entry_df['resource'].values[4][0]
    print(text)
    # print(url_out)
    print(id_out)
    print(profile[0])
    print(meta)


    # clean up the data
def clean_up(row):
    pass



=======

    # this is now normalized into rows and columns
    result = pd.json_normalize(this_df)
    print(result)
>>>>>>> origin/master










