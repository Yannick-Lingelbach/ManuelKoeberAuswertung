# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:30:45 2019

@author: LYI9FE
"""
print(chr(27) + "[2J") # Clear Console

import pandas as pd
#import numpy as np
#from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
import os


# Import data to be analysed
Manuel = False

if Manuel:
    actual_path='U:/Bachelorarbeit/Messdaten'
    folder_name = '/19_05_07'
else:
    actual_path='C:/Users/LYI9Fe/Documents/10_PythonProject/30_Koeber_Manuel'
    folder_name = '/Data'

##############################################################

listdir = pd.Series(os.listdir(actual_path+folder_name))

# -> Select from List of Files read in:
file_number=list(range(12,13)) 
#file_number=[0,3,4]

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

######## Figure 1: Plotting the Temperature ##########

# -> Select from List of Measurements:
lst_curves_1=[2,3,4] # Erste Y-Axe 
lst_curves_2=[1]     # Zweite Y-Axe

matplotlib.pyplot.close()

marker ={0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-', 7:'-', 8:'-',9:'-',10:'-',11:'-',12:'-',13:'-', 14:'-'}
#marker.extend(list(pd.Series(matplotlib.markers.MarkerStyle().markers).index))

if True:
    fig, ax1 = plt.subplots()
    
    color = matplotlib.rcParams['axes.prop_cycle'].by_key()['color']
    
    for i in lst_curves_1:
        ax1.plot(df_all_days['Systemzeitdiagramm'], df_all_days.iloc[:,i], label=df_all_days.columns[i],linewidth=1.0)
 
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    
    for i in lst_curves_2:
        ax2.plot(df_all_days['Systemzeitdiagramm'], df_all_days.iloc[:,i], label=df_all_days.columns[i],linewidth=1.0,color='r')
 
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
        
    ax1.set(xlabel='time', ylabel='% Percentage',
              title='Percentage of Gas in furnace')
    ax1.legend(loc=2)
    
    ax2.set(xlabel='time', ylabel='% Percentage',
          title='Percentage of Gas in furnace')
    ax2.legend(loc=1)
    ax2.tick_params(axis='y', labelcolor='r')
    ax1.grid()
    ax1.tick_params(axis="x", rotation=50,labelsize=8 )
    
    myFmt = mdates.DateFormatter('%d %b %H:%M')
    ax1.xaxis.set_major_formatter(myFmt)













