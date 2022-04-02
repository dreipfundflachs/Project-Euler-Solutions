# PROJECT EULER - PROBLEM 19
import time


start = time.time()

months = {'january': 31, 'february': 28, 'march': 31,
          'april': 30, 'may': 31, 'june': 30,
          'july': 31, 'august': 31, 'september': 30,
          'october': 31, 'november': 30, 'december': 31
          }

# Jan 1 1901 was a Tuesday
week = ['tuesday', 'wednesday', 'thursday',
        'friday', 'saturday', 'sunday', 'monday'
        ]


day_count = 0
sunday_count = 0
for year in range(1901, 2001):
    if (year % 400) == 0 or ((year % 4) == 0 and (year % 100) != 0):
        leap_year = True
    else:
        leap_year = False
    for month, number_of_days in months.items():
        if month == 'february' and leap_year:
            actual_number_of_days = number_of_days + 1
        else:
            actual_number_of_days = number_of_days
        for day in range(1, actual_number_of_days + 1):
            current_day = week[day_count % 7]
            if current_day == 'sunday' and day == 1:
                sunday_count += 1
            day_count += 1

print(sunday_count)

end = time.time()
print(f"Program runtime: {end - start} seconds")
