# importing libraries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# sidebar menu option
st.sidebar.markdown("# Home")
st.markdown("<h1 style='text-align: center; color: red;'>Car Insurance Claim Prediction</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 6, 1])  # to center the image using 3 columns
# col1
with col1:
    st.write("")
# col2
with col2:
    st.image("car_insurance.png", width=850)
with col3:
    st.write("")

# loading the dataset
df = pd.read_csv('car_insurance_claim_ds.csv')
st.header("Tabular Data")
st.write('Displaying first 10 rows of the dataset.')
st.table(df.head(10))
st.header("Dataset Statistical Summary")
st.table(df.describe().T)

# Correlation map using seaborn
st.header("Correlation Graph")
fig = plt.figure(figsize=(40, 20))
sns.heatmap(df.corr(), annot=True, fmt=".3f")
st.pyplot(fig)

# Graphic representation of dataset
st.header('Visualization of dataset')
fig = plt.figure(figsize=(15, 15))
plt.subplot(3, 3, 1)
sns.scatterplot(x='age_of_car', y='age_of_policyholder', hue="fuel_type", data=df)
plt.subplot(3, 3, 2)
sns.scatterplot(x="age_of_car", y="age_of_policyholder", hue="is_claim", data=df)
plt.subplot(3, 3, 3)
sns.boxplot(x="policy_tenure", data=df)
plt.subplot(3, 3, 4)
sns.violinplot(x="fuel_type", y="width", hue="is_claim", data=df)
plt.subplot(3, 3, 5)
sns.barplot(x="is_parking_sensors", y="is_brake_assist", hue="cylinder", data=df)
plt.subplot(3, 3, 6)
sns.barplot(x="is_central_locking", y="is_speed_alert", hue="fuel_type", data=df)
st.pyplot(fig)


# ad_hpt = joblib.load("car_insurance_claim_model.sav")

