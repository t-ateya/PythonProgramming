"""
    Activity Selection Problem

    Given N number of activities with their start and end times, we need to select the max number of activities that can be 
    performed by a single person, assuming that a person can only work on a single activity at a time.

    Algorithm
    1. Sort activities based on finish time
    2. Select first activity from sorted array and print it
    3. For all remaining activities:
        If the start time of this activity is greater or equal to the finish time of previously selected activity, then 
        select this activity and print it
"""

activities = [ ["A1", 0, 6],
               ["A2", 3, 4],
               ["A3", 1, 2],
               ["A4", 5, 8],
               ["A5", 5, 7],
               ["A6", 8, 9],

]

def print_max_activities(activities):
    activities.sort(key=lambda x: x[2]) #Sort activities by col 2
    i = 0
    first_activity = activities[i][0]
    print(first_activity)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j 
print_max_activities(activities)