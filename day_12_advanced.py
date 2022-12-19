# This function asks a user to input their year of birth and calculates their current age in minutes
# This question forms part of the advanced task for challenge day 12 of 50 days of Python.

import datetime


def age_in_minutes():
    while True:
        year_min = 525600  # set num of minutes in year
        current_year = datetime.datetime.now()  # get correct datetime
        today_year = current_year.year  # get current year

        user_input = input("Enter year of birth (in digits): ")
        if (len(user_input) < 4) or (len(user_input)) > 4:  # check if year or not 4 digits
            print("Invalid date length! Please enter a 4 digit YOB")
            continue
        if (int(user_input) < 1900) or (int(user_input) > today_year):  # check if year is incorrect
            print("Invalid year! Please enter a date between 1900 and current year")
            continue
        elif len(str(user_input)) == 4:
            age_min = (today_year - int(user_input)) * year_min  # calculate age in minutes
            print("You are {:,} minutes old".format(age_min))
        break  # get out of loop if correct input made


age_in_minutes()
