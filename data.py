import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

def download(url):
        ''' Downloads data into current working directory with name owid-covid-data.csv '''
        r = requests.get(url, allow_redirects=True)
        open('owid-covid-data.csv', 'wb').write(r.content)

def dat():
        ''' Creates pandas DataFrame for columns location, date, total and new cases, and total and new deaths. '''
        data = pd.read_csv(
        os.getcwd()+'/owid-covid-data.csv', 
        usecols=['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths'],
        parse_dates=['date'],
        )
        data = data.set_index('date')
        data = data.sort_values('date', ascending=True)
        return data

def changes(countries):
        ''' Makes sure input is written as it is on data. '''
        for i in range(len(countries)):
                if countries[i] == 'UK':
                        countries[i] = 'United Kingdom'
                elif countries[i] == 'US' or countries[i] == 'United States of America':
                        countries[i] = 'United States'
        return countries

def make_plot(countries, data): 
        plt.figure(figsize=(12, 6))
        
        plt.subplot(2,2,1)
        for country in countries:
                plt.plot(data.loc[data['location']==country.title()]['total_cases'])
        plt.legend(countries)
        #plt.text()
        plt.title('Total cases of COVID-19')
        plt.xlabel('Date')
        plt.ylabel('Total Cases (millions)')

        plt.subplot(2,2,2)
        for country in countries:
                plt.plot(data.loc[data['location']==country.title()]['total_deaths'])
        plt.legend(countries)
        plt.title('Total deaths by COVID-19')
        plt.xlabel('Date')
        plt.ylabel('Total Deaths')

        plt.subplot(2,2,3)
        for country in countries:
                plt.plot(data.loc[data['location']==country.title()]['new_cases'])
        plt.legend(countries)
        plt.title('New Cases of COVID-19')
        plt.xlabel('Date')
        plt.ylabel('New Cases')

        plt.subplot(2,2,4)
        for country in countries:
                plt.plot(data.loc[data['location']==country.title()]['new_deaths'])
        plt.legend(countries)
        plt.title('New Deaths by COVID-19')
        plt.xlabel('Date')
        plt.ylabel('New Deaths')

        plt.tight_layout()
        plt.show()

download('https://covid.ourworldindata.org/data/owid-covid-data.csv')
data = dat()
countries = input('What countries do you want to look at? Separate them with a comma. Ex: Brazil, United States, Canada \n Input: ').split(', ')
countries = changes(countries)
make_plot(countries, data)