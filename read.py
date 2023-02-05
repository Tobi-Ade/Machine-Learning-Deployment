import os, pandas as pd 

current_dir = os.getcwd()
for file in os.listdir(current_dir):
    file_type = 'csv'
    if file.endswith(file_type):
        file_name = os.path.join(current_dir,  file)

# print(file_name)

## read with pandas dataframe 

consumer_complaints = pd.read_csv(file_name)
pd.set_option('display.max_columns', None)

print(consumer_complaints.head())