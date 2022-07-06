import numpy as np
class Temperature:
    def __init__(self):
        self.temperatures_list = []
        self.day_count = 0
        self.days = 0
        self.temp_array = np.array([])
    
    def get_temps(self):
        "Returns the values of temperature for n days"
        n_days = int(input("How many day's temperature?: "))
        self.days = n_days
        self.day_count +=1
        while self.day_count <=self.days:
            temp = input(f"Day {self.day_count}'s high temp:  ")
            self.temperatures_list.append(float(temp))
            self.day_count +=1
        self.temp_array = np.array(self.temperatures_list)
        print(f"The temp values for {self.days} days are: {self.temperatures_list}")
    

        
    def cal_average_temp(self):
        """Returns the average of all the temps"""
        average = sum(self.temp_array)/len(self.temp_array)
        print(f"Averge: {average}")
        self.check_temp_range(average)
    

    def check_temp_range(self, average):
        """"Returns number of days having temperatures above average"""
        count = 0
        for temp in self.temperatures_list:
            if temp > average:
                count +=1
        print(f"{count} day(s) above average")



tp = Temperature()
tp.get_temps()
tp.cal_average_temp()

