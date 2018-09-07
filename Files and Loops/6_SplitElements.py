f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = []
for row in rows:
    split_list = row.split(',')
    final_data.append(split_list)
print(final_data[0:5])