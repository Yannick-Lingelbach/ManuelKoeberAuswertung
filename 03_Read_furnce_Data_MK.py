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
import matplotlib
import os


actual_path='C:/Users/LYI9Fe/Documents/10_PythonProject/30_Koeber_Manuel'
# Import data to be analysed

listdir = pd.Series(os.listdir(actual_path+'/Data'))

# -> Select from List of Files read in:
file_number=list(range(8)) 
#file_number=[0,3,4]
file_number=[30,31]

list_df_fur=[]

# Read in Data from furnace
for i in file_number:
    df_my_import   = pd.read_csv(actual_path+'/Data/'+listdir[i],
                           sep="\t",skipfooter=1,decimal='.',encoding = 'unicode_escape', parse_dates=['Systemzeitdiagramm'],engine='python')
    list_df_fur.append(df_my_import)

######## Data Cleaning ######## 
    
# Set all timestamps to same start point then Find start of 'Solltemoeratur'>0 
# and align all curves to that startpoint by shifting them

list_start_time = []


for df in list_df_fur:
    df.insert(loc=1, column='Zeit', value = df['Systemzeitdiagramm']-df.loc[0,'Systemzeitdiagramm'])
    
    #i=0
    #while (df.loc[i,'SOLLTEMPERATUR[°C]'] == 0) and (i<len(df)):
    #    i +=1
    #list_start_time.append(df.loc[i,'Zeit'])  
        
# now shift all time series to allign with the latest start point
#latest_start = max(list_start_time)

#for i,df in enumerate(list_df_fur):
#    df.Zeit = df.Zeit+latest_start-list_start_time[i]
    

  
print('-> List of Files read in: \n\n' 
      + str(listdir) 
      + '\n\n-> List of Measurements: \n')

for i,val in enumerate(df_my_import.dtypes.iteritems()):
    print('['+str(i)+']'+'\t'+str(val[0]))

######## Figure 1: Plotting the Temperature ##########

# -> Select from List of Measurements:
lst_curves=[3,4,5]

matplotlib.pyplot.close()

marker ={0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-', 7:'-', 8:'-',9:'-',10:'-',11:'-',12:'-',13:'-', 14:'-'}
#marker.extend(list(pd.Series(matplotlib.markers.MarkerStyle().markers).index))

if True:
    fig, temp = plt.subplots()
    
    color = matplotlib.rcParams['axes.prop_cycle'].by_key()['color']
    
    for count,df in enumerate(list_df_fur):
        for i in lst_curves:
            temp.plot(pd.to_datetime(df['Zeit']).dt.time, df.iloc[:,i],marker[count], label=str(count)+'_'+df.columns[i],linewidth=1.0)
        
    temp.set(xlabel='time', ylabel='% Percentage',
              title='Percentage of Gas in furnace')
    temp.legend()
    temp.grid()


######## Figure 2:  Plotting the Pressure ##########

# -> Select which Curves to plot
lst_pres_curves=[6]
marker_press = {0:'-',1:'-',2:'-',3:'-',4:'-',5:'-',6:'-', 7:'-', 8:'-',9:'-',10:'-',11:'-',12:'-',13:'-', 14:'-'}

if False:
    fig, pres = plt.subplots()
    for count,df in enumerate(list_df_fur):
        for curve in lst_pres_curves:
            pres.plot(pd.to_datetime(df['Zeit']).dt.time, df.iloc[:,curve],marker_press[curve],c=color[count], label=str(count)+'_'+df.columns[curve],linewidth=1.0)
        
    pres.set(xlabel='time', ylabel='pressure (mbar)',
              title='Pressure of Gas in furnace')
    pres.set_yscale("log", nonposy='clip')
    pres.legend()
    pres.grid()


######## Figure 3:  Plotting Temperature and Pressure ##########

if False:
    fig, temp2 = plt.subplots()
    lines = []
    
    File_numb = file_number.index(3)
    df = list_df_fur[File_numb]
    
    lst_temp_curves2 = [2]
    lst_pres_curves2 = [3]
    
    col_temp=['darkred','red','lightred']
    col_pres=['darkblue','blue','lightblue']
    
    for i,curve in enumerate(lst_temp_curves2):
        lines += temp2.plot(pd.to_datetime(df['Zeit']).dt.time, df.iloc[:,curve],marker[curve],c=col_temp[i], label=str(File_numb)+'_'+df.columns[curve],linewidth=1.0)
        
    temp2.set(xlabel='time',title='Temperature and Pressure in furnace')
    temp2.set_ylabel('temperature (°C)', color=col_temp[0])
    
    pres2 = temp2.twinx()

    for j,curve in enumerate(lst_pres_curves2):
        lines += pres2.plot(pd.to_datetime(df['Zeit']).dt.time, df.iloc[:,curve],marker_press[curve],c=col_pres[j], label=str(File_numb)+'_'+df.columns[curve],linewidth=1.0)
    
    pres2.set_ylabel('pressure (mbar)', color=col_pres[0])  # we already handled the x-label with ax1
    #pres2.set_yscale("log", nonposy='clip')
    
    temp2.legend(lines, [l.get_label() for l in lines])

    

#tem_pre.set_yscale("log", nonposy='clip')
#
#tem_pre.grid()  











