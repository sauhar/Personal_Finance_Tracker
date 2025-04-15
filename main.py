import pandas as pd
import csv
from datetime import datetime
from input_data import *
import matplotlib.pyplot as plt


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
        # Ensure the file ends with a newline before appending
        with open(self.csv_file, "a+", newline="") as csvfile:  # a + Create it if it doesn’t exist
            csvfile.seek(0, 2)  # Go to end of file
            if csvfile.tell() > 0:  # gives the current file position in bytes
                # move 1 step back if the file is not empty
                csvfile.seek(csvfile.tell() - 1)
                if csvfile.read(1) != '\n':  # if the last character is not new line
                    csvfile.write('\n')  # Add a newline if not present

            writer = csv.DictWriter(
                csvfile,  # DictWriter converts our Python dictionary into a proper CSV row
                fieldnames=self.COLUMNS,
                quoting=csv.QUOTE_MINIMAL  # Only wrap values in quotes when needed
            )
            writer.writerow(new_data)
        print('Entry added successfully')

    def get_transactions(self, start_date, end_date):
        df = pd.read_csv(self.csv_file)
        # converting all the dates of date column into a datetime object so that we can filter them as per transaction
        df["date"] = pd.to_datetime(df["date"], format=date_format)
        start_date = datetime.strptime(start_date, date_format)
        end_date = datetime.strptime(end_date, date_format)

        mask_filter = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask_filter]

        if filtered_df.empty:
            print("Transactions not found in the given date range")
        else:
            print(
                f"Transactions from {start_date.strftime(date_format)} to {end_date.strftime(date_format)}"
            )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(date_format)}
                )
            )

            total_income = filtered_df[filtered_df["category"]
                                       == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"]
                                        == "Expense"]["amount"].sum()
            print("\nSummary:")
            # .2f do 2 decimal place function
            print(f"Total Income:${total_income:.2f}")
            print(f"Total Expense:${total_expense:.2f}")
            print(f"Net Savings:${(total_income - total_expense):.2f}")

        return filtered_df


def add():
    CSV().initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    # input_data is an instance method of the CSV class, not a static method so we need . so we need to give give it self agrument
    CSV().input_data(date, amount, category, description)


def plot_transactions(df):
    df.set_index('date', inplace=True)

    income_df = (df[df["category"] == "Income"]
                 .resample("D")                  # D means daily frequency of date
                 .sum().reindex( df.index, fill_value=0)
        )
    
    
    expense_df = (df[df["category"] == "Expense"]
                .resample("D")
                .sum()
                .reindex(df.index, fill_value=0)
    )
    
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()



def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV().get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n) ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
