data_lines = []  # List to hold data lines from the file
dates = []       # List to store numeric dates
answers = []     # List to store corresponding Wordle words

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",  # Month abbreviations
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Function to convert month/day/year into a numeric date (yyyymmdd)
def to_number(mon, dy, yr):
    num = int(yr) * 10000
    num += (months.index(mon) + 1) * 100
    num += int(dy)
    return num

# Function to search for a date by word
def search_word(word):
    word = word.upper()
    if word in answers:
        index = answers.index(word)
        return dates[index]
    else:
        return 0

# Function to search for a word by date
def search_date(mon, dy, yr):
    target = to_number(mon, dy, yr)
    if target in dates:
        return answers[dates.index(target)]
    else:
        return None

# Try to read the data file
file_loaded = True

try:
    with open("/workspaces/ICS3U_S2/ICS3U/Data/wordle.dat", "r") as file:
        for line in file:
            data_lines.append(line.strip().split())
except OSError as e:
    print("There was a problem opening the file:", e)
    file_loaded = False

# If the file loaded, continue with processing
if file_loaded:

    # Fill the dates and answers lists from the data
    for entry in data_lines:
        dates.append(to_number(entry[0], entry[1], entry[2]))
        answers.append(entry[3])

    print("Welcome to the Wordle Finder!")
    option = input("Enter 'w' to search by word or 'd' to search by date: ").lower()

    if option == "w":
        user_word = input("Enter a word to look up: ")
        found = search_word(user_word)
        if found > 0:
            print("The word", user_word.upper(), "was used on", found)
        else:
            print(user_word.upper(), "was not found.")

    elif option == "d":
        y = input("Enter the year: ")
        m = input("Enter the month (e.g. Jan): ").capitalize()
        d = input("Enter the day: ")

        input_date = to_number(m, d, y)

        if input_date < 20210619:
            print(input_date, "is before the first Wordle. Try a later date.")
        elif input_date > 20240421:
            print(input_date, "is too recent. The data ends at 20240421.")
        else:
            result = search_date(m, d, y)
            if result != None:
                print("The word on", input_date, "was", result)
            else:
                print("No word found for", input_date)

    else:
        print("Invalid option. Please enter 'w' or 'd'.")
