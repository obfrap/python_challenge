#Import libraries to use
import csv
import pathlib
import os

#Set path for finding csv file

csv_path = pathlib.Path('Resources/budget_data.csv')

#Create lists to store the data
my_list=[]
profit_loss = []
date_combined = []
month = []
year = []

#Open csv file and read
with open(csv_path) as csv_file:
    csv_data = csv.reader(csv_file)
    
    #can skip header row and save if needed for later
    csv_header=next(csv_data)

    #once skipped append values to separate lists
    for row in csv_data:
        date_combined.append(row[0])
        profit_loss.append(int(row[1]))
#print(date_combined)
#print(profit_loss)

#count total # of months
tot_mon=len(date_combined)
#print(tot_mon)
net_tot=sum(profit_loss)
#print(net_tot)
avg_pl=round((net_tot/tot_mon),2)
#print(avg_pl)
gr_inc=int(max(profit_loss))
gr_dec=int(min(profit_loss))
#print(gr_inc)
#print(gr_dec)

#find index location for each value
gr_inc_idx=profit_loss.index(gr_inc)
gr_dec_idx=profit_loss.index(gr_dec)
#print(gr_inc_idx)

#Print it all out
print(f"Total Months: {tot_mon}")
print(f"Total: ${net_tot}")
print(f"Average Change: ${avg_pl}")
print(f"Greatest Increase in Profits: {date_combined[gr_inc_idx]} (${profit_loss[gr_inc_idx]})")
print(f"Greatest Decrease in Profits: {date_combined[gr_dec_idx]} (${profit_loss[gr_dec_idx]})")
