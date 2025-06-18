"""
 Author : Abdullah Parvez
  Student Number : 790809
  Revison date : 17 june 2025
  Program : Credit Card Report
  Description :The output of this program will be the expired or soon-to-be-expired credit cards, giving the subscriber's:
name,
credit card type,
credit card number, and
expiry date, in order of date from past to future.

Dictonary

last_names      : List that stores all customers last names
cc_types        : List that stores credit card types Visa or MasterCard
cc_numbers      : List that stores the credit card numbers as strings
exp_months      : List that stores the expiry month as integers
exp_years       : List that stores the expiry year as integers
exp_dates       : List that stores expiry dates in yyyymm format 
cutoff_date     : The last valid date June 2025 used to check if cards are expired
file            : The file object used to open and read data.dat
line            : One line from the file being read
parts           : A list that holds the parts of each line split by commas
expired_indexes : List of indexes for credit cards that are expired or need renewal
i, j            : Loop counters used when finding expired cards and sorting them
full_name       : The customers full name irst + last
card_type       : The type of credit card Visa or MasterCard
card_num        : The credit card number with a # added at the front
date_num        : Expiry date in yyyymm format, used to compare against cutoff_date
month_str       : Month as a two-digit string
date_str        : Final expiry date as a string used when printing
status          : Shows if the card is EXPIRED or “RENEW IMMEDIATELY”
"""






# Arrays to store data
first_names = []     # Stores first names
last_names = []      # Stores last names
cc_types = []        # Stores credit card types (e.g., Visa, MasterCard)
cc_numbers = []      # Stores credit card numbers
exp_months = []      # Stores expiry months
exp_years = []       # Stores expiry years
exp_dates = []       # Stores combined expiry dates in YYYYMM format

cutoff_date = 202506  # June 2025 as YYYYMM

try:
    file = open("data.dat", "r")              # Open the file for reading
    line = file.readline().strip()            # Read the first line

    while line != "":                         # Keep reading until the file ends
        parts = line.split(",")               # Split each line by commas
        first_names.append(parts[0])          # Add first name
        last_names.append(parts[1])           # Add last name
        cc_types.append(parts[2])             # Add credit card type
        cc_numbers.append(parts[3])           # Add credit card number
        exp_months.append(int(parts[4]))      # Add expiry month as integer
        exp_years.append(int(parts[5]))       # Add expiry year as integer
        exp_dates.append(int(parts[5]) * 100 + int(parts[4]))  # Convert to YYYYMM
        line = file.readline().strip()        # Read the next line

    file.close()                              # Close the file

except OSError:
    print("Could not open the file.")         # Error message if file can't be opened

# Find all cards that are expired or need renewal
expired_indexes = []

for i in range(len(exp_dates)):
    if exp_dates[i] <= cutoff_date:           # If the expiry is before or equal to June 2025
        expired_indexes.append(i)             # Save that index

# Sort those cards by expiry date using exchange sort
for i in range(len(expired_indexes) - 1):
    for j in range(i + 1, len(expired_indexes)):
        if exp_dates[expired_indexes[j]] < exp_dates[expired_indexes[i]]:
            expired_indexes[i], expired_indexes[j] = expired_indexes[j], expired_indexes[i]  # Swap

# Print the report to the screen
print("Credit Cards that are expired or need renewal:\n")

for i in expired_indexes:
    full_name = first_names[i] + " " + last_names[i]              # Combine first and last name
    card_type = cc_types[i]                                       # Credit card type
    card_num = "#" + cc_numbers[i]                                # Add # before credit card number
    date_num = exp_years[i] * 100 + exp_months[i]                 # Expiry date as YYYYMM
    status = "EXPIRED" if date_num < cutoff_date else "RENEW IMMEDIATELY"  # Status check

    if exp_months[i] < 10:
        month_str = "0" + str(exp_months[i])                      # Add leading 0 if needed
    else:
        month_str = str(exp_months[i])

    date_str = str(exp_years[i]) + month_str                      # Build date as string

    print(full_name + ": " + card_type.ljust(12) + " " + card_num + " " + date_str + " " + status) #print the output
