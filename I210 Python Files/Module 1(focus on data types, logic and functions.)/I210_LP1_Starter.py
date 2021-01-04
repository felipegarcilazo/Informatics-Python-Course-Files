# Write the function for Section 3 here

# Main section

# Each list has 20 temperatures recorded in the given city during the month of February.
# For Indiana, the average temperature range in February is 24 - 40 F.
# This is based on climate data from 1981 - 2010.
# Given the data below, are temperatures rising, falling, or neither?
indy_temps = [27, 24, 64, 48, 34, 23, 61, 19, 17, 53, 19, 44, 44, 28, 10, 55, 31, 36, 32, 52]
bloomington_temps = [64, 56, 30, 26, 20, 46, 13, 41, 57, 10, 32, 43, 53, 23, 59, 41, 18, 44, 24, 20]
lafayette_temps = [55, 56, 13, 49, 30, 36, 16, 26, 58, 17, 53, 57, 14, 57, 60, 15, 54, 28, 56, 10]
evansville_temps = [44, 34, 36, 34, 38, 57, 63, 21, 59, 43, 41, 58, 51, 43, 44, 27, 12, 63, 19, 21]
fort_wayne_temps = [19, 61, 19, 53, 63, 32, 61, 60, 43, 28, 25, 61, 14, 57, 12, 34, 52, 17, 29, 11]

# Section 1 - Compute the Average and Offset

all_temps = (indy_temps + bloomington_temps + lafayette_temps +
             evansville_temps + fort_wayne_temps)
total_temp = 0
for temp in all_temps:
    total_temp += temp
average_temp = total_temp / len(all_temps)
normal_temp = 32
print('All temperatures:')
print(all_temps)
print('The average of all temperatures is: ' + str(average_temp) + 'F.')
if average_temp > normal_temp:
    difference = average_temp - normal_temp
    print('This was', round(difference, 2), 'above normal.')
elif average_temp < normal_temp:
    difference = normal_temp - average_temp
    print('This was', round(difference, 2), 'below normal.')
else:
    print('This is the normal temperature')

# Section 2 - Compute the Temperature Ranges

below_range = 0
above_range = 0
within_range = 0
for temp in all_temps:
    if temp < 24:
        below_range += 1
    elif temp > 40:
        above_range += 1
    else:
        within_range += 1
print('')
print(str(below_range), 'readings were below the normal range.')
print(str(within_range), 'readings were within the normal range.')
print(str(above_range), 'readings were above the normal range.')

# Section 3 - Print Temperature Charts (call the function here)

def histogram(city):
    if city == indy_temps:
        city_name = 'Indianapolis IN'
    elif city == bloomington_temps:
        city_name = 'Bloomington IN'
    elif city == lafayette_temps:
        city_name = 'Lafayette IN'
    elif city == evansville_temps:
        city_name = 'Evansville IN'
    elif city == fort_wayne_temps:
        city_name = 'Fort Wayne IN'
    else:
        print('No temperature chart found for that city.')
    first_range = 0
    second_range = 0
    third_range = 0
    fourth_range = 0
    fifth_range = 0
    sixth_range = 0
    for temp in city:
        if 10 <= int(temp) <= 19:
            first_range += 1
        elif 20 <= temp <= 29:
            second_range += 1
        elif 30 <= temp <= 39:
            third_range += 1
        elif 40 <= temp <= 49:
            fourth_range += 1
        elif 50 <= temp <= 59:
            fifth_range += 1
        else:
            sixth_range += 1
    dashes = '-' * 45
    print('Temperature Chart for', city_name)
    print(dashes)
    print('10 - 19F :', '*' * first_range)
    print('20 - 29F :', '*' * second_range)
    print('30 - 39F :', '*' * third_range)
    print('40 - 49F :', '*' * fourth_range)
    print('50 - 59F :', '*' * fifth_range)
    print('60 - 65F :', '*' * sixth_range)
    print(dashes)
