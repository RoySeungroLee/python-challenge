#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 11:37:01 2018

@author: roy
"""

import os
import csv

employee_path1 = "/Users/roy/Desktop/Repository/python-challenge/PyBoss/employee_data1.csv"
employee_path2 = "/Users/roy/Desktop/Repository/python-challenge/PyBoss/employee_data2.csv"

emp_id = []
name = []
name_split = []
first_name = []
last_name = []
dob = []
ssn = []
ssn_split = []
state = []
us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID','Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
    'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
    'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO','Montana': 'MT',
    'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM',
    'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
    'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
}

#getting separate lists for each column
with open(employee_path1, newline ='') as employee_csv1:
    employee_reader = csv.reader(employee_csv1, delimiter =',')
    csvheader = next(employee_reader)
    for row in employee_reader:
        #print(row)
        emp_id.append(row[0])
        #take entire name first
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
        
#separating first and last name
for a in range(len(name)):
    name_split.append(name[a].split())
    first_name.append(name_split[a][0])
    last_name.append(name_split[a][1])
    
#changing date format
for a in range(len(dob)):
    dob[a] = dob[a].replace('-','/')

#hiding a portion of ssn
for a in range(len(ssn)):
    ssn_split.append(ssn[a].split('-'))
    ssn[a] = ssn_split[a][2]
    ssn[a] = "***-**-" + str(ssn[a]) 

#state abbreviation
for a in range(len(state)):
    state[a] = us_state_abbrev[state[a]]

components = zip(emp_id,first_name,last_name,dob,ssn,state)


output = "/Users/roy/Desktop/Repository/python-challenge/PyBoss/PyBoss.csv"
with open(output,'w',newline='') as datafile:
   writer = csv.writer(datafile)
   writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
   writer.writerows(components)

        
        

        