"""
Zoom API Example

Intended to provide demonstration of Zoom API utilization using
pre-built client to communicate with system. This example will
take input from the user on a local destination filepath, execute
a Zoom API request for analytics data from last month, then create
a CSV report of that data in the provided destination filepath.
Note: please enable API access in your Zoom account and setup the
.zoom_api_config file with relevant content prior to running for
best results.

Pre-reqs: Python 3.x and requests library
Last modified: July 2017
By: Dave Bunten

License: MIT - see license.txt
"""

import os
import sys
import logging
import json
import time
import math
import csv
import datetime
import zoom_web_api_client as zoom_web_api_client

if __name__ == "__main__":

    run_path = os.path.dirname(__file__)

    #log file datetime
    current_datetime_string = '{dt.month}-{dt.day}-{dt.year}_{dt.hour}-{dt.minute}-{dt.second}'.format(dt = datetime.datetime.now())
    logfile_path = run_path+'/logs/zoom_api_example_'+current_datetime_string+'.log'

    #logger for log file
    logging_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging_datefmt = '%m/%d/%Y - %I:%M:%S %p'
    logging.basicConfig(filename=logfile_path,
        filemode='w',
        format=logging_format,
        datefmt=logging_datefmt,
        level=logging.INFO
        )

    #logger for console
    console = logging.StreamHandler()
    formatter = logging.Formatter(logging_format,
    datefmt=logging_datefmt)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

    #open config file with api key/secret information
    api_config_file = open(run_path+"/"+".zoom_api_config")
    api_config_data = json.load(api_config_file)

    #gathering destination filepath input
    input_report_destination = input("Enter report destination filepath: ")

    #create zoom client
    client = zoom_web_api_client.client(
        api_config_data["root_request_url"],
        api_config_data["api_key"],
        api_config_data["api_secret"],
        api_config_data["data_type"]
        )

    #gather date strings for request
    last_day_of_previous_month = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    last_month_number = last_day_of_previous_month.strftime("%m").lstrip("0")
    current_year = last_day_of_previous_month.strftime("%Y")

   #list of keys we're interested in from the return data
    keys = ["date",
        "new_user",
        "meetings",
        "participants",
        "meeting_minutes"
        ]

    #list of keys we will need to find sums on
    sum_keys = ["new_user",
        "meetings",
        "participants",
        "meeting_minutes"
        ]

    #for storing our results
    daily_results = []

    #make the Zoom api request and parse the result for the data we need
    result = client.do_request("report/getdailyreport", {"year":current_year,"month":last_month_number})
    result_json = json.loads(result)
    daily_results = result_json["dates"]

    logging.info("Daily object rows: "+str(len(daily_results)))

    #final result data by row
    write_list = []

    #loop through the result users listing
    for user_data in daily_results:
            row = {}
            #for each key, only keep those which are in keys list above
            for key,value in user_data.items():
                if key in keys:
                    row[key] = value
            write_list.append(row)

    #determine sums row
    sum = {}
    for row_data in write_list:
        for key,value in row_data.items():
            if key in sum_keys:
                if key in sum:
                    sum[key] += int(value)
                else:
                    sum[key] = int(value)
            elif key == "date":
                sum[key] = "totals"

    #add the sums to the write_list
    write_list.append(sum)

    #create filename for report
    download_filename = input_report_destination.rstrip('/')+'/zoom_'+current_year+'-'+last_month_number+'.csv'

    #write output as a csv
    with open(download_filename, 'w', newline='') as fp:
        a = csv.DictWriter(fp, delimiter=',',fieldnames=keys, restval='',extrasaction='ignore')
        a.writeheader()
        a.writerows(write_list)

    logging.info("Finished creating Zoom stats file: "+download_filename)
    logging.info("Example finished!")
