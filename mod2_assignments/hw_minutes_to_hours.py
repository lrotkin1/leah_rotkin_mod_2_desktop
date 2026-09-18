"""Leah Rotkin - user can calculate how many hours and minutes there is in their entry"""

"""my function takes the user's entry and divides it first by 60 to get the hours and then it gets the remaining minutes"""
def minutes_to_hours_and_minutes():
    hours=minutes//60 #makes the value of minutes equal the value of the user's input divided by 60 (to get the amount of hours)
    final_minutes=minutes%60 #makes the value of final minutes equal the value of the user's input divided by 60 keeping only the remainder to get the remaining minutes
    #below - prints the hours and the minutes
    print(hours, 'hours and', final_minutes, 'minutes')

minutes=int(input('How many minutes do you want to calculate?')) #makes the value of minutes equal the users input

#calls my function
minutes_to_hours_and_minutes()