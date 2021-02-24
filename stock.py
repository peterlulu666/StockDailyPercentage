import yfinance
import csv
import os

prev_start_date = "2021-02-22"
prev_start_end_date = "2021-02-23"
start_date = "2021-02-23"
end_date = "2021-02-24"
with open('stock_list.csv', newline='') as f_stock_list:
    reader_stock_list = csv.reader(f_stock_list)
    stock_name_list = list(reader_stock_list)

csv_fields = ["Stock name", "Percentage change"]
csv_rows = []


def stock_percentage(prev_start_date, prev_start_end_date, start_date, end_date, stock_name):
    yfinance.download(stock_name, start=prev_start_date, end=prev_start_end_date).to_csv("prev" + stock_name + ".csv")
    yfinance.download(stock_name, start=start_date, end=end_date).to_csv(stock_name + ".csv")
    with open("prev" + stock_name + ".csv", newline='') as f:
        reader = csv.reader(f)
        prev_data = list(reader)

    with open(stock_name + ".csv", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    percentage_change = (float(data[1][4]) - float(prev_data[1][4])) / float(prev_data[1][4])
    # Number percentage and decimal in Python
    csv_rows.append([stock_name, str("{0:0.2f}%".format(percentage_change * 100))])
    os.remove("prev" + stock_name + ".csv")
    os.remove(stock_name + ".csv")


def main():
    for stock_name in stock_name_list:
        stock_percentage(prev_start_date, prev_start_end_date, start_date, end_date, str(stock_name[0]))

    with open("Stock.csv", 'w') as csv_file:
        # creating a csv writer object
        csv_writer = csv.writer(csv_file)

        # writing the fields
        csv_writer.writerow(csv_fields)

        # writing the data rows
        csv_writer.writerows(csv_rows)


main()
