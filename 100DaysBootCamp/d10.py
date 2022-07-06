# Function with outputs

def format_name(f_name, l_name):
    # docString
    """
        Takes a first and last name and format it to return the
        title case of version of the name.
    """
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return (f"{formatted_f_name} {formatted_l_name}")


# print(format_name(input("What is your first name? "),
    # input("What is your last name? ")))


# Challenge Day 10.1
def is_leap(year):
    is_leap_year = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return is_leap_year
            else:
                return not is_leap_year
        else:
            return is_leap_year
    else:
        return not is_leap_year


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 30, 31, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
# print(days)
# print(is_leap(2016))
# format_name()


# While loops, Flags and Recursion
