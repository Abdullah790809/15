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
