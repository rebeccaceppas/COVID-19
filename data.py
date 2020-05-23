from matplotlib import pyplot
import pandas as pd
import OpenBlender
import json

url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

data = pd.read_csv(
        '/Users/rebeccaceppas/code/COVID-19/owid-covid-data.csv', 
        usecols=['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths'],
        parse_dates=['date'],
        )

data = data.set_index('date')
data = data.sort_values('date', ascending=True)

#Country specific data
Brazil = data.loc[data['location']=='Brazil']
Canada = data.loc[data['location']=='Canada']
US = data.loc[data['location']=='United States']


#creating plot object
pyplot.figure(figsize=(12, 6))

#creating each subplot
pyplot.subplot(2,2,1)
pyplot.plot(Brazil['total_cases'])
pyplot.plot(Canada['total_cases'])
pyplot.plot(US['total_cases'])
pyplot.legend(['Brazil', 'Canada', 'United States'])
pyplot.title('Total cases of COVID-19')
pyplot.xlabel('Date')
pyplot.ylabel('Total Cases (millions)')

pyplot.subplot(2,2,2)
pyplot.plot(Brazil['total_deaths'])
pyplot.plot(Canada['total_deaths'])
pyplot.plot(US['total_deaths'])
pyplot.legend(['Brazil', 'Canada', 'United States'])
pyplot.title('Total deaths by COVID-19')
pyplot.xlabel('Date')
pyplot.ylabel('Total Deaths')

pyplot.subplot(2,2,3)
pyplot.plot(Brazil['new_cases'])
pyplot.plot(Canada['new_cases'])
pyplot.plot(US['new_cases'])
pyplot.legend(['Brazil', 'Canada', 'United States'])
pyplot.title('New Cases of COVID-19')
pyplot.xlabel('Date')
pyplot.ylabel('New Cases')

pyplot.subplot(2, 2, 4)  # rows, columns, panel selected
pyplot.plot(Brazil['new_deaths'])
pyplot.plot(Canada['new_deaths'])
pyplot.plot(US['new_deaths'])
pyplot.legend(['Brazil', 'Canada', 'United States'])
pyplot.title('New Deaths by COVID-19')
pyplot.xlabel('Date')
pyplot.ylabel('New Deaths')

pyplot.tight_layout()
pyplot.show()