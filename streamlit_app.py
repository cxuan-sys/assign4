# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Christopher Xuan")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "new tab"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: Volume Chart
with tabs[3]:
   # Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Christopher Xuan")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository)
df = pd.read_csv("msft.csv")

# Black <-> red flashing for the 4th tab and its banner
st.markdown(
    """
    <style>
    @keyframes blackred {
        0%   { background-color: #000000; color: #ffffff; }
        50%  { background-color: #ff0000; color: #ffffff; }
        100% { background-color: #000000; color: #ffffff; }
    }
    button[data-baseweb="tab"]:nth-of-type(4) {
        animation: blackred 1.5s infinite;
        border-radius: 6px 6px 0 0;
    }
    .flash-banner {
        animation: blackred 1.5s infinite;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        font-size: 1.6rem;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "🔥 Returns"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader("Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader("Closing Price for MSFT")
    st.line_chart(df["Close"])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader("Volume for MSFT")
    st.bar_chart(df["Volume"])

# Tab 4: Name, current time, and histogram of daily returns
with tabs[3]:
    st.subheader("Built by Christopher Xuan")
    st.write("Welcome to my 4th tab!")
    st.area_chart(df["Close"])
