import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

def download(url):
        ''' Downloads data into current working directory with name owid-covid-data.csv '''
        r = requests.get(url, allow_redirects=True)
        open('owid-covid-data.csv', 'wb').write(r.content)

def data():
        ''' Creates pandas DataFrame for columns location, date, total and new cases, and total and new deaths. '''
        data = pd.read_csv(
        os.getcwd()+'/owid-covid-data.csv', 
        usecols=['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths'],
        parse_dates=['date'],
        )
        data = data.set_index('date')
        data = data.sort_values('date', ascending=True)
        return data

def sub_data(countries, data):
        ''' Uses inputs countries list from user, creates sub DataFrames for desired countries. '''
        for country in countries:      
                country = data.loc[data['location']==country.capitalize()]
        print(countries.head())
        return countries

""" def make_plot(countries):
       

       #4 for loops, each for one of the plots
       
        pass """

""" def final():
        download(url)
        data(url)
        sub_data(countries)
        make_plot()
        pass """



url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
download(url)
data()
countries = input('What countries do you want to look at? Input them with a single space as separation. Ex. Brazil US Canada \n').split(' ')
sub_data(countries, data)