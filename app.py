import streamlit as st
import pandas as pd
import folium

def load_data(csv_url):
    data = pd.read_csv(csv_url)
    return data

def create_map(data):
    # Create a map centered around the mean coordinates
    map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
    my_map = folium.Map(location=map_center, zoom_start=10)

    # Add markers for each coordinate
    for _, row in data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name']  # Change 'Name' to the column name containing the marker label
        ).add_to(my_map)

    return my_map

def main():
    st.title("CSV Map Viewer")
    st.sidebar.header("Options")

    # Specify the URL of the CSV file on GitHub
    csv_url = 'https://raw.githubusercontent.com/ChisholmLegacyProject/Coop/main/coops.csv'

    data = load_data(csv_url)
    st.dataframe(data)  # Display the CSV data

    # Check if 'Latitude' and 'Longitude' columns exist
    if 'Latitude' in data.columns and 'Longitude' in data.columns:
        my_map = create_map(data)
        folium_static(my_map)  # Display the map
    else:
        st.error("The CSV file should contain 'Latitude' and 'Longitude' columns.")
