# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp "])

## Average temp
# temp_list = data["temp"].to_list()
# average_temp = round(sum(temp_list) / len(temp_list))
# print(average_temp)

## Average temp using pandas 
# average_temp = data["temp"].mean()
# print(average_temp)

# To get max using pandas
print(data["temp"].max())
