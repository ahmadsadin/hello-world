import datetime


def getCurrentDate():	# return current date in dd/mm/yyyy string format
	date = datetime.datetime.now()
	return date.strftime("%d/%m/%Y")
	
def getCurrentTime():	# return current time in hh:mm:ss string format
	date = datetime.datetime.now().time()
	return date.strftime("%H:%M:%S")
	

def getSubstring(s, i, j):	# slicer function to extract digits from date
	if j < i:
		raise ValueError("j has to be greater than i")
	elif i < 0:
		raise IndexError("i should be greater than 0")	
	else:
		return s[i:j+1]
		
		
def getDay(date):	# return day of date as int
	day=getSubstring(date,0,1)
	return int(day)
	
def getMonth(date):	# return month of date as int
	month=getSubstring(date,3,4)
	return int(month)
	
def getYear(date):	# return year of date as int
	year=getSubstring(date,6,9)
	return int(year)

def getHour(time):	# return hour of time as int
	hour=getSubstring(time,0,1)
	return int(hour)
	
def getMinute(time):	# return month of date as int
	minute=getSubstring(time,3,4)
	return int(minute)
	
def getSecond(time):	# return year of date as int
	second=getSubstring(time,6,7)
	return int(second)
	
	
def isLeapYear(year):	# checks if year is leap and returns boolean
	bool = False
	if year % 4 == 0:	# if divisible by 4 then leap
		bool = True
		if year % 100 == 0:		# if centenary year
			if year % 400 == 0:	# must be divisible by 400 to be leap
				bool = True
			else:
				bool = False
	return bool
		

def getDaysInAMonth(month, year):	# returns # of days in month as int
	if month <= 7:		# if month is between Jan-July
		if month % 2 == 0:	# if month number is even
			daycount = 30	# return 30 days
			if month == 2:	# if Feb return 28
				daycount = 28
				if isLeapYear(year):	# if leap, return 29
					daycount = 29
		else:
			daycount = 31	# else return 31 for odd months
	else:					# if month is between Aug-Dec (knuckle calc!)
		if month % 2 == 0:	# now if even, return 31
			daycount = 31
		else:
			daycount = 30	# else return 30 for odd months
	return daycount
	
	

def main():
	current_date = "31/12/2019"
# 	current_date = getCurrentDate()
	current_time = getCurrentTime()
	
	current_hr = getHour(current_time)
	current_min = getMinute(current_time)
	current_sec = getSecond(current_time)
	
	current_year = getYear(current_date)
	current_month = getMonth(current_date)
	current_day = getDay(current_date)
	
	julian_day = 0
	for m in range(1, current_month):
		julian_day = getDaysInAMonth(m, current_year) + julian_day
	julian_day = julian_day + current_day
		
# 	print(julian_day)
	print(current_hr)
	print(current_min)
	print(current_sec)
	
	
if __name__ == "__main__":
    main()