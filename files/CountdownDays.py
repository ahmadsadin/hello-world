import datetime


def getCurrentDate():	# return current date in dd/mm/yyyy string format
	date = datetime.datetime.now()
	return date.strftime("%d/%m/%Y")
	

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
	

def dueDateHasPassed(current, due):		# check if due date has passed
	bool = True
	if getYear(current) < getYear(due):	# if current year is under due year
		bool = False					# then due date passed is False
	elif getYear(current) == getYear(due):	# if current year is equal to due year
		if getMonth(current) < getMonth(due):	# then check months column
			bool = False
		elif getMonth(current) == getMonth(due):	#if current month equals due month
			if getDay(current) < getDay(due):		# check day column
				bool = False
	return bool


def countDaysLeft(current, due):	# counts diff between current and due dates
	days_left = 0
	if dueDateHasPassed(current, due):	# if due date has passed return 0
		return days_left
	# else if year and month columns are equal
	elif getYear(current) == getYear(due) and getMonth(current) == getMonth(due):
		days_left = getDay(due) - getDay(current)	# just count the diff in days
		return days_left
	# else if years are equal but month columns are not
	elif getYear(current) == getYear(due) and getMonth(current) < getMonth(due):
		run_month = getMonth(current) + 1	# set running month to next one from current
		while run_month < getMonth(due):	# loop thru all months until due month
			days_left = days_left + getDaysInAMonth(run_month, getYear(current))
			run_month += 1					# count # of days and increment month
	# if current and due years are different
	else:	
		run_year = getYear(current)	# set running year to current
		while run_year <= getYear(due):	# loop thru all years until due year reached
			if run_year == getYear(current):	# if running year is in current year
				run_month = getMonth(current) + 1
				while run_month <= 12:	# loop through current month till end of year
					days_left = days_left + getDaysInAMonth(run_month, run_year)
					run_month += 1
			elif run_year == getYear(due):	# if running year is in due year
				run_month = 1
				while run_month < getMonth(due):	# loop thru Jan till due month
					days_left = days_left + getDaysInAMonth(run_month, run_year)
					run_month += 1
			else:						# if running year is neither current/due year
				run_month = 1
				while run_month <= 12:	# loop thru 12 months Jan-Dec
					days_left = days_left + getDaysInAMonth(run_month, run_year)
					run_month += 1
			run_year += 1
	# at the very end calculate days diff
	days_left = days_left + getDay(due) + \
	(getDaysInAMonth(getMonth(current), getYear(current)) - getDay(current))
	return days_left
	
	
def displayCountDown(due_date):
	current_date = getCurrentDate()
	print("Today is: %s" % current_date)
	print("Due date: %s" % due_date)
	days_left = countDaysLeft(current_date, due_date)
	if days_left > 0:
		print("You have %d days left. You can do it!" % days_left)
	else:
		print("The due date has passed! :( Better luck next time!")
	

def main():
	due_date = raw_input("Pls enter the due date in dd/mm/yyyy format: ")
	displayCountDown(due_date)
	
if __name__ == "__main__":
    main()