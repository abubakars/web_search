import streamlit as st
import geopandas as gpd

# Title
st.title("🗺️ Niger State Settlement Locations")

# Function to load and filter data
@st.cache_data
def load_data():
    # Load all settlement points in Nigeria (GeoJSON)
    url_settlements = "https://bulk.openafrica.net/dataset/nigerian-settlement-points.geojson"
    settlements = gpd.read_file(url_settlements)

    # Load Niger State boundary (you'll need a correct GeoJSON link)
    url_niger_boundary = "https://your_url_to_niger_state_boundary.geojson"
    niger_boundary = gpd.read_file(url_niger_boundary)

    # Match coordinate reference systems
    settlements = settlements.to_crs(niger_boundary.crs)

    # Spatial join to get settlements within Niger State
    niger_settlements = gpd.sjoin(settlements, niger_boundary, predicate="within")

    return niger_settlements

# Load and show map
settlements_in_niger = load_data()
st.write(f"Total settlements in Niger State: {len(settlements_in_niger)}")

# Display map
st.map(settlements_in_niger[['geometry']], use_container_width=True)
