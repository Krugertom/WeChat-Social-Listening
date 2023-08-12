This script retrieves article data from specific WeChat accounts using the Newrank API and exports the data to a CSV file.

## Dependencies:
requests
pandas
json
numpy

## Prerequisites:
You need to have an API Key from Newrank, which you can get from your personal account details on the Newrank website.
You should have the WeChat account ID, available on the account profile page in Weixin, for the brands you wish to retrieve data for.
Make sure to install the required dependencies using pip:
bash

~~~
pip install requests pandas numpy
~~~

## Setup:
Replace NEWRANK ACCOUNT KEY in the headers dictionary with your actual Newrank API key.
Replace WECHAT ACCOUNT ID in the brand_name variable with the WeChat account ID of the brand(s) you're interested in. You can add multiple account IDs separated by commas.
Specify the date range for which you want to retrieve the data. The format should be YYYY-MM-DD 00:00:00. Multiple date ranges are allowed but the maximum length for one date range is one month.
Replace SPECIFIED PATH with the desired path where you'd like to save the CSV file containing the article data.
Execution:
Run the script:


~~~
python3 script_name.py
~~~

The script will loop through each WeChat account ID and each date range specified, make requests to the Newrank API to retrieve article data, and then concatenate all results and save them to a CSV file.

## Notes:
Ensure that the API key and WeChat account ID are kept confidential and not exposed in any public repository.
Check for any rate limits or restrictions imposed by the Newrank API to avoid getting blocked or incurring extra costs.
The default page and size for each API request are set to 1 and 20 respectively. Adjust these values if necessary.

## Disclaimer:
This script and guide are for educational purposes. Always refer to Newrank's official documentation and ensure that you are compliant with their terms of service.
