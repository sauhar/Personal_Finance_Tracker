from datetime import datetime

date_format = "%d-%m-%y"
CATEGORIES = {"I": "Income", "E":"Expense"}  ## create dictionary

def get_date(prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format) ## strftime converts a datetime object into a formatted string
    try:
        valid_date = datetime.strptime(date_str,date_format) ## strptime converts a string into a datetime object, using a format you specify
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    amount = float(input("Enter the amount: "))
    try:
        if amount <=0:
            print("Amount must be a non-negative and non-zero value.")
        return amount
    except:
        print("Invalid amoun Type")
        return get_amount()


def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    try:
        if category in CATEGORIES:
            return CATEGORIES[category]
    except:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
        return get_category()

def get_description():
    return input("Enter a description (optional): ")