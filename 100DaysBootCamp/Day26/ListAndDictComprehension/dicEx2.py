"""
    You're going to use dictionary comprehension to create a dictionary called weather_f that takes each temperature in degrees Celcius and converts
    it into Farenheit
    
    Hint; (temp_c*9/5) + 32 = temp_f
"""

weather_c ={
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24,
}

def convert_c_to_f(dict_weather):
    """Converts celcius to f """
    return {day:(temp_c*9/5) + 32 for (day,temp_c ) in weather_c.items()}

print(convert_c_to_f(weather_c))