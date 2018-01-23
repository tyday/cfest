"""
First foray into looking into a csv with python

I think I'm going to create a class that holds the info for each entry.abs
Maybe.

Created by: Ty Day
Created when: 1/23/2018
"""
import datetime

def convert_to_date(requestdate):
    """ Converts a string in 2018-11-01 format into
    and returns year,month,day tuple"""
    requestdate = requestdate.strip()
    year = int(requestdate[0:4])
    month = int(requestdate[5:7])
    day = int(requestdate[8:10])
    return year, month, day
    
def getRequestDates():
    inFile = open('shiftrequests.csv')
    population = []
    for l in inFile:
        try:
            line = l.strip()
            requestdate = line.split(',')[5]
            year,month,day = convert_to_date(requestdate)
            # year = int(requestdate[0:4])
            # month = int(requestdate[5:7])
            # day = int(requestdate[8:10])
            req_date = datetime.date(year, month, day)
            population.append(req_date)
        except:
            continue
    return population


request_date = getRequestDates()
year_dict = {}
for entry in request_date:
    if entry.year in year_dict:
        year_dict[entry.year] +=1
    else:
        year_dict[entry.year] = 1
print(year_dict)

