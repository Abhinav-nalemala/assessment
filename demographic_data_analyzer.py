import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # What percentage of people with advanced education make more than 50K?
    higher_education = None
    higher_education_rich = None
    percentage_higher_education_rich = None

    # What percentage of people without advanced education make more than 50K?
    lower_education = None
    lower_education_rich = None
    percentage_lower_education_rich = None

    # What is the minimum number of hours a person works per week?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = None
    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {percentage_higher_education_rich}%")
        print
