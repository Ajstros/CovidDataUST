"""Scrape and plot the COVID new case data at the University of St. Thomas.

October 2021
Abe Stroschein, ajstroschein@stthomas.edu
"""

import requests, bs4
import matplotlib.pyplot as plt
import pandas as pd


def plot_total_cases(*argv):
    """Plot the total new cases vs. weeks on the same plot.

    Arguments
    ---------
    *argv : pandas.DataFrame
        Any number of DataFrames with "Total Positive" and "Week Of" columns to graph.
    """

    fig, ax = plt.subplots()
    ax.set_position([0.1, 0.2, 0.8, 0.7])

    for df in argv:
        dates = df["Week Of"]
        total_cases = df["Total Positive"]

        plt.plot(dates, total_cases)
        # plt.ylim(0, max(total_cases))
        plt.title("Total New Covid Cases at St. Thomas")
        plt.xlabel("Date")
        plt.ylabel("Total New Cases")
        for label in ax.get_xticklabels():  # Rotates x labels
            label.set_rotation(40)
            label.set_horizontalalignment("right")
        plt.grid(True)
    plt.show()


def plot_total_cases_subplots(*argv):
    """Plot the total new cases vs. weeks on the separate subplots.

    Arguments
    ---------
    *argv : pandas.DataFrame
        Any number of DataFrames with "Total Positive" and "Week Of" columns to graph.
    """

    fig, axes = plt.subplots(nrows=1, ncols=len(argv))
    print(axes)

    for i in range(len(argv)):
        df = argv[i]
        dates = df["Week Of"]
        total_cases = df["Total Positive"]
        ax = axes[i]

        left = 0.1
        width = 0.8
        height = 0.3
        bottom = 0.175 + (height + 0.175) * i
        ax.set_position([left, bottom, width, height])
        plt.sca(ax)
        plt.plot(dates, total_cases)
        plt.ylim(0)
        plt.title("Total New Covid Cases at St. Thomas")
        plt.xlabel("Date")
        plt.ylabel("Total New Cases")
        for label in ax.get_xticklabels():  # Rotates x labels
            label.set_rotation(40)
            label.set_horizontalalignment("right")
        plt.grid(True)
    plt.show()


def get_data(url="https://www.stthomas.edu/covid19/dashboard/historical/index.html"):
    """Return a DataFrame of the data at the URL."""

    # Get webpage, make soup
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    table_elem = soup.find("table")
    tbody_elem = table_elem.find("tbody")
    row_elems = tbody_elem.find_all("tr")
    # Get table headers. Strip whitespace, capitalize each first letter
    headers = [x.text.strip().title() for x in table_elem.find("thead").find_all("th")]
    # Get table data
    data = []
    for row in row_elems:
        d = [x.text for x in row.find_all(["th", "td"])]
        # Get 'week of' column and keep as a string
        d[0] = d[0].strip()
        # All other data should be integers
        for i in range(1, len(d)):
            item = d[i]
            if not item.isdigit():
                no_asterisk = item.replace("*", "")
                if no_asterisk.isdigit():
                    d[i] = int(no_asterisk)
                else:
                    d[i] = "nan"
            else:
                d[i] = int(item)
        data.append(d)
    return pd.DataFrame(data=data, columns=headers)


if __name__ == "__main__":
    # TODO: add command line flags
    urls = [
        "https://www.stthomas.edu/covid19/dashboard/historical/index.html",
        "https://www.stthomas.edu/covid19/dashboard/",
    ]
    dfs = []
    for url in urls:
        df = get_data(url)
        dfs.append(df)
        print(url)
        print(df)
        print()
    plot_total_cases_subplots(dfs[0], dfs[1])
