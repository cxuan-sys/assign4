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
    st.markdown('<div class="flash-banner">Built by YOUR NAME HERE</div>',
                unsafe_allow_html=True)

    st.write(f"**Current time:** {datetime.now().strftime('%A, %B %d, %Y  %I:%M:%S %p')}")

    df = pd.read_csv("msft.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    df["Daily Return %"] = df["Close"].pct_change() * 100

    st.subheader("Distribution of MSFT Daily Returns")
    fig, ax = plt.subplots()
    ax.hist(df["Daily Return %"].dropna(), bins=50, color="red", edgecolor="black")
    ax.set_xlabel("Daily return (%)")
    ax.set_ylabel("Number of days")
    ax.axvline(0, color="black", linestyle="--")
    st.pyplot(fig)
