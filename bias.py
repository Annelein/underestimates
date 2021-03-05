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
DENSITY = "AssessBenefits10"
INFANT = "AssessBenefits11"
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


if __name__ == '__main__':
    # Load data into a pandas DataFrame
    df = load_data(INPUT_CSV)

    # Select data from DataFrame
    # df = df[[GENDER, FORMALED, DENSITY, INFANT, GDP]]

    # Strip data where necessary
    df[FORMALED] = df[FORMALED].str.strip()
    df[GENDER] = df[GENDER].str.strip()

    # Convert relevant columns to floats
    # df = to_float(df, GDP)
    # df = to_float(df, INFANT)
    # df = to_float(df, DENSITY)

    # Print descriptive statistics
    central_tendency(df, GDP)
    five_number(df, INFANT)

    # frequency_df = df.loc[df['DevType'] == 'Full-stack developer']
    frequency_df = df['Gender'].value_counts()
    print(frequency_df, "\n")

    frequency_df = df[FORMALED].value_counts()
    print(frequency_df, "\n")

    frequency_df = df['JobSatisfaction'].value_counts()
    print(frequency_df, "\n")

    case1 = df.loc[df['DevType'] == 'Full-stack developer']
    case1 = case1.loc[df['DevType'] == 'Full-stack developer']
    case1 = case1[FORMALED].value_counts()
    print(case1, "\n")

    # Mannen:
    case1 = df.loc[df['Gender'] == 'Male']
    case1 = case1.loc[df['DevType'] == 'Full-stack developer']
    print("Male Full-stack developers: ")
    print(case1.shape[0], "\n")
    # case1 = case1.loc[df['DevType'] == 'Full-stack developer']
    case1 = case1[FORMALED].value_counts()
    print(case1, "\n")

    # Vrouwen:
    case1 = df.loc[df['Gender'] == 'Female']
    case1 = case1.loc[df['DevType'] == 'Full-stack developer']
    print("Female Full-stack developers: ")
    print(case1.shape[0], "\n")
    # case1 = case1.loc[df['DevType'] == 'Full-stack developer']
    case1 = case1[FORMALED].value_counts()
    print(case1, "\n")

    frequency_df = df['YearsCoding'].value_counts()
    print(frequency_df, "\n")

    # henk = df.loc[df['YearsCoding'] == '3-5 years', '0-2 years']
    henk = df.loc[df['YearsCoding'] <= '3-5 years']
    henk = henk[[GENDER, FORMALED, GDP, 'YearsCoding', 'EducationParents']]

    print(henk, "\n")



    # result = df.head(10)
    # print("First 10 rows of the DataFrame:")
    # print(result)

    # Create GDP list and remove missing/outlying value(s)
    GDP_list = []
    GDP_list = df[GDP].tolist()
    GDP_cleanlist = [x for x in GDP_list if str(x) != 'nan']
    GDP_cleanlist.remove(max(GDP_cleanlist))

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
