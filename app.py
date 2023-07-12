import streamlit as st
import pandas as pd

def load_data(csv_url):
    data = pd.read_csv(csv_url)
    return data

def main():
    st.title("CSV Map Viewer")
    st.sidebar.header("Options")

    # Specify the URL of the CSV file on GitHub
    csv_url = 'https://raw.githubusercontent.com/ChisholmLegacyProject/Coop/main/coops.csv'

    data = load_data(csv_url)
    st.dataframe(data)  # Display the CSV data

    # Check if 'Latitude' and 'Longitude' columns exist
    if 'Latitude' in data.columns and 'Longitude' in data.columns:
        # Filter out rows with missing latitude or longitude values
        filtered_data = data.dropna(subset=['Latitude', 'Longitude'])
        
        # Display the map
        st.map(filtered_data)
    else:
        st.error("The CSV file should contain 'Latitude' and 'Longitude' columns.")

if __name__ == '__main__':
    main()
