import covid_data

urls = [
    'https://www.stthomas.edu/covid19/dashboard/historical/index.html',
    'https://www.stthomas.edu/covid19/dashboard/',
]
dfs = []
for url in urls:
    df = covidData.get_data(url)
    dfs.append(df)
    print(url)
    print(df)
    print()
    covidData.plot_total_cases(df)
covidData.plot_total_cases(dfs[0], dfs[1])
covidData.plot_total_cases_subplots(dfs[0], dfs[1])
