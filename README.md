# Traffic.py

This application launches a Streamlit dashboard to explore hourly westbound traffic measurements from I94 between Minneapolis
and St. Paul from Oct-2012 to Oct-2018.

_hosted by Streamlit.io at_<br>
<url=weblink-here>


---

## Data Source:

**Metro_Interstate_Traffic_Volume.csv from:**<br>
https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume# <br/>
**original data source:**<br>
Traffic data from MN Department of Transportation<br>
Weather data from OpenWeatherMap

---

## Data Feature Information:

- __holiday:__ _Categorical_ US National holidays plus regional holiday, Minnesota State Fair <br>
__temp:__ _Numeric_ Average temp in kelvin <br>
__rain_1h:__ _Numeric_ Amount in mm of rain that occurred in the hour <br>
__snow_1h:__ _Numeric_ Amount in mm of snow that occurred in the hour <br>
__clouds_all:__ _Numeric_ Percentage of cloud cover <br>
__weather_main:__ _Categorical_ Short textual description of the current weather <br>
__weather_description:__ _Categorical_ Longer textual description of the current weather <br>
__date_time:__ _DateTime_ Hour of the data collected in local CST time <br>
__traffic_volume:__ _Numeric_ Hourly I-94 ATR 301 reported westbound traffic volume <br>



---

## To Run:

    - streamlit run Traffic.py

---

## Requirements:

    - python 3.9
    - streamlit
    - pandas
    - plotly

---

## Data Preparation:
    
    - All Data was comma delimited
