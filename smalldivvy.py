import csv
ACCEPTED_MSG = """
Hi Customer born in the year {} :

On the start time of {} you left from station {} on your first divvy ride of the day.

We are thrilled to let you know that your fitness goal was acheived.

We look forward to seeing you on 11/1/2017 in our office for the fitness seminar.
Thank you,
Divvy Workshop Organizers
"""

csv_file = open('datain.csv')
csv_reader =csv.reader(csv_file, delimiter=',')
next(csv_reader)

for row in csv_reader:
    trip_id, start_time, end_time, bikeid, tripduration, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthyear = row
    msg = ACCEPTED_MSG.format(birthyear, start_time, from_station_name)
    print("E-mail content:")
    print(msg)

csv_file.close()
