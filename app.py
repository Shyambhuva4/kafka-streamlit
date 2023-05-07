import streamlit as st
import matplotlib
import numpy as np 
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json
import pandas as pd
from io import BytesIO
import time 

st.title("Time series Visualizer")

    
st.text("Let us help you with data ☺")



##### IMPLEMENTING Visualizer ######

def print_on_site():
     try:
      consumer = KafkaConsumer(
        "ts-analysis",
        bootstrap_servers="localhost:9093",
        value_deserializer=lambda x: json.loads(x.decode()),
    )
     except:
          return 0
     return consumer

bruh = st.checkbox("Choose your Device")

consumer = print_on_site()
serialized_df_response = next(consumer).value

        # Convert the serialized DataFrame back to a Pandas DataFrame
df_response = pd.read_csv(BytesIO(serialized_df_response.encode()))


# Display the values of the row horizontally in Streamlit

# df_response["ts"] = pd.to_datetime(df_response["ts"], unit="s")

# Set the timestamp column as the index of the DataFrame
df_response.set_index("ts", inplace=True)
devices=df_response["device"].unique().tolist()
if bruh==True:
 finallist = st.selectbox("Our Choices",devices)

# Resample the data to a fixed frequency (e.g. every 5 minutes) and forward fill missing values
filtered_df = df_response[df_response["device"] == finallist]

bruh2 = st.checkbox("Fasinates")
if bruh2:
# Plot the "co", "humidity", and "temp" columns for the selected device using Streamlit's line_chart function
     st.line_chart(filtered_df[["co"]].tail(100))
     st.line_chart(filtered_df[["humidity"]].tail(100))
     st.line_chart(filtered_df[["lpg"]].tail(100))
     st.line_chart(filtered_df[["smoke"]].tail(100))
     st.line_chart(filtered_df[["temp"]].tail(100))
# Plot the data using Streamlit's line_chart function

# for device, group in grouped_df:
#     st.line_chart(group["co"].tail(100))
#     st.line_chart(group['humidity'].tail(100))
#     st.line_chart(group['lpg'].tail(100))
#     st.line_chart(group['smoke'].tail(100))
#     st.line_chart(group['temp'].tail(100))

