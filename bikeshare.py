import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

sure = ""


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ""
    while city not in CITY_DATA.keys():
        print(" \Hello to our bike share program. \n")
        print(" please choose one city from the cities below. \n")
        print(" 1.chicago \n 2.new york city \n 3.washington")
        city = input("write  the city name as shown above :-").lower().strip()

        if city not in CITY_DATA.keys():
            print(" :( You entered a wrong city, please check your spelling :(")

    print(" you have chosen the city >> {}".format(city))
    

    # TO DO: get user input for month (all, january, february, ... , june)
    months_dict = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 5, "all": 7}
    months_list = ["january", "february", "march", "april", "may", "june", "all"]
    month = ""
    while month not in months_dict.keys():
        print("\nplease type the month you want to search for")
        print("Type 'all' if you want data from all months \n")
        print(months_list)
        print("\n")
        month = input("write  the month name as shown above :-").lower().strip()
        if month not in months_dict.keys():
            print(" :( You entered a wrong month, please check your spelling :(")

    print(" you have chosen the month  >> {}".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]

    day = ""
    while day not in days_list:
        print("\nplease type the day you want to search for")
        print("Type 'all' if you want data from all days \n")

        print(days_list)
        day = input("write  the day name as shown above :-").lower().strip()
        if day not in days_list:
            print(" :( You entered a wrong day, please check your spelling :(")

    print("you have chosen the day {}".format(day))

    print(" displaying data for \n city: {} \n the month: {} \n the day:{}".format(city, month, day))
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    cdf = df.copy(deep=True)

    # convert the Start Time column to datetime
    cdf['Start Time'] = pd.to_datetime(cdf['Start Time'])

    # extract month and day of week from Start Time to create new columns
    cdf['month'] = cdf['Start Time'].dt.month
    cdf['day_of_week'] = cdf['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        cdf = cdf[cdf['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        cdf = cdf[cdf['day_of_week'] == day.title()]

    return cdf


print('-' * 40)


def time_stats(df):
    cdf = df.copy(deep=True)
    months_dict = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 5, "all": 7}
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = cdf['month'].mode()[0]
    print("the most common month is : {}".format(common_month))

    # TO DO: display the most common day of week

    common_day = cdf['day_of_week'].mode()[0]
    print("The most common day is : {}".format(common_day))

    # TO DO: display the most common start hour
    cdf['hour'] = cdf['Start Time'].dt.hour
    common_hour = cdf['hour'].mode()[0]
    print("The most common hour is : {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    cdf = df.copy(deep=True)
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station = cdf["Start Station"].mode()[0]
    print("The most common Start Station is : {} \n".format(common_station))
    # TO DO: display most commonly used end station
    common_station_end = cdf["End Station"].mode()[0]
    print("The most common End Station is : {} \n".format(common_station_end))

    # TO DO: display most frequent    combination of start station and end station trip

    cdf["Frequent Combination"] = cdf["Start Station"] + " TO " + cdf["End Station"]
    freq_start_end = cdf["Frequent Combination"].mode()[0]
    print("The most frequent combination of start station and end station trip is :{} \n".format(freq_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    cdf = df.copy(deep=True)
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    duration_trip = cdf["Trip Duration"].sum()
    print("The total trip durations is :{}".format(duration_trip))
    # TO DO: display mean travel time
    mean_travel = cdf["Trip Duration"].mean()
    mean_travel = float(mean_travel) // 60
    print(" The average travel time is {} minutes".format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    cdf = df.copy(deep=True)
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = cdf["User Type"].value_counts()
    print("The counts of the user types are : \n{}".format(user_types))

    # TO DO: Display counts of gender
    try:
        gender_counts = cdf["Gender"].value_counts()
        print(" The counts of the user genders are : \n{} \n".format(gender_counts))
    except:
        print("\n No Gender specifications found in Washington \n")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early = cdf["Birth Year"].min()
        early = (int(early))
        recently = cdf["Birth Year"].max()
        recently = (int(recently))
        most_common_year = cdf["Birth Year"].mode()[0]
        most_common_year = (int(most_common_year))
        print("\nThe earliest year of the users is :{}".format(early))
        print("\nThe most recent year of the users is:{}".format(recently))
        print("\nThe most common year of birth of users is:{}\n".format(most_common_year))
    except:
        print("\n NO Birth Year specification for users in Washington \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


""" I will add a new function to display rows data according client request"""


def raw_data(df):
    trial1 = 0
    trial2 = 5
    print("please enter 'Yes' if you want to display 5 rows of data , or 'No' if you don't")
    response = input().lower().strip()

    while response == "yes":
        print(" \n displaying desired raw data.... \n")
        showing = df.iloc[trial1: trial2]
        print(showing)
        trial1 += 5
        trial2 += 5

        print("please enter 'Yes' if you want to display MORE 5 rows of data , or 'No' if you don't")
        response = input().lower().strip()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
