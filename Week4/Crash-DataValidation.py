#!/usr/bin/env python
# coding: utf-8



import pandas as pd
df = pd.read_csv('Crash-data.csv')




#for existence assertion
data = df[df['Crash ID'] != 'NULL']
print(data)





#limit assertion : "Every crash occurred with highway number 26"

df=df[df['Highway Number']==26]





# intra-record assertions
# For every crash id there must be a latitude and longitude
for index, row in df.iterrows():
    if row['Record Type'] == 1:
        if not row['Latitude Degrees'] and not row['Longitude Degrees']:
            df.drop(index, inplace=True)
print(len(df))




# inter-record assertions
# For every crashId there will be atleast one vehicle id
for index, row in df.iterrows():
    if row['Record Type'] == 2:
        if not row['Vehicle ID']:
            print("Did not find vehicle Id for the record on index ", index, row['Crash ID'])
            df.drop(index, inplace=True)
print(len(df))





#Summary assertion: "Crash record is unique across all the records"
dup_rows = df[df.duplicated()]
df_remove_dup = df.drop_duplicates(subset ="Crash ID",keep='first')





#statistical distribution assertion : “crashes are evenly/uniformly distributed throughout the months of the years"
import matplotlib.pyplot as plt

xlabel='Crash Month'
ylabel='Crash Day'
df.plot(xlabel,ylabel,color = 'Red', kind= 'scatter')
plt.grid()
plt.show()







