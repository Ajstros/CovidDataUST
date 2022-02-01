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