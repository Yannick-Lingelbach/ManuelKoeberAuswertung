# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:30:45 2019

@author: LYI9FE
"""
print(chr(27) + "[2J") # Clear Console

import pandas as pd
from pandas import ExcelWriter
import os


# Import data to be analysed
Manuel = False

if Manuel:
    actual_path='U:/Bachelorarbeit/Messdaten'
    folder_name = '/19_05_07'
else:
    actual_path='C:/Users/LYI9Fe/Documents/10_PythonProject/30_Koeber_Manuel'
    folder_name = '/Data'
    
folder_out  = '/Output/'
export_name = 'PythonExport.xlsx'

##############################################################

listdir = pd.Series(os.listdir(actual_path+folder_name))

# -> Select from List of Files read in:
file_number=list(range(12,32)) 

list_df_fur=[]

# Read in Data from furnace
dateparse = lambda x: pd.datetime.strptime(x, '%d.%m.%Y %H:%M:%S')

for i in file_number:
    df_my_import   = pd.read_csv(actual_path+folder_name+'/'+listdir[i],
                           sep="\t",skipfooter=1,decimal='.',encoding = 'unicode_escape', parse_dates=['Systemzeitdiagramm'], date_parser=dateparse,engine='python')
    list_df_fur.append(df_my_import)

df_all_days = pd.concat(list_df_fur)

######## Data Cleaning ######## 

df_all_days['Systemzeitdiagramm']= pd.to_datetime(df_all_days['Systemzeitdiagramm'],format='%Y-%m-%d %H:%M:%S', errors='ignore')
  
print('-> List of Files read in: \n\n' 
      + str(listdir) 
      + '\n\n-> List of Measurements: \n')

for i,val in enumerate(df_my_import.dtypes.iteritems()):
    print('['+str(i)+']'+'\t'+str(val[0]))


df_all_days.set_index('Systemzeitdiagramm',inplace=True)

writer = ExcelWriter(actual_path+folder_out+export_name)
df_all_days.to_excel(writer,'Sheet1')
writer.save()








