import pandas as pd
import csv
from datetime import datetime
from input_data import *


class CSV:
    def __init__(self):
        self.csv_file = 'my_finance_data.csv'
        self.COLUMNS = ["date", "amount", "category", "description"]

    def initialize_csv(self):
        try:
            pd.read_csv(self.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.COLUMNS)
            df.to_csv(self.csv_file, index=False)

    def input_data(self, date, amount, category, description):
        new_data = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        # with open will automatically close the file
        with open(self.csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.COLUMNS)  ## DictWriter object is created to allow you to write dictionaries into a CSV file.
            writer.writerow(new_data)
        print('Entry added successfully')

def get_transactions(self,start_date, end_date):
    df = pd.read_csv(self.csv_file)
    ## converting all the dates of date column into a datetime object so that we can filter them as per transaction
    df["date"] = pd.to_datetime(df["date"],format=date_format)
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)
    
    mask = (df["date"]>=start_date) & (df["date"]<=end_date)
    filtered_df = df.loc(mask)




def add():
    CSV().initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV().input_data(date, amount, category, description)  ## input_data is an instance method of the CSV class, not a static method so we need . so we need to give give it self agrument

add()