DEBUG_GEN = 0
DEBUG_FUNC = 0

# Number of Days    Month
#             31        1
#          28/29        2
#             31        3
#             30        4
#             31        5
#             30        6
#             31        7
#             31        8
#             30        9
#             31       10
#             30       11
#             31       12


MONTH = { 
          1: "Jan",
          2: "Feb",
          3: "Mar",
          4: "Apr",
          5: "May",
          6: "Jun", 
          7: "Jul",
          8: "Aug", 
          9: "Sep",
          10: "Oct",
          11: "Nov",
          12: "Dec"
          }

DAY = {
        0: "Mon",
        1: "Tue",
        2: "Wed",
        3: "Thu",
        4: "Fri",
        5: "Sat",
        6: "Sun"
        }
# a leap year occurs on any year evenly divisble by 4, but not on a century
# unless it is divisible by 400
def isLeap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        
        if year % 100 == 0:
            return False

        return True
    return False

# a function to return how many days are in a month, year
# month (1-12)
def total_days(month, year):
    if month < 1 or month > 12:
        print("warning: invalid month")

    # special case for February on leap years
    if month == 2:
        if isLeap(year):
            return 29
        else:
            return 28

    # 30 days in April, June, September, November
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    # 31 days all remaining months
    return 31

# test total_days
if DEBUG_FUNC:
    for y in range(1900,1905):
        for m in range(1,13):
            print(MONTH[m],y,"has",total_days(m,y),"days")


# test isLeap()
if DEBUG_FUNC:
    nLeapYears = 0
    for y in range(1900,2001):
        if isLeap(y):
            print(y, ": leap")
            nLeapYears += 1
        #else:
        #    print(y, ":")
    print("total leap years:",nLeapYears)
    print("1900 test:", isLeap(1900))  # Expect False
    print("2000 test:", isLeap(2000))  # Expect True

print("--- Problem 19 ---")

if DEBUG_GEN:
    for _ in range(15):
        print(MONTH[month],day,year,DAY[date % 7])
        date += 1

# Starting day: Monday, 1 Jan, 1901
date = 0
day = 1
month = 1
year = 1900
TOTAL_FIRST_SUNDAYS = 0
while year < 2001:
    #print(MONTH[month],day,year,DAY[date % 7])

    # check if today is Sunday and first of the month
    # and year >= 1901 (!!!!!!!!!!!)
    if DAY[date % 7] == "Sun" and day == 1 and year >= 1901:
        print(MONTH[month],day,year,DAY[date % 7])
        TOTAL_FIRST_SUNDAYS += 1
    
    # calculate next day
    day = day + 1

    # check if we roll over to the next month
    if day > total_days(month, year):
        # reset day
        day = 1

        # update to next month
        month = month + 1

        # check if we roll over to the next year
        if month > 12:
            # reset month
            month = 1

            # update to next year
            year = year + 1

    date = date + 1


#print(MONTH[month],day,year,DAY[date % 7])
print("Total Sundays that fell on the first of the month:", TOTAL_FIRST_SUNDAYS)


# What day is May 23, 2025?

# Starting day: Monday, 1 Jan, 1901
date = 0
day = 1
month = 1
year = 1900
while year < 2026:
    # break when we find out date of interest
    if day == 23 and month == 5 and year == 2025:
        break

    # calculate next day
    day = day + 1

    # check if we roll over to the next month
    if day > total_days(month, year):
        # reset day
        day = 1

        # update to next month
        month = month + 1

        # check if we roll over to the next year
        if month > 12:
            # reset month
            month = 1

            # update to next year
            year = year + 1

    date = date + 1
print(MONTH[month],day,year,"is a",DAY[date % 7],"is the date I solved this")
