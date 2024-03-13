import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data using the updated caching mechanism
@st.cache_data
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/belajarcarabelajar/data-analisis-bcbacademy/master/dashboard/all_data.csv')

    return data

data = load_data()

# Set visualization styles
sns.set(style="whitegrid")

# Visualization 1: Distribution of Orders by Province
st.subheader('Distribution of Orders by Province')
order_counts = data['Provinsi'].value_counts()
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=order_counts.index, y=order_counts.values, palette="viridis", ax=ax)
plt.xticks(rotation=45, ha="right")
plt.xlabel('Province')
plt.ylabel('Number of Orders')
st.pyplot(fig)

# Convert 'Total' to numeric, errors='coerce' will set invalid parsing to NaN
data['Total'] = pd.to_numeric(data['Total'], errors='coerce')

# Visualization 3: Order Total Distribution
st.subheader('Distribution of Order Totals')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data['Total'], bins=30, kde=True, color='blue', ax=ax)
plt.xlabel('Order Total')
plt.ylabel('Frequency')
st.pyplot(fig)

# Convert 'Waktu Dibuat' to datetime
data['Waktu Dibuat'] = pd.to_datetime(data['Waktu Dibuat'], errors='coerce', dayfirst=True)

# Set 'Waktu Dibuat' as the index
data_time_series = data.set_index('Waktu Dibuat')

# Resample data to weekly counts of orders
weekly_orders = data_time_series.resample('W').size()

# Visualization 4: Time Series of Orders
st.subheader('Weekly Trend of Orders')
fig, ax = plt.subplots(figsize=(12, 6))
weekly_orders.plot(color='green', ax=ax)
plt.xlabel('Week')
plt.ylabel('Number of Orders')
st.pyplot(fig)

# Get the top 5 payment methods
top_5_payment_methods = data['Pembayaran dari Bank'].value_counts().head(5)

# Visualization 2: Top 5 Payment Method Distribution
st.subheader('Top 5 Payment Method Distribution')
fig, ax = plt.subplots(figsize=(8, 8))
plt.pie(top_5_payment_methods, labels=top_5_payment_methods.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("viridis", len(top_5_payment_methods)))
st.pyplot(fig)

# Menghitung jumlah order untuk setiap produk
product_counts = data['Nama Produk'].value_counts()

# Visualization: Distribusi Persentase Produk Paling Banyak Diminati
st.subheader('Distribusi Persentase Produk Paling Banyak Diminati')
fig, ax = plt.subplots(figsize=(10, 8))
plt.pie(product_counts, labels=product_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("viridis", len(product_counts)))
st.pyplot(fig)

# Mengambil 5 URL teratas berdasarkan frekuensi
top_5_urls = data['URL Landasan'].value_counts().head(5)

# Visualization: Top 5 URL Landasan Berdasarkan Frekuensi
st.subheader('Top 5 URL Landasan Berdasarkan Frekuensi')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_5_urls.index, y=top_5_urls.values, palette="viridis", ax=ax)
plt.xticks(rotation=45)
plt.xlabel('URL Landasan')
plt.ylabel('Frekuensi')
st.pyplot(fig)

st.caption('Copyright © Iwan Kurniawan 2024')
