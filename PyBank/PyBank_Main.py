# Import Modules/Dependencies
import os
import csv


# Define Variables and Create Empty Lists to be Appended Later
Month_List = []
Profit_Loss_List = []
Monthly_Change = []


# Set Relative Path to CSV File
pybank_csv = os.path.join('..', 'Data_Files','pybank_budget_data.csv')

# Open & Read CSV File with Specified Delimiter
with open(pybank_csv, newline='', encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip Header Row when Reading CSV File
    csv_header = next(csvfile)

    # Read & Iterate Through Each Row of Data
    for row in csvreader:

        # Append Month_List to Include All Months in Given CSV File
        Month_List.append(row[0])

        # Append Profit_Loss_List to Include the Profit/Loss for All Months in Given CSV File
        Profit_Loss_List.append(int(row[1]))


# Set For Loop to Iterate Through Each Profit/Loss Value in Profit_Loss_List Except for Final Value
for i in range(len(Profit_Loss_List) -1):

    # Append Monthly_Change List to Include the Calculated Monthly Change for All Months
    Monthly_Change.append(Profit_Loss_List[i + 1] - Profit_Loss_List[i])


# Determine the Final Value for all Required Variables
Total_months = len(Month_List)

Net_total_amount = sum(Profit_Loss_List)

Average_change = round(sum(Monthly_Change) / len(Monthly_Change), 2)

Greatest_increase_in_profits = max(Monthly_Change)

Greatest_increase_month = (Monthly_Change.index(max(Monthly_Change)) + 1)

Greatest_decrease_in_profits = min(Monthly_Change)

Greatest_decrease_month = (Monthly_Change.index(min(Monthly_Change)) + 1)


# Print Financial Analysis Table in Terminal
print("Financial Analysis")
print("--------------------------------------------------")
print(f"Total Months: {Total_months}")
print(f"Total: {Net_total_amount}")
print(f"Average Change: ${Average_change}")
print(f"Greatest Increase in Profits: {Month_List[Greatest_increase_month]} (${Greatest_increase_in_profits})")
print(f"Greatest Decrease in Profits: {Month_List[Greatest_decrease_month]} (${Greatest_decrease_in_profits})")


# Set Relative Path to Output Text File
output_file = os.path.join("..", "Output_Files", "Financial_Analysis.text")

# Open and Write to Text File
with open(output_file, "w") as txtfile:

    # Write Financial Analysis Table in Text File
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------------------------------------\n")
    txtfile.write(f"Total Months: {Total_months}\n")
    txtfile.write(f"Total: {Net_total_amount}\n")
    txtfile.write(f"Average Change: ${Average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {Month_List[Greatest_increase_month]} (${Greatest_increase_in_profits})\n")
    txtfile.write(f"Greatest Decrease in Profits: {Month_List[Greatest_decrease_month]} (${Greatest_decrease_in_profits})")