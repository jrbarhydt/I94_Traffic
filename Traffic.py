# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# ======================================================================================================================
# Functions
# ----------------------------------------------------------------------------------------------------------------------

def df_queried_an_grouped(dataframe, temp_range, rain_range, snow_range):
    new_df = dataframe.query(f"{snow_range[0]} <= snow_1h <= {snow_range[1]}")
    new_df = new_df.query(f"{temp_range[0]} <= temp_f <= {temp_range[1]}")
    new_df = new_df.query(f"{rain_range[0]} <= rain_1h <= {rain_range[1]}")
    new_df = new_df.groupby([new_df.date_time.dt.hour]).mean()
    return new_df


# ======================================================================================================================
# Initialization
# ----------------------------------------------------------------------------------------------------------------------
data_filepath = "Metro_Interstate_Traffic_Volume.csv"

# init dataframe
df = pd.read_csv(data_filepath)
df["date_time"] = pd.to_datetime(df["date_time"], infer_datetime_format=True)
# convert K to Fahrenheit
mean_temp = ((9/5)*(df.temp.mean()-273.15)+32)
df["temp_f"] = df.temp.apply(lambda kelvin: mean_temp if kelvin == 0.0 else (9/5)*(kelvin-273.15)+32)
# clean up outliers
mean_rain = df.rain_1h.mean()
std = df.rain_1h.std()
df["rain_1h"] = df.rain_1h.apply(lambda rain: mean_rain if rain > 5*std else rain)

# ======================================================================================================================
# Streamlit Generation
# ----------------------------------------------------------------------------------------------------------------------

# generate title
st.title("I-94 Traffic Explorer")

# generate sidebar
with st.sidebar:
    # init sidebar
    st.title("Select filters/sliders")
    st.markdown("_Compare two sets of conditions to see how they affect traffic._")

    st.markdown("---")
    st.header("Blue Conditions")
    a_temp = st.slider("Temperature [°F]",
                       min_value=int(df.temp_f.min()),
                       max_value=int(df.temp_f.max()),
                       value=(-21, 35),
                       key=11)
    col_a = st.columns(2)
    with col_a[0]:
        a_snow = st.slider("Hourly Snowfall [mm]",
                           max_value=float(df.snow_1h.max()),
                           value=(0.06, 0.46),
                           key=12)
    with col_a[1]:
        a_rain = st.slider("Hourly Rainfall [mm]",
                           max_value=float(df.rain_1h.max()),
                           value=(0.0, float(df.rain_1h.max())),
                           key=13)

    st.markdown("---")
    st.header("Red Conditions")
    b_temp = st.slider("Temperature [°F]",
                       min_value=int(df.temp_f.min()),
                       max_value=int(df.temp_f.max()),
                       value=(80, 98),
                       key=21)
    col_b = st.columns(2)
    with col_b[0]:
        b_snow = st.slider("Hourly Snowfall [mm]",
                           max_value=float(df.snow_1h.max()),
                           value=(0.0, 0.46),
                           key=22)
    with col_b[1]:
        b_rain = st.slider("Hourly Rainfall [mm]",
                           max_value=float(df.rain_1h.max()),
                           value=(0.0, float(df.rain_1h.max())),
                           key=23)
# generate queried dataframes
df_hr_a = df_queried_an_grouped(df, a_temp, a_rain, a_snow)
df_hr_b = df_queried_an_grouped(df, b_temp, b_rain, b_snow)
# plot results
fig = go.Figure()
hr_12h_fmt = [str(hr+12)+"AM" if hr == 0 else str(hr)+"PM" if hr == 12 else str(hr)+"AM" if hr < 12 else str(hr-12)+"PM" for hr in df_hr_a.index]
fig.add_trace(go.Scatter(x=hr_12h_fmt, y=df_hr_a["traffic_volume"], mode="lines+markers", fill="tozeroy", name="Blue"))
fig.add_trace(go.Scatter(x=hr_12h_fmt, y=df_hr_b["traffic_volume"], mode="lines+markers", fill="tozeroy", name="Red"))
fig.update_layout(xaxis_title="Time of Day [H AM/PM]", yaxis_title="Average Traffic Volume")
st.plotly_chart(fig, use_container_width=True)

# link to other pages
footer = """<style>
               .footer {
               position: fixed;
               left: 0;
               bottom: 0;
               width: 100%;
               background-color: #262730;
               color: white;
               text-align: center;
               }
            </style>
            <div class="footer">
               <a href="https://jrbarhydt-guitarfingering-guitarfingering-zljmbo.streamlitapp.com/">Guitar Chord Explorer</a>
               &nbsp;&nbsp;&nbsp;
               <a href="https://jrbarhydt-raisinexplorer-raisins-c3z4pe.streamlitapp.com/">Raisin Explorer</a>
               &nbsp;&nbsp;&nbsp;
               <a href="https://jrbarhydt-i94-traffic-traffic-sespds.streamlitapp.com/">I-94 Traffic Explorer</a>
            </div>
        """
st.markdown(footer, unsafe_allow_html=True)
