from geopy.geocoders import Nominatim
import folium
from fpdf import FPDF
import io
from PIL import Image

def generate_map_pdf(address, output_pdf):
    # Initialize the geolocator
    geolocator = Nominatim(user_agent="map_pdf_generator")
    
    # Geocode the address
    location = geolocator.geocode(address)
    if not location:
        print("Address not found.")
        return
    
    latitude, longitude = location.latitude, location.longitude
    
    # Generate the map with Folium
    folium_map = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude], popup=address).add_to(folium_map)
    
    # Save the map to an HTML file and render it as an image
    map_data = folium_map._to_png(5)  # Render the map with a high resolution
    map_image = Image.open(io.BytesIO(map_data))
    
    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Add title to the PDF
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Location Map for: {address}", ln=True, align='C')
    
    # Save map image to a temporary file
    map_image_path = "temp_map.png"
    map_image.save(map_image_path)
    
    # Add the map image to the PDF
    pdf.image(map_image_path, x=10, y=30, w=190)  # Adjust position and width as needed
    
    # Save the PDF
    pdf.output(output_pdf)
    print(f"PDF saved as {output_pdf}")

# Example usage
user_address = "1600 Amphitheatre Parkway, Mountain View, CA"
output_pdf_file = "map_output.pdf"
generate_map_pdf(user_address, output_pdf_file)
