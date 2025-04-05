def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5500)
print(hours, minutes, seconds)

def lucky_number(name):
    user_number = len(name) * 9
    print(user_number)
lucky_number("christine")

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)

# This function calculates the number of days in a variable number of
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function's parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# aa year(years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years * 365) + (months * 30) + days
# Use the "return" keyword to send the result of the "my_days"
# Calculation to the function call.
    return my_days
# Function call with user provided parameter values
print(find_total_days(2,5,23))

def convert_volume(fluid_ounce):
    ml = fluid_ounce * 29.5
    return ml
print("The volume in millimeters is " + str(convert_volume(2)))
