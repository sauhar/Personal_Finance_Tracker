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
        with open(self.csv_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.COLUMNS)
            writer.writerow(new_data)
        print('Entry added successfully')


def add():
    csv_instance = CSV()
    csv_instance.initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    csv_instance.input_data(date, amount, category, description)

add()