# Zoom API Example

This repository is intended to provide an example of using the Zoom API with Python. This example will take input from the user on a local destination filepath, execute a Zoom API request for daily analytics data from last month, then create a CSV report of that data in the provided destination filepath.

## Prerequisites and Documentation

Before you get started, make sure to install or create the following prerequisites:

* Python 3.x: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Python Requests Library (non-native library used for HTTP requests): [http://docs.python-requests.org/en/master/](http://docs.python-requests.org/en/master/)
* Enable Zoom API key: [https://zoom.us/developer/api/credential](https://zoom.us/developer/api/credential)

Zoom API documentation can be found at the following URL: [https://zoom.github.io/api/](https://zoom.github.io/api/)

## File Descriptions

- **zoom_web_api_client.py**
A web api client used to connect to the system. This is Python class file used for making connections to the Zoom system.

- **.zoom_api_config_sample**
A file which uses JSON to store credentials used by the zoom_web_api_client.py Python class for making web API connections to Zoom. The file as it stands in this repository is a template and must be modified to be named ".zoom_api_config" and filled in with your site-specific information.

- **zoom_api_example.py**
A file which makes use of the  zoom_web_api_client.py Python class for making web API connections to Zoom. This example will take input from the user on a local destination filepath, execute a Zoom API request for daily analytics data from last month, then create a CSV report of that data in the provided destination filepath.

## Usage

1. Ensure prerequisites outlined above are completed.
2. Fill in necessary &lt;bracketed&gt; areas in .zoom_api_config_sample specific to your account
2. Rename .zoom_api_config_sample to  .zoom_api_config (removing the text "_sample")
3. Run zoom_api_example.py with Python 3.x

### Sample Usage

    C:\Users\dabu5788.OIT-ETS-D-001>python C:\zoom_api_example\zoom_api_example.py
    Enter report destination filepath: C:\
    07/13/2017 - 12:29:58 PM - INFO - Starting new HTTPS connection (1): api.zoom.us
    07/13/2017 - 12:29:58 PM - INFO - Daily object rows: 30
    07/13/2017 - 12:29:58 PM - INFO - Finished creating Zoom stats file: C:\zoom_2017-6.csv
    07/13/2017 - 12:29:58 PM - INFO - Example finished!

## License
MIT - See license.txt
