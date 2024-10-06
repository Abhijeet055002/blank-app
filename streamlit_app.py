import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
file_path = r"C:\Users\ABHIJEET\OneDrive\Fore\Trimester 1\Python\Project-2\Imports_Exports_Dataset.csv"
df = pd.read_csv(file_path)

# Sidebar: User selects country
st.sidebar.title("Country Filter")
countries = df['Country'].unique().tolist()
selected_country = st.sidebar.selectbox("Select a Country", options=["All"] + countries)

# Filter dataset based on selected country
if selected_country != "All":
    df = df[df['Country'] == selected_country]

# Sidebar: User selects the type of visualization
st.sidebar.title("Visualization Options")
visualization_type = st.sidebar.selectbox("Select the Visualization", 
    options=["Shipping Method vs Weight", "Date vs Value", "Date vs Quantity", 
             "Shipping Method vs Payment Terms", "Payment Terms vs Value"])

# Visualization 1: Shipping Method vs Weight
if visualization_type == "Shipping Method vs Weight":
    st.title("Shipping Method vs Weight")
    shipping_method_weight = df.groupby('Shipping_Method')['Weight'].sum().reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Weight', y='Shipping_Method', data=shipping_method_weight, palette='viridis')
    plt.title('Shipping Method vs Total Weight')
    plt.xlabel('Total Weight')
    plt.ylabel('Shipping Method')
    st.pyplot(plt)

# Convert the 'Date' column to datetime format (handle errors by coercing invalid dates to NaT)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with NaT in the 'Date' column
df = df.dropna(subset=['Date'])

# Visualization 2: Date vs Value
if visualization_type == "Date vs Value":
    st.title("Date vs Value")
    date_value = df.groupby(df['Date'].dt.date)['Value'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Date', y='Value', data=date_value, marker='o', color='blue')
    plt.title('Date vs Total Value')
    plt.xlabel('Date')
    plt.ylabel('Total Value')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Visualization 3: Date vs Quantity
elif visualization_type == "Date vs Quantity":
    st.title("Date vs Quantity")
    date_quantity = df.groupby(df['Date'].dt.date)['Quantity'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Date', y='Quantity', data=date_quantity, marker='o', color='green')
    plt.title('Date vs Total Quantity')
    plt.xlabel('Date')
    plt.ylabel('Total Quantity')
    plt.xticks(rotation=45)
    st.pyplot(plt)


# Visualization 4: Shipping Method vs Payment Terms
elif visualization_type == "Shipping Method vs Payment Terms":
    st.title("Shipping Method vs Payment Terms")
    shipping_payment = df.groupby(['Shipping_Method', 'Payment_Terms']).size().reset_index(name='Count')

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Shipping_Method', y='Count', hue='Payment_Terms', data=shipping_payment, palette='coolwarm')
    plt.title('Shipping Method vs Payment Terms')
    plt.xlabel('Shipping Method')
    plt.ylabel('Count')
    st.pyplot(plt)

# Visualization 5: Payment Terms vs Value
elif visualization_type == "Payment Terms vs Value":
    st.title("Payment Terms vs Value")
    payment_value = df.groupby('Payment_Terms')['Value'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Value', y='Payment_Terms', data=payment_value, palette='magma')
    plt.title('Payment Terms vs Total Value')
    plt.xlabel('Total Value')
    plt.ylabel('Payment Terms')
    st.pyplot(plt)

# Footer
st.sidebar.write("Use the dropdown menus to explore different visualizations and filter by country.")
