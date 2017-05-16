# NAME OBETI SILIVIO 
# REG NO 16/U/20182/PS
#the expected output should be
# day, date, month,year
#for example friday 20th august 1990.

#importing the datetime, and calendar module
import datetime,calendar
#in order to use the programme continuously avery year i set the time with system time 
cur_year = int(datetime.date.today().strftime('%Y'))

date = input("Enter birth date (1-31)\n")

endings = ["st", "nd", "rd"]+ 17*["th"] + ["st", "nd", "rd"] + 7*["th"] + ["st"]

days = ['Monday','Tuesday','Wednesday',
        'Thursday','Friday','Saturday',
        'Sunday']

month = int(input("Enter the month in which you were born in(1-12)\n"))

month_names = ['January','February','March',
                'April','May','June',
                'July','August','September',
                'October','November','December']

age = int(input("How old are you now? \n"))

month_birth = month_names[month-1]
date_birth = int(date)
year_birth = (cur_year-age)
var4 = date+endings[date_birth-1]
var5 = calendar.weekday(year_birth,month,date_birth)
var6 = days[var5]
#printing the date and year
print("You were born on",var6 ,var4, month_birth,", " ,year_birth)
