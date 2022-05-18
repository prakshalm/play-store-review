from datetime import datetime, timedelta

# datetime object containing current date and time
now = datetime.now()
print('Job Running at ' + str((datetime.now() + timedelta(hours=5.5)).strftime('%Y-%m-%d %H:%M:%S')))

print('Modules successfully loaded')
