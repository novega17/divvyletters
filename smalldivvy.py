import csv
import matplotlib.pyplot as plt
import pandas as pd
%pylab inline
ACCEPTED_MSG = """
Hi Customer born in the year {} :

On the start time of {} you left from station {} on your first divvy ride of the day.

You successfully completed your ride at {} at the station {} .

We are thrilled to let you know that your fitness goal was acheived.

We look forward to seeing you continue to use our bike service and enjoy a truly green transportation alternative.
Thank you,
Divvy Bike Organizers
"""

csv_file = open('datain.csv')
csv_reader =csv.reader(csv_file, delimiter=',')
next(csv_reader)

for row in csv_reader:
    trip_id, start_time, end_time, bikeid, tripduration, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthyear = row
    msg = ACCEPTED_MSG.format(birthyear, start_time, from_station_name, end_time, to_station_name)
    print("E-mail content:")
    print(msg)
    data2 = pd.read_csv("datain.csv")
    data2=data[["birthyear"]]
    # data_sorted = data2.sort(["birthyear"])
    data2.head()
    data2.plot()
    plt.show()
csv_file.close()