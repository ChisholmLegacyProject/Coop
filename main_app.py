import streamlit as st
import folium
from streamlit_folium import folium_static

def main():
    st.title("Interactive Map")
    st.sidebar.title("Map Configuration")

    # Sidebar options
    zoom_level = st.sidebar.slider("Zoom Level", 1, 18, 10)
    map_file = st.sidebar.file_uploader("https://raw.githubusercontent.com/ChisholmLegacyProject/Coop/main/map.html", type=["html"])

    if map_file is not None:
        # Read the uploaded HTML file
        map_html = map_file.read()

        # Create a Folium map object
        folium_map = folium.Map(location=[0, 0], zoom_start=zoom_level)

        # Render the HTML map in the Folium map object
        folium_map.get_root().html.add_child(folium.Element(map_html))

        # Render the Folium map object using folium_static
        folium_static(folium_map)

if __name__ == "__main__":
    main()
