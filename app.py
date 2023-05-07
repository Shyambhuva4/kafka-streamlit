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

df_response = pd.read_csv(BytesIO(serialized_df_response.encode()))


df_response.set_index("ts", inplace=True)
devices=df_response["device"].unique().tolist()
if bruh==True:
 finallist = st.selectbox("Our Choices",devices)

filtered_df = df_response[df_response["device"] == finallist]

bruh2 = st.checkbox("Fasinates")
if bruh2:
     st.line_chart(filtered_df[["co"]].tail(100))
     st.write("maximum value of CO emission is :"+ str(max(filtered_df["co"])))
     st.line_chart(filtered_df[["humidity"]].tail(100))
     st.write("maximum humidity is :"+ str(max(filtered_df["humidity"])))
     st.line_chart(filtered_df[["lpg"]].tail(100))
     st.write("maximum lpg is :"+ str(max(filtered_df["lpg"])))
     st.line_chart(filtered_df[["smoke"]].tail(100))
     st.write("maximum value of smoke emission is :"+ str(max(filtered_df["smoke"])))
     st.line_chart(filtered_df[["temp"]].tail(100))
     st.write("maximum value of temperature is :"+ str(max(filtered_df["temp"])))
