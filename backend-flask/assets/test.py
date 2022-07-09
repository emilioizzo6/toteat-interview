import json
import os
import datetime
with open(os.path.join("ventas.json")) as file:
    data = json.load(file)

for key, value in data[1].items():
    print(key, value)

# dc = data[1]['date_closed']
# do = data[1]['date_opened']
# dcd = datetime.datetime.strptime(dc, '%Y-%m-%d %H:%M:%S')
# dod = datetime.datetime.strptime(do, '%Y-%m-%d %H:%M:%S')
# diff_time = dcd - dod

# dc2 = data[2]['date_closed']
# do2 = data[2]['date_opened']
# dcd2 = datetime.datetime.strptime(dc2, '%Y-%m-%d %H:%M:%S')
# dod2 = datetime.datetime.strptime(do2, '%Y-%m-%d %H:%M:%S')
# diff_time2 = dcd2 - dod2

# print(diff_time)
# print(diff_time2)
# print((diff_time + diff_time2)/2)    

