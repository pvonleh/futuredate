#Prince D. Vonleh

from datetime import datetime, timedelta
#Get a future date of expiration for anything.
# e.g. subscribing to a site that says you have 180 days left
amt = int(input("Please enter the amount of days you would like to add to the current date: "))
print ('Today: ',datetime.now().strftime('%d/%m/%Y %H:%M:%S') )
date_after_month = datetime.now()+ timedelta(days=amt)
print ('After', amt ,'days', date_after_month.strftime('%d/%m/%Y %H:%M:%S'))