import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    # Set the title of application
    st.title("This is stramlit app  data insights.")
    st.sidebar.title("Data Insights")

    uploaded_file = st.sidebar.file_uploader("Upload your file.",type = ['csv','xlsx'])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv('uploaded_file')
                st.sidebar.success("File uploaded successfully.")
            else:
                data = pd.read_excel(uploaded_file)
                st.sidebar.success("File uploaded successfully.")

            st.subheader("Data Overview")
            st.dataframe(data.head())

            st.subheader("Basic Information about file.")
            st.write("Shape of data:",data.shape)
            st.write("Columns in data:",data.columns.tolist())
            st.write("data types of columns:",data.dtypes)

            st.subheader("Statistical Summary")
            st.write(data.describe())

            st.subheader("Missing Values")
            st.write(data.isnull().sum())

           
           

        except Exception as e:
            st.sidebar.error(f"Error reading file: {e}")
    else:
        st.sidebar.info("Please upload a CSV or Excel file.")


if __name__ == "__main__":
    main()
