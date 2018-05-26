#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 17:54:25 2018

@author: roy
"""
import os as path
import csv

budget_path1 = "/Users/roy/Desktop/Repository/python-challenge/PyBank/budget_data_1.csv"
budget_path2 = "/Users/roy/Desktop/Repository/python-challenge/PyBank/budget_data_2.csv"

total_months = 0
total_revenue = 0

change_total = 0.0
change_average = 0.0

revenue_list = []
revenue_list2 = []
change_list = []
month_list = []
counter = 0

with open(budget_path1, newline='') as budget1_0:
    csvreader = csv.reader(budget1_0, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        #counting total months
        total_months += 1
        #adding all the revenue
        total_revenue += int(row[1])
        #creating a copy of revenues in a list
        revenue_list.append(row[1])
        month_list.append(row[0])
        
with open(budget_path1, newline='') as budget1_1:
    csvreader = csv.reader(budget1_1, delimiter=',')
    #skipping first two lines
    csvheader = next(csvreader)
    csvheader = next(csvreader)
    for row in csvreader:
        #getting the total change by substracting second month revenue from the first month revenue
        change_total = int(revenue_list[0]) - int(row[1])
        revenue_list2.append(row[1])       
    #dividing the total change by number of changes
    change_average = change_total / (total_months -1)

#creating a list of changes 
for a in range(len(revenue_list2)):
    change = int(revenue_list[a]) - int(revenue_list2[a])
    change_list.append(change)

#finding the greatest increase and its position
great_increase = change_list[0]
increase_index = 0
for a in range(len(change_list)):
    if change_list[a] > great_increase:
        great_increase = change_list[a]
        increase_index = a

#finding the greatest decrease and its position
great_decrease = change_list[0]
decrease_index = 0
for a in range(len(change_list)):
    if change_list[a] < great_decrease:
        great_decrease = change_list[a]
        decrease_index = a
    
#printing to terminal
print("Financial Analysis" + '\n'+"------------------------------------------")
print("Total Months: "+str(total_months))
print("Total Revenue: $"+str(total_revenue))
print("Average Revenue Change: $"+str(change_average))
print("Greatest Increase in Revenue: "+month_list[increase_index+1] + " ($"+str(great_increase)+")")
print("Greatest Increase in Revenue: "+month_list[decrease_index+1] + " ($"+str(great_decrease)+")")

#creating a textfile
def createFile(dest):
    name = "PyBank.txt"
    f = open(name,'w')
    f.write("Financial Analysis" + '\n'+"------------------------------------------"+ '\n')
    f.write("Total Months: "+str(total_months)+ '\n')
    f.write("Total Revenue: $"+str(total_revenue)+ '\n')
    f.write("Average Revenue Change: $"+str(change_average)+ '\n')
    f.write("Greatest Increase in Revenue: "+month_list[increase_index+1] + " ($"+str(great_increase)+")"+ '\n')
    f.write("Greatest Increase in Revenue: "+month_list[decrease_index+1] + " ($"+str(great_decrease)+")")
    f.close
if __name__=='__main__':
    destination = "/Users/roy/Desktop/python-challenge/PyBank"
    createFile(destination)
createFile("/Users/roy/Desktop/python-challenge/PyBank")