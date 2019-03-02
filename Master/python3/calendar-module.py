# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/calendar-module/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
import calendar

m,d,y = list(map(int, input().split()))
dt = datetime.datetime(y, m, d)
print(calendar.day_name[dt.weekday()].upper())

