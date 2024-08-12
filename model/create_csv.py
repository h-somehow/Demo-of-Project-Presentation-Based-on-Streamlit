import csv
 
data = [
    ['Weight', 'Species'],
    [48.3, 'Dog'],
    [32.3, 'Dog'],
    [32.3, 'Dog'],
    [32.3, 'Dog'],
    [45.4, 'Dog']
]
 
filename = 'data.csv'

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
 
print(f'{filename} created successfully.')