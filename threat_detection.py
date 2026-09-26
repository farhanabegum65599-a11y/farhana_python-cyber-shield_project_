import pandas as pd
import numpy as np

def load_data():
    data=pd.read_csv("cyber_threat_data.csv")
    return data

def detect_threats():
    data = load_data()
    packet_score = np.clip(data["Packet_Count"] / 1600*50,0,50)
    login_score = np.clip(data["Failed_Login"] / 35*50,0,50)
    data["Threat_Score"] = packet_score + login_score 
    data["Risk_Level"] = np.where(data["Threat_Score"] >= 70,"HIGH",
    np.where(data["Threat_Score"] >= 40,"MEDIUM","LOW"))
    return data
def get_summary(data):

    high = np.sum(data["Risk_Level"] == "HIGH")
    medium = np.sum(data["Risk_Level"] == "MEDIUM")
    low = np.sum(data["Risk_level"] == "LOW")
    return high,medium,low

   
