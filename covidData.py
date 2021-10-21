#! python3
# covidData.py - downloads latest covid data from stthomas dashboard

import requests, bs4, os, math
import matplotlib.pyplot as plt
import pandas as pd


def plot_total_cases(df):
    dates = df['Week Of']
    total_cases = df['Total Positive']

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


def get_data(url='https://www.stthomas.edu/covid19/dashboard/historical/index.html'):
    """Return a DataFrame of the data at the URL."""

    # Get webpage, make soup
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='html.parser')

    table_elem = soup.find('table')
    tbody_elem = table_elem.find('tbody')
    row_elems = tbody_elem.find_all('tr')
    # Get table headers. Strip whitespace, capitalize each first letter
    headers = [x.text.strip().title() for x in table_elem.find('thead').find_all('th')]
    # Get table data
    data = []
    for row in row_elems:
        d = [x.text for x in row.find_all(['th', 'td'])]
        # Get 'week of' column and keep as a string
        d[0] = d[0].strip()
        # All other data should be integers
        for i in range(1, len(d)):
            item = d[i]
            if not item.isdigit():
                no_asterisk = item.replace('*', '')
                if no_asterisk.isdigit():
                    d[i] = int(no_asterisk)
                else:
                    d[i] = 'nan'
            else:
                d[i] = int(item)
        data.append(d)
    return pd.DataFrame(data=data, columns=headers)
    

if __name__ == '__main__':
    # TODO: set up a function to put all data together into one graph (easier with pandas)
    # TODO: set up a function to graph both sets of data as subplots of the same matplotlib figure
    urls = [
        'https://www.stthomas.edu/covid19/dashboard/historical/index.html',
        'https://www.stthomas.edu/covid19/dashboard/',
    ]
    for url in urls:
        df = get_data(url)
        print(url)
        print(df)
        print()
        plot_total_cases(df)
