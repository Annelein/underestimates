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

    frequency_df = df['HoursComputer'].value_counts()
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

    frequency_df = df['YearsCodingProf'].value_counts()
    print(frequency_df, "\n")

    highed = ['Bachelor’s degree (BA, BS, B.Eng., etc.)','Master’s degree (MA, MS, M.Eng., MBA, etc.)', 'Associate degree', 'Professional degree (JD, MD, etc.)', 'Other doctoral degree (Ph.D, Ed.D., etc.)',]
    lowed = [ 'I never completed any formal education', 'Primary/elementary school', 'Some college/university study without earning a degree', 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)']
    lotofex = ['6-8 years', '9-11 years', '12-14 years', '15-17 years', '18-20 years', '21-23 years', '24-26 years', '27-29 years', '30 or more years']

    # henk = df.loc[df['YearsCodingProf'].isin(['0-2 years','3-5 years'])]
    henk = df.loc[df['YearsCodingProf'].isin(lotofex)]
    henk = henk.loc[df['DevType'] == 'Full-stack developer']
    henk = henk.loc[df['Employment'] == 'Employed full-time']
    henk = henk.loc[df[FORMALED].isin(highed)]
    henk = henk[[GENDER, FORMALED, GDP, 'YearsCodingProf', 'EducationParents', 'Employment']]
    malehenk = henk.loc[df['Gender'] == 'Male']
    femalehenk = henk.loc[df['Gender'] == 'Female']
    print('amount of henks:   ' + str(henk.shape[0]))
    print('mean income henk:  ' + str(round(henk[GDP].mean(), 2)))
    print('mean income male henk:   ' + str(round(malehenk[GDP].mean(), 2)))
    print('mean income female henk: ' + str(round(femalehenk[GDP].mean(), 2)))
    print('\n')

    rows = ['0-2 years', '3-5 years', '6-8 years', '9-11 years', '12-14 years', '15-17 years', '18-20 years', '21-23 years', '24-26 years', '27-29 years', '30 or more years']
    littlex = ['0-2 years', '3-5 years']

# Bachelor’s degree (BA, BS, B.Eng., etc.)
# Master’s degree (MA, MS, M.Eng., MBA, etc.)
    brian = df.loc[df['YearsCodingProf'].isin(lotofex)]
    brian = brian.loc[df['DevType'] == 'Full-stack developer']
    brian = brian.loc[df['Employment'] == 'Employed full-time']
    brian = brian.loc[df[FORMALED].isin(lowed)]
    brian = brian[[GENDER, FORMALED, GDP, 'YearsCodingProf', 'EducationParents', 'Employment']]
    print('amount of brians:  ' + str(brian.shape[0]))
    print('mean income brian: ' + str(round(brian[GDP].mean(), 2)))

    malebrian = brian.loc[df['Gender'] == 'Male']
    femalebrian = brian.loc[df['Gender'] != 'Male']
    print('mean income male brian:   ' + str(round(malebrian[GDP].mean(), 2)))
    print('mean income female brian: ' + str(round(femalebrian[GDP].mean(), 2)))
    print('\n')

    fullstack = df.loc[df['DevType'] == 'C-suite executive (CEO, CTO, etc.)']
    print('amount of ceo:   ' + str(fullstack.shape[0]))
    male = fullstack.loc[df['Gender'] == 'Male']
    female = fullstack.loc[df['Gender'] == 'Female']
    print('mean income male:   ' + str(round(male[GDP].mean(), 2)))
    print('mean income female: ' + str(round(female[GDP].mean(), 2)))

    male = df.loc[df['Gender'] == 'Male']
    female = df.loc[df['Gender'] == 'Female']
    female = female.loc[df[FORMALED].isin(lowed)]
    male = male.loc[df[FORMALED].isin(lowed)]
    print('mean income male:   ' + str(round(male[GDP].mean(), 2)))
    print('mean income female: ' + str(round(female[GDP].mean(), 2)))

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
