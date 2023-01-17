import os
import csv

# path to read and write files
read_path = os.path.join('Resources', 'budget_data.csv')
write_path = os.path.join('analysis', 'output.txt')

# creating and assigning variables needed for calculating 
month_counter = 0
net_total= 0
average_change= 0
great_in_profit = 0
great_de_profit = 0
previous_row = 0
change = 0
change_list = list()

#opening csv file to parse and perform calculations
with open(read_path) as csvfile:
    # reading the file an assigning "," as the delimeter
    csvreader = csv.reader(csvfile, delimiter = ',')

    # getting rid of the column names
    csv_header = next(csvreader)

    # iterating over the file 
    for row in csvreader:
        # as long as the first element of row contains a date value add one to the month counter
        if row[0] is not None:
            month_counter += 1
        
        # set current row  to the current Profit/Losses value
        current_row = int(row[1])

        # Continue adding each elements of the row containing the Profit/Losses value
        # to obtain the net total
        net_total += int(row[1])

        # calculate change in Profit/Losses from the current and previous value
        change = current_row -  previous_row

        # append the changes in profit/losses to a list for future calculations
        change_list.append(change)

        # if the current change is greater than the greatest increase in profit
        # assign it's value to great_in_profit and save the date
        if great_in_profit < change:
            great_in_profit = change
            great_in_date = row[0]

        # if the current change is less than the greatest decrease in profit
        # assign it's value to great_de_profit and save the date
        if great_de_profit > change:
            great_de_profit = change
            great_de_date = row[0]
        
        # set the value to the current row to previous row for the next iteration
        previous_row = int(row[1])


# remove the first value of the list 
change_list.pop(0)

# calculate the average changes in Profit/Losses from the change_list 
average_change = round(sum(change_list)/ len(change_list), 2)

# Print all the calculated values in the format specified
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_counter}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {great_in_date} (${great_in_profit})")
print(f"Greatest Decrease in Profits: {great_de_date} (${great_de_profit})")


# export the calculated values to a txt file in the format specified
with open(write_path, "w") as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {month_counter}")
    txtfile.write("\n")
    txtfile.write(f"Total: ${net_total}")
    txtfile.write("\n")
    txtfile.write(f"Average Change: ${average_change}")
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {great_in_date} (${great_in_profit})")
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {great_de_date} (${great_de_profit})")
    txtfile.write("\n")

    

