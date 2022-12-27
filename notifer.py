import datetime
import time
import requests
from plyer import notification

# initializing a variable with None (temporary)
# indicating that there is no data available currently
covidStats = None
try:
    covidStats = requests.get(
        "https://api.covidtracking.com/v1/us/current.json")
except:
    # data is not fetched because of internet connection
    print("Consider checking the internet connection")

print(covidStats.json())
# in case data is fetched
if (covidStats != None):
    # converting data into json
    jsonData = covidStats.json()

    while (True):
        notification.notify(
            title="COVID19 Stats on {}".format(
                jsonData[0]['date']),

            # defining the message of notification
            message="Positive cases: {totalcase} \n Negative Cases:{todaycases}\n Total Death:{todaydeath}\n".format(
                totalcase=jsonData[0]['positive'],
                todaycases=jsonData[0]['negative'],
                todaydeath=jsonData[0]['death']
            ),
            timeout=30,
            app_icon='3677my.ico'
        )

        time.sleep(60*60*12)
