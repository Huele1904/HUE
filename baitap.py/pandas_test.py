import pandas as pd

mylist = [1, 2, 3, 4, 5, 10]
my_series = pd.Series(mylist)
print(my_series)
print(type(my_series))

print(my_series[5])

mylist = [1, 2, 3]
my_series = pd.Series(mylist, index= ["x", "y", "z"])
print(my_series["y"])

calories = {"day1": 420, "day2": 380, "day3":390}
mycar = pd.Series(calories, index = ["day1", "day2", "day3"])
print(mycar)