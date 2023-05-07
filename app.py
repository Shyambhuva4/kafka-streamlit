import streamlit as st
import matplotlib
import numpy as np 
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json
import pandas as pd
from io import BytesIO
import time 

st.title("Food Recommendation System")

    
st.text("Let us help you with food")



##### IMPLEMENTING RECOMMENDER ######

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


consumer = print_on_site()
serialized_df_response = next(consumer).value

        # Convert the serialized DataFrame back to a Pandas DataFrame
df_response = pd.read_csv(BytesIO(serialized_df_response.encode()))
row = df_response.iloc[0]

# Display the values of the row horizontally in Streamlit

table = pd.DataFrame(columns=df_response.columns)

# Display the empty table
st.table(table)
for i, row in df_response.iterrows():
    # Wait for 1 second to simulate streaming data
    time.sleep(1)

    # Append the row to the table
    table = table.append(row, ignore_index=True)

    # Display the updated table
    st.experimental_set_query_params(row=i)
    st.table(table)
