"""
  Author : Abdullah Parvez
  Student Number : 790809
  Revison date : 2 March 2025
  Program : Even or Odd
  Description : A program that determines whether the product of number is even or odd
VARIABLE DICTIONARY
 # data_lines   : List that holds each line of file data (split into parts)
# dates        : List that holds the converted numeric dates (format: yyyymmdd)
# answers      : List that holds the corresponding Wordle words
# months       : List of month abbreviations used for converting text to numbers
# num          : Numeric representation of a date (used in to_number function)
# word         : The word the user is searching for (used in search_word)
#= mon, dy, yr  : Month, day, and year input by the user (used in search_date)
# target       : Numeric version of the user's input date (used in search_date)
# file_loaded  : Boolean flag to check if file opened successfully
# file         : File object used to read "wordle.dat"
 line         : Current line being read from the file
 entry        : One row from data_lines being processed (contains date + word)
 option       : User’s menu selection – 'w' for word search, 'd' for date search
 user_word    : Word entered by the user when searching by word
 found        : Numeric date found for a word (from search_word)
 input_date  : Numeric version of a user-entered date (for validation)
 result       : Word found for a given date (from search_date)
---------------------------------------------------------

"""



# List to hold lines read from the file
data_lines = []

# Lists to hold dates (as numbers) and corresponding Wordle answers
dates = []
answers = []

# List of month abbreviations for conversion
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Function to convert month, day, and year into a numeric date in yyyymmdd format
def to_number(mon, dy, yr):
    num = int(yr) * 10000                     # Multiply year by 10,000
    num += (months.index(mon) + 1) * 100      # Find month index and multiply by 100
    num += int(dy)                            # Add the day
    return num

# Function to search for a date by the given Wordle word
def search_word(word):
    word = word.upper()  # Convert input to uppercase for consistent comparison
    if word in answers:  # If the word exists in the answers list
        index = answers.index(word)  # Get the index of the word
        return dates[index]          # Return the corresponding date
    else:
        return 0  # Return 0 if the word is not found

# Function to search for a Wordle word by date
def search_date(mon, dy, yr):
    target = to_number(mon, dy, yr)  # Convert input to numeric date
    if target in dates:              # If the date exists in the list
        return answers[dates.index(target)]  # Return the corresponding word
    else:
        return None  # Return None if the date is not found

# Attempt to open and read the data file
file_loaded = True  # Flag to check if the file was loaded successfully

try:
    file = open("wordle.dat", "r")       # Open file in read mode
    line = file.readline().strip()       # Read and clean the first line
    while line != "":                    # Loop until no more lines
        data_lines.append(line.split())  # Split line into parts and store in list
        line = file.readline().strip()   # Read the next line
    file.close()                         # Close the file
except OSError:
    print("Could not open the file.")  # Display error message
    file_loaded = False  # Mark the file as not loaded

# If the file was loaded successfully, continue the program
if file_loaded:

    # Process the data: fill dates and answers lists
    for entry in data_lines:
        dates.append(to_number(entry[0], entry[1], entry[2]))  # Convert date to number
        answers.append(entry[3])  # Store the answer word

    # Greet the user and ask how they want to search
    print("Welcome to the Wordle Finder!")
    option = input("Enter 'w' to search by word or 'd' to search by date: ").lower()
