"""
Ruba Al-talhi
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
          city = input("choose a city , new york city, chicago or washington?\n").lower()
          if city not in ("new york city", "chicago", "washington"):
            print("Sorry, you entered the wrong city name. Try again.")
            continue
          else:
            break

     # get user input for month (all, january, february, ... , june)
    while True:
          month = input("choose a month , January, February, March, April, May, June or 'all'?\n").lower()  
          if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Sorry, you entered the wrong month name. Try again.")
            continue
          else:
            break
    # user input for day of week (all, monday, tuesday, ... sunday)
    while True:
          day = input("choose a day : Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'all'?.\n").lower()
          if day not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
            print("Sorry, you entered the wrong day name. Try again.")
            continue
          else:
            break

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of the week:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common starting hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end)

    # display most frequent combination of start station and end station trip
    df['Frequent Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Frequent Trip'].mode()[0]
    print('Most common trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time, 'seconds')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User Type Count:\n', user_type_count)

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender Count:\n', gender_count)
    except KeyError:
        print('\nGender Count: No data available.')

    # Display earliest, most recent, and most common year of birth
    try:
        birth_min = int(df['Birth Year'].min())
        print('\nEarliest year of birth:', birth_min)
    except KeyError:
        print('\nEarliest year of birth: No data available.')

    try:
        birth_max = int(df['Birth Year'].max())
        print('Most recent year of birth:', birth_max)
    except KeyError:
        print('Most recent year of birth: No data available.')

    try:
        birth_mode = int(df['Birth Year'].mode()[0])
        print('Most common year of birth:', birth_mode)
    except KeyError:
        print('Most common year of birth: No data available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays raw data 5 rows at a time, if requested."""

    show_data = input('\nWould you like to see 5 rows of raw data? yes or no:\n').lower()
    if show_data != 'no':
        i = 0
        while (i < df['Start Time'].count() and show_data != 'no'):
            print(df.iloc[i:i+5])
            i += 5
            more_data = input('\nWould you like to see 5 more rows of data? yes or no:\n').lower()
            if more_data != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()