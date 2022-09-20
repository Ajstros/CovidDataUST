# CovidDataUST
Scrape and plot the COVID new case data at the University of St. Thomas.

The University of St. Thomas posts COVID case data at two links:
- [Historical](https://www.stthomas.edu/covid19/dashboard/historical/index.html)
- [Past 2 Weeks](https://www.stthomas.edu/covid19/dashboard/)

This program scrapes the data from those pages and graphs it over time.

# Dependencies
- requests
- bs4
- matplotlib
- pandas

These can be installed from the requirements.txt file in this repository:
```sh
pip install -r requirements.txt
```

# Usage
After copying the repository, run covid_data.py to graph all available data.

# Example
```sh
❯ py covid_data.py
https://www.stthomas.edu/covid19/dashboard/historical/index.html
                              Week Of  Total Positive Employee Positive  Student Positive Primary Campus  (Minneapolis) Primary Campus  (St. Paul)
0     Historical Apr. - Aug. 28, 2020              26               nan                26                           nan                        nan
1             Aug. 29 - Sept. 4, 2020              17                 1                16                             0                         17
2                  Sept. 5 - 11, 2020               9                 0                 9                             2                          7
3                 Sept. 12 - 18, 2020              36                 3                33                             2                         34
4                 Sept. 19 - 25, 2020              56                 0                56                             4                         52
..                                ...             ...               ...               ...                           ...                        ...
92        August 13 - August 19, 2022              17                14                 3                             4                         13
93        August 20 - August 26, 2022              22                13                 9                             2                         20
94      August 27 - September 2, 2022              28                18                10                             3                         25
95    September 3 - September 9, 2022              19                10                 9                             3                         16
96  September 10 - September 16, 2022              64                 8                56                            16                         48

[97 rows x 6 columns]

https://www.stthomas.edu/covid19/dashboard/
                             Week Of  Total Positive  Employee Positive  Student Positive  Minneapolis Campus  St. Paul Campus
0    September 3 - September 9, 2022              19                 10                 9                   3               16
1  September 10 - September 16, 2022              64                  8                56                  16               48
```

![Plot of COVID data from April 2020 to September 16, 2022](https://github.com/Ajstros/CovidDataUST/blob/main/example_plot.png)
