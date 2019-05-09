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
Manuel = True

if Manuel:
    actual_path='U:/Bachelorarbeit/Messdaten'
    folder_name = '/19_05_07'
else:
    actual_path='C:/Users/LYI9Fe/Documents/10_PythonProject/30_Koeber_Manuel'
    folder_name = '/Data'



##############################################################

listdir = pd.Series(os.listdir(actual_path+folder_name))

# -> Select from List of Files read in:
file_number=list(range(12,32)) 
#file_number=[0,3,4]
#file_number=[16,17]
#file_number=list(range(3,39))

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











