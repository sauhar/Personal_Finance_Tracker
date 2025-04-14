import pandas as pd
import csv
from datetime import datetime
from input_data import *

class CSV:
    def __init__(self):
        self.csv_file = 'my_finance_data.csv'
        self.COLUMNS=["date", "amount", "category", "description"]

    def initialize_csv(self):
        try:
            pd.read_csv(self.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.COLUMNS)    
            df.to_csv(self.csv_file, index=False)

    def input_data(self, date, amount, category, description):
        new_data = {
            'date':date,
            'amount': amount,
            'category': category,
            'description': description
        }
        ## with open will automatically close the file
        with open(self.csv_file,'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.COLUMNS)
            writer.writerow(new_data)
        print('Entry added successfully')


CSV().initialize_csv()
CSV().input_data("25-06-2025", "256.25", "income", "salary")
