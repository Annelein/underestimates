# Name: Maria Daan
# Student number: 11243406
"""
Exploratory Data Analysis
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json


INPUT_CSV = "survey_results_public_mega_inc.csv"
GENDER = "Gender"
FORMALED = "FormalEducation"
YEARSCODINGPROF = "YearsCodingProf"
YEARSCODING = "YearsCoding"
EMPLOYMENT = "Employment"
DEVTYPE = "DevType"
GDP = "ConvertedSalary"


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
    print('\n')
    print('Type: ')
    print(devtype)
    print(ex_level)
    print(ed_level)
    employee = DataFrame.loc[df['YearsCodingProf'].isin(ex_level)]
    employee = employee.loc[df['DevType'] == devtype]
    employee = employee.loc[df['Employment'] == 'Employed full-time']
    employee = employee.loc[df[FORMALED].isin(ed_level)]
    print('amount of employees:         ' + str(employee.shape[0]))
    print('mean income employee:        ' + str(round(employee[GDP].mean(), 2)))

    maleemployee = employee.loc[df['Gender'] == 'Male']
    femaleemployee = employee.loc[df['Gender'] != 'Male']
    print('mean income male employee:   ' + str(round(maleemployee[GDP].mean(), 2)))
    print('mean income female employee: ' + str(round(femaleemployee[GDP].mean(), 2)))
    print('\n')
    return employee

def print_freq(DataFrame, column):
    frequency_df = DataFrame[column].value_counts()
    print(frequency_df, "\n")

def print_salary(DataFrame, Gender):
    employee = DataFrame.loc[DataFrame['Gender'] == Gender]

    print('mean income ' + str(Gender) + ' employee:   ' + str(round(employee[GDP].mean(), 2)))
    # print('mean income female employee: ' + str(round(femaleemployee[GDP].mean(), 2)))
    # print('mean income other employee:   ' + str(round(otheremployee[GDP].mean(), 2)))

if __name__ == '__main__':
    # Load data into a pandas DataFrame
    df = load_data(INPUT_CSV)

    # Select data from DataFrame
    df = df[[GENDER, FORMALED, GDP, YEARSCODINGPROF, YEARSCODING, EMPLOYMENT, DEVTYPE]]

    # Strip data where necessary
    df[FORMALED] = df[FORMALED].str.strip()
    df[GENDER] = df[GENDER].str.strip()

    # Convert relevant columns to floats
    # df = to_float(df, GDP)
    # df = to_float(df, INFANT)
    # df = to_float(df, DENSITY)

    # Print descriptive statistics
    # central_tendency(df, GDP)
    # five_number(df, INFANT)

    print_freq(df, GENDER)
    print_freq(df, FORMALED)

    alled = [ 'I never completed any formal education', 'Primary/elementary school', 'Some college/university study without earning a degree', 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)', 'Bachelor’s degree (BA, BS, B.Eng., etc.)','Master’s degree (MA, MS, M.Eng., MBA, etc.)', 'Associate degree', 'Professional degree (JD, MD, etc.)', 'Other doctoral degree (Ph.D, Ed.D., etc.)',]
    lowed = [ 'I never completed any formal education', 'Primary/elementary school', 'Some college/university study without earning a degree', 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)']
    highed = ['Bachelor’s degree (BA, BS, B.Eng., etc.)','Master’s degree (MA, MS, M.Eng., MBA, etc.)', 'Associate degree', 'Professional degree (JD, MD, etc.)', 'Other doctoral degree (Ph.D, Ed.D., etc.)']

    allex = ['0-2 years', '3-5 years', '6-8 years', '9-11 years', '12-14 years', '15-17 years', '18-20 years', '21-23 years', '24-26 years', '27-29 years', '30 or more years']
    littlex = ['0-2 years', '3-5 years']
    lotofex = ['6-8 years', '9-11 years', '12-14 years', '15-17 years', '18-20 years', '21-23 years', '24-26 years', '27-29 years', '30 or more years']

    print_salary(df, 'Female')
    print_info(df, 'Full-stack developer', lotofex, lowed)

    print_info(df, 'Full-stack developer', lotofex, highed)

    print_info(df, 'C-suite executive (CEO, CTO, etc.)', allex, alled)

#     # Create GDP list and remove missing/outlying value(s)
#     GDP_list = []
#     GDP_list = df[GDP].tolist()
#     GDP_cleanlist = [x for x in GDP_list if str(x) != 'nan']
#     GDP_cleanlist.remove(max(GDP_cleanlist))

    # Plot a histogram of the GDPs
    # plt.hist(GDP_cleanlist, 20)
    # plt.xlabel(GDP)
    # plt.ylabel('Employees')
    # plt.show()

    # # Plot a boxplot of the infant mortality
    # df[INFANT].plot.box()
    # plt.show()

    # Write data to a json file
    # with open('bias.json', 'w') as outfile:
    #     outfile.write(df.set_index(GENDER).to_json(orient='index'))
