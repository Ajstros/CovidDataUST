#! python3
# covidData.py - downloads latest covid data from stthomas dashboard

import requests, bs4, os, math
import matplotlib.pyplot as plt

def print_table(table):
    width_of_terminal = os.get_terminal_size()[0]
    number_of_columns = len(table[0])
    column_width = math.floor(width_of_terminal/number_of_columns) - 1
    print()
    print('=' * width_of_terminal)
    for row in table:
        for item in row:
            if len(item) > column_width:
                item = item[:column_width - 3] + '...'
            print(item.ljust(column_width), end='|')
        print()
    print('=' * width_of_terminal)
    print()

def plot_data(table):
    dates = [row[0] for row in table[1:]]
    total_cases = [int(row[1]) for row in table[1:]]

    fig, ax = plt.subplots()
    ax.set_position([0.1, 0.2, 0.8, 0.7])

    plt.plot(dates, total_cases)
    # plt.ylim(0, max(total_cases))
    plt.title("Total New Covid Cases at St. Thomas")
    plt.xlabel("Date")
    plt.ylabel("Total New Cases")
    for label in ax.get_xticklabels(): # Rotates x labels
        label.set_rotation(40)
        label.set_horizontalalignment('right')
    plt.grid(True)
    plt.show()

# Get webpage, make soup
url = 'https://www.stthomas.edu/covid19/dashboard/historical/index.html'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features='html.parser')

table = [[]]
current_row = 0
string_count = 0
for i in soup.find('table').stripped_strings:
    table[current_row].append(i.replace('*', ''))
    string_count += 1
    if string_count == 6:
        table.append([])
        current_row += 1
        string_count = 0
table.pop()

print_table(table)
if input("Enter q to quit, enter any other key to continue to graph: ").lower() != 'q':
    plot_data(table)
