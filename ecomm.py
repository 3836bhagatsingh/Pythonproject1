

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    # Set the title of application
    st.title("📊 Streamlit App for Data Insights")
    st.sidebar.title("Upload and Explore Your Dataset")

    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        try:
            # Detect file type and read accordingly
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)  # removed quotes
            else:
                data = pd.read_excel(uploaded_file)

            st.sidebar.success("✅ File uploaded successfully!")

            # Display data overview
            st.subheader("🔍 Data Preview")
            st.dataframe(data.head())

            # Basic info
            st.subheader("📋 Dataset Info")
            st.write("**Shape of data:**", data.shape)
            st.write("**Columns:**", data.columns.tolist())
            st.write("**Data types:**")
            st.write(data.dtypes)

            # Statistical Summary
            st.subheader("📈 Statistical Summary")
            st.write(data.describe())

            # Missing values
            st.subheader("❗ Missing Values")
            st.write(data.isnull().sum())

        except Exception as e:
            st.sidebar.error(f"❌ Error reading file: {e}")
    else:
        st.sidebar.info("📁 Please upload a CSV or Excel file.")

if __name__ == "__main__":
    main()

