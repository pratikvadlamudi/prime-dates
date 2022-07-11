# IMPORTS:

import pandas as pd
import calendar
import math
from datetime import datetime
from IPython.display import display,HTML


# FUNCTIONS:

def getDates(startDate, endDate):
  return pd.date_range(start = startDate, end = endDate).to_pydatetime().tolist()

def isPrimeNumber(n):
  for i in range(2,int(math.sqrt(n))+1):
      if (n%i) == 0:
        return False
  return True

def getPrimeNumberList(startDate, endDate, format):
  primeDateList = []

  for date in getDates(startDate, endDate):
    if isPrimeNumber(int(date.strftime(format))):
      primeDateList.append(date)
  return primeDateList

def makeHighlightedCalendar(startDate, endDate, format):
  dateList = getPrimeNumberList(startDate, endDate, format)
  cal = calendar.HTMLCalendar()
  startDate = datetime.strptime(startDate, "%Y-%m-%d")
  endDate = datetime.strptime(endDate, "%Y-%m-%d")
  for year in range(startDate.year, endDate.year + 1):
      for month in range(1, 13):
        highlightedMonth = cal.formatmonth(year,month)
        for date in dateList:
          if date.month == month:
              highlightedMonth = highlightedMonth.replace('>%i<'%date.day, ' bgcolor="#66ff66"><b>%i</b><'%date.day)
        display(HTML(highlightedMonth))

# MAIN:

makeHighlightedCalendar("2022-01-01", "2024-01-01", "%m%d%Y")