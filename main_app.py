import streamlit as st
import requests
from streamlit_folium import folium_static
import folium

def main():
    st.title("Interactive Map")
    st.sidebar.title("Map Configuration")

    # Sidebar options
    zoom_level = st.sidebar.slider("Zoom Level", 1, 18, 10)
    github_url = st.sidebar.text_input("https://raw.githubusercontent.com/ChisholmLegacyProject/Coop/main/map.html")

    if github_url:
        # Fetch the HTML content from the GitHub URL
        response = requests.get(github_url)
        if response.status_code == 200:
            map_html = response.text

            # Create a Folium map object
            folium_map = folium.Map(location=[0, 0], zoom_start=zoom_level)

            # Render the HTML map in the Folium map object
            folium_map.get_root().html.add_child(folium.Element(map_html))

            # Render the Folium map object using folium_static
            folium_static(folium_map)
        else:
            st.error("Failed to fetch HTML file. Please make sure the URL is correct and accessible.")

if __name__ == "__main__":
    main()
