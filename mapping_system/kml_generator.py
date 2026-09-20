import os
import simplekml


def generate_larc_kml(
    animal_coordinates, source_coords, source_description, output_filename
):
    """Generates an AEAC-compliant KML file containing animal hotspot placemarks

    and a primary Source marker.
    """
    # Initialize the KML object
    kml = simplekml.Kml()

    # Add the detected animal hotspots
    for index, coords in enumerate(animal_coordinates):
        lat, lon = coords
        marker_name = f"Hotspot {index + 1}"

        # Create the placemark point in KML (SimpleKML uses (Longitude, Latitude))
        point = kml.newpoint(name=marker_name, coords=[(lon, lat)])

        # Customize icon style (Green Circle)
        point.style.iconstyle.icon.href = (
            "http://maps.google.com/mapfiles/kml/paddle/grn-circle.png"
        )
        print(f"Added {marker_name} at Coordinates: Lat: {lat:.6f}, Lon: {lon:.6f}")

    # Add the mandatory "Source" placemark
    source_lat, source_lon = source_coords
    source_point = kml.newpoint(
        name="Source", coords=[(source_lon, source_lat)]
    )
    source_point.description = source_description

    # Customize source icon style (Red Star)
    source_point.style.iconstyle.icon.href = (
        "http://maps.google.com/mapfiles/kml/paddle/red-stars.png"
    )
    print(
        f"Added 'Source' at Coordinates: Lat: {source_lat:.6f}, Lon: {source_lon:.6f}"
    )
    print(f"Source Description: '{source_description}'")

    # Save the file to disk
    kml.save(output_filename)
    print(f"\nSuccess! Compliant KML exported to {output_filename}")


if __name__ == "__main__":
    mock_animals = [
        (50.035210, -110.702500),
        (50.035840, -110.701950),
        (50.034980, -110.703800),
    ]
    mock_source = (50.036120, -110.701100)
    mock_description = (
        "Ungulate herd base nesting area - 12 adult deer sighted."
    )
    output_file = "LARC_Wildlife_Map_Test.kml"

    generate_larc_kml(mock_animals, mock_source, mock_description, output_file)