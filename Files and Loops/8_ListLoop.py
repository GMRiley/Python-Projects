crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
cities_list = []
for outer_list in final_data:
    city = outer_list[0]
    cities_list.append(city)