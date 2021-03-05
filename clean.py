# Name: Maria Daan
# Student number: 11243406
"""
Exploratory Data Analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import awoc

INPUT_CSV = "survey_results_public_mega_inc.csv"
COUNTRY = "Country"
GENDER = "Gender"
FORMALED = "FormalEducation"
YEARSCODINGPROF = "YearsCodingProf"
YEARSCODING = "YearsCoding"
EMPLOYMENT = "Employment"
DEVTYPE = "DevType"
GDP = "ConvertedSalary"

my_world = awoc.AWOC()
countries_of_europe = my_world.get_countries_list_of('Europe')

def load_data(input):
    """
    Loads data into a pandas DataFrame
    """
    df = pd.read_csv(input)
    df = df.replace('NA', np.nan)
    return df


def to_float(DataFrame, column):
    """
    Converts data in column to float values
    """
    df = DataFrame
    first = df[column].iloc[0]

    # Use first value in column to detect stringtype and modify if necessary
    if ',' in first:
        df[column] = df[column].str.replace(',', '.')
    elif 'dollars' in first:
        df[GDP] = df[GDP].str.strip('dollars')
    df[column] = df[column].astype(float)

    return df


def central_tendency(DataFrame, column):
    """
    Computes and prints the Central Tendency of a column
    """
    print(f'{column}\n'
          f'count: {DataFrame[column].count()}\n'
          f'max: {DataFrame[column].max()}\n'
          f'min: {DataFrame[column].min()}\n'
          f'mean: {round(DataFrame[column].mean(), 2)}\n'
          f'median: {DataFrame[column].median()}\n'
          f'mode: {DataFrame[column].mode()}\n')


def five_number(DataFrame, column):
    """
    Computes and prints the Five Number Summary of a column
    - Minimum, First Quartile, Median, Third Quartile and Maximum.
    """
    values = DataFrame[column].describe()[['min', '25%', '50%', '75%', 'max']]
    print(f'{column}\n{values}')


def print_info(DataFrame, devtype, ex_level, ed_level):
    employee = DataFrame.loc[df[YEARSCODINGPROF].isin(ex_level)]
    employee = employee.loc[df['DevType'] == devtype]
    employee = employee.loc[df['Employment'] == 'Employed full-time']
    employee = employee.loc[df[FORMALED].isin(ed_level)]
    print('amount of employees:         ' + str(employee.shape[0]))
    print('mean income employee:        ' + str(round(employee[GDP].mean(), 2)))
    return employee

def print_freq(DataFrame, column):
    frequency_df = DataFrame[column].value_counts()
    print(frequency_df, "\n")

def print_salary(DataFrame, Gender):
    if Gender == 'other':
        employee = DataFrame.loc[DataFrame['Gender'] != 'Male']
        employee = employee.loc[DataFrame['Gender'] != 'Female']
    elif Gender == 'all':
        employee = DataFrame
    else:
        employee = DataFrame.loc[DataFrame['Gender'] == Gender]
    print('mean income ' + str(Gender) + ' employee:   ' + str(round(employee[GDP].mean(), 2)))

if __name__ == '__main__':
    # Load data into a pandas DataFrame
    df = load_data(INPUT_CSV)

    # Select data from DataFrame
    df = df[[COUNTRY, GENDER, FORMALED, GDP, YEARSCODINGPROF, YEARSCODING, EMPLOYMENT, DEVTYPE]]

    # Strip data where necessary
    df[FORMALED] = df[FORMALED].str.strip()
    df[GENDER] = df[GENDER].str.strip()

    # Print descriptive statistics
    central_tendency(df, GDP)
    five_number(df, GDP)

    print_freq(df, GENDER)
    print_freq(df, FORMALED)

    alled = [ 'I never completed any formal education', 'Primary/elementary school', 'Some college/university study without earning a degree', 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)', 'Bachelor’s degree (BA, BS, B.Eng., etc.)','Master’s degree (MA, MS, M.Eng., MBA, etc.)', 'Associate degree', 'Professional degree (JD, MD, etc.)', 'Other doctoral degree (Ph.D, Ed.D., etc.)',]
    lowed = [ 'I never completed any formal education', 'Primary/elementary school', 'Some college/university study without earning a degree', 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)']
    highed = ['Bachelor’s degree (BA, BS, B.Eng., etc.)','Master’s degree (MA, MS, M.Eng., MBA, etc.)', 'Associate degree', 'Professional degree (JD, MD, etc.)', 'Other doctoral degree (Ph.D, Ed.D., etc.)']

    allex = ['0-2 years', '3-5 years', '6-8 years', '9-11 years', '12-14 years', '15-17 years', '18-20 years', '21-23 years', '24-26 years', '27-29 years', '30 or more years']
    littlex = ['0-2 years', '3-5 years']
    lotofex = ['6-8 years', '9-11 years', '12-14 years', '15-17 years', '18-20 years', '21-23 years', '24-26 years', '27-29 years', '30 or more years']

    # All
    print_salary(df, 'all')
    print_salary(df, 'Male')
    print_salary(df, 'Female')
    print_salary(df, 'other')

    # Self-taught, little professional experience, low educated
    print('Self-taught, little professional experience, low educated:')
    self_taught = print_info(df, 'Full-stack developer', littlex, lowed)
    print_salary(self_taught, 'Male')
    print_salary(self_taught, 'Female')
    print_salary(self_taught, 'other')
    print('\n')

    # System-taught, little professional experience, high educated
    print('System-taught, little professional experience, high educated')
    system_taught = print_info(df, 'Full-stack developer', littlex, highed)
    print_salary(system_taught, 'Male')
    print_salary(system_taught, 'Female')
    print_salary(system_taught, 'other')
    print('\n')

    all_emp = print_info(df, 'Full-stack developer', littlex, alled)
    all_EU = all_emp.loc[df['Country'].isin(countries_of_europe)]
    all_US = all_emp.loc[df['Country'] == 'United States']

    print('\n')
    print('All EU Full-stack developers, little experienced:')
    print_salary(all_EU, 'all')
    print_salary(all_EU, 'Male')
    print_salary(all_EU, 'Female')
    print_salary(all_EU, 'other')
    print('\n')

    print('All US Full-stack developers, little experienced:')
    print_salary(all_US, 'all')
    print_salary(all_US, 'Male')
    print_salary(all_US, 'Female')
    print_salary(all_US, 'other')
    print('\n')

    system_taught_EU = system_taught.loc[df['Country'].isin(countries_of_europe)]
    system_taught_US = system_taught.loc[df['Country'] == 'United States']
    self_taught_EU = self_taught.loc[df['Country'].isin(countries_of_europe)]
    self_taught_US = self_taught.loc[df['Country'] == 'United States']

    # System-taught, little professional experience, high educated
    print('System-taught US:')
    system_taught = print_info(system_taught_US, 'Full-stack developer', littlex, highed)
    print_salary(system_taught, 'Male')
    print_salary(system_taught, 'Female')
    print_salary(system_taught, 'other')
    print('\n')

    # System-taught, little professional experience, high educated
    print('System-taught EU:')
    system_taught = print_info(system_taught_EU, 'Full-stack developer', littlex, highed)
    print_salary(system_taught, 'Male')
    print_salary(system_taught, 'Female')
    print_salary(system_taught, 'other')
    print('\n')

     # Self-taught, little professional experience, low educated
    print('Self-taught US:')
    self_taught = print_info(self_taught_US, 'Full-stack developer', littlex, lowed)
    print_salary(self_taught, 'Male')
    print_salary(self_taught, 'Female')
    print_salary(self_taught, 'other')
    print('\n')

     # Self-taught, little professional experience, low educated
    print('Self-taught EU:')
    self_taught = print_info(self_taught_EU, 'Full-stack developer', littlex, lowed)
    print_salary(self_taught, 'Male')
    print_salary(self_taught, 'Female')
    print_salary(self_taught, 'other')
    print('\n')


    # Create GDP list and remove missing/outlying value(s)
    GDP_list = []
    GDP_list = df[GDP].tolist()
    GDP_cleanlist = [x for x in GDP_list if str(x) != 'nan']
    GDP_cleanlist.remove(max(GDP_cleanlist))

    # Plot a histogram of the GDPs
    plt.hist(GDP_cleanlist, 20)
    plt.xlabel(GDP)
    plt.ylabel('Employees')
    plt.show()
