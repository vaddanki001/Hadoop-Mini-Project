#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np

file_list = []
for line in sys.stdin:
  line = line.strip()
  line_fields = line.split(',')
  file_list.append(line_fields)

df = pd.DataFrame(file_list, columns = ["Incident_Id","Incident_type","VIN","Make","Model","Year","Incident_date","Description"])

df.sort_values(by='VIN',inplace = True)
df_replaced = df.replace(r'^\s*$', np.nan, regex=True)

df_replaced.fillna(method='ffill',inplace =True)

for row in df_replaced.itertuples():
  if row.Incident_type == 'A':
    print('%s\t%s' % (row.VIN, row.Incident_type+"_"+row.Make+"_"+row.Year))