# most_active_cookie

A command line program in python to process the log file and return the most active cookie for specified day. 

### Execution

Command: python3 most_active_cookie.py your_csv_file -d yyyy-mm-dd
Sample command: python3 most_active_cookie.py cookie_log.csv -d 2018-12-09

### Testing
To execute the unit/integration tests, navigate to the root directory and run the following command:
python3 -m unittest

### Sample CSV

|cookie          |timestamp                |
|----------------|-------------------------|
|AtY0laUfhglK3lC7|2018-12-09T14:19:00+00:00|
|SAZuXPGUrfbcn5UA|2018-12-09T10:13:00+00:00|
|5UAVanZf6UtGyKVS|2018-12-09T07:25:00+00:00|
|AtY0laUfhglK3lC7|2018-12-09T06:19:00+00:00|
|SAZuXPGUrfbcn5UA|2018-12-08T22:03:00+00:00|
|4sMM2LxV07bPJzwf|2018-12-08T21:30:00+00:00|
|fbcn5UAVanZf6UtG|2018-12-08T09:30:00+00:00|
|4sMM2LxV07bPJzwf|2018-12-07T23:30:00+00:00|

Output for Sample CSV:
AtY0laUfhglK3lC7
