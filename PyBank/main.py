#Import libraries to use
import csv
import pathlib


#Set path for finding csv file

csv_path = pathlib.Path('Resources/budget_data.csv')

#Create lists to store the data
my_list=[]
profit_loss = []
date_combined = []


#Open csv file and read
with open(csv_path) as csv_file:
    csv_data = csv.reader(csv_file)
    
    #can skip header row and save if needed for later
    csv_header=next(csv_data)

    #once skipped append values to separate lists
    for row in csv_data:
        date_combined.append(row[0])
        profit_loss.append(int(row[1]))


#count total # of months a
tot_mon=len(date_combined)

# Calculate overall profit loss, sum it all up
net_tot=sum(profit_loss)

# Calculate average change in profit/loss
avg_pl=round((net_tot/tot_mon),2)

#Calculate max/min
gr_inc=int(max(profit_loss))
gr_dec=int(min(profit_loss))

#find index location for each value
gr_inc_idx=profit_loss.index(gr_inc)
gr_dec_idx=profit_loss.index(gr_dec)

#Print it all out
print("'''text")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {tot_mon}")
print(f"Total: ${net_tot}")
print(f"Average Change: ${avg_pl}")
print(f"Greatest Increase in Profits: {date_combined[gr_inc_idx]} (${profit_loss[gr_inc_idx]})")
print(f"Greatest Decrease in Profits: {date_combined[gr_dec_idx]} (${profit_loss[gr_dec_idx]})")
print("'''")

#Create Output Path
output_path = pathlib.Path('Analysis/Results.txt')

#Write output to output path
with open(output_path, 'w') as output:
    output.write("'''text \n")
    output.write("Financial Analysis \n")
    output.write("---------------------------- \n")
    output.write(f"Total Months: {tot_mon} \n")
    output.write(f"Total: ${net_tot} \n")
    output.write(f"Average Change: ${avg_pl} \n")
    output.write(f"Greatest Increase in Profits: {date_combined[gr_inc_idx]} (${profit_loss[gr_inc_idx]}) \n")
    output.write(f"Greatest Decrease in Profits: {date_combined[gr_dec_idx]} (${profit_loss[gr_dec_idx]}) \n")
    output.write("'''" )

