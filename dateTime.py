import datetime

today = datetime.datetime.now()
print(today)
print(f'Today: {today:%y-%m-%d-%A}')
