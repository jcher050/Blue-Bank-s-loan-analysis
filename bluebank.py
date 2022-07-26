# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:50:36 2022

@author: chery
"""

import json 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data 
json_file = open ('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp() to get the annual income 
income = np.exp(loandata['log.annual.inc'])
loandata['Annualincome'] = income


    
#applying for loops to loan data 

#using first 10

length =len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >=780:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Error - Unknown'
        
    
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)  

loandata['fico.category'] = ficocat
    
    
    
# df.loc as conditional statements
# df.loc[df[columnname] condition, newcolumnname] = 'value if the condition is met'

#for interest rates, a new column is wanted. rate > 0.12 then high, else low 

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type']= 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type']= 'Low'
    

#number of loans?rows by fico.category'
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='red', width = 0.2)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='green', width = 0.3)
plt.show()

#scatter plots
ypoint = loandata['Annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#2caf55')
plt.show()
    
    
#writing to csv 
loandata.to_csv('loan_cleaned.csv', index = True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    