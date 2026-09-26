import streamlit as st
import pandas as pd

st.title(" 🛡️CYBERSHIELD")
st.subheader("Intelligent Cyber Threat Detection System")

#load cyber security dataset
data = pd.read_csv("cyber_data.csv")

st.write("### 📊 Cyber Security Dataset")
st.dataframe(data)

st.write("### 🔍 Threat Summary")

threat_count = data["threat"].value_counts()

st.bar_chart(threat_count)

st.success("CyberShield Dataset Loaded Successfully!  🛡️ ")

st.write("### 🛡️ Threat Detection")

packet_size = st.number_input("Packet Size", min_value=0)
connection_count = st.number_input("Connection Count", min_value=0)
failed_logins = st.number_input("Failed Logins", min_value=0)
port_scan = st.selectbox("Port Scan Detected?", [0,1])

if st.button("Detect Threat"):

    if failed_logins >=8 or connection_count >=60:
        result = "🔴 Attack"
    elif failed_logins >=2 or connection_count >=20 or port_scan == 1:
        result = "🟡 Suspicious"
    else:
        result = "🟢 Normal"
    st.subheader("Detection Result")
    st.success(result)

    st.write("###  📊 Security Dashboard")
    total = len(data)
    normal = (data["threat"] == "Normal").sum()
    suspicious = (data["threat"] == "Suspicious").sum()
    attack = (data["threat"] == "Attack").sum()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Records", total)
    col2.metric("🟢 Normal", normal)
    col3.metric("🟡 Suspicious", suspicious)
    col4.metric("🔴 Attack", attack)
