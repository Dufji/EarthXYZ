import math

EARTH_RADIUS = 6378137 # meters

def gps_to_mc_coords(lat, lon, elevation, scale=1):
    x = lon * (math.pi / 180) * EARTH_RADIUS / scale
    z = math.log(math.tan((math.pi / 4) + (math.radians(lat) / 2))) * EARTH_RADIUS / scale
    y = elevation / scale
    return x, y, z

def mc_coords_to_gps(x, y, z, scale=1):
    lon = (x * scale) / (EARTH_RADIUS * (math.pi / 180))
    lat = 2 * math.atan(math.exp((z * scale) / EARTH_RADIUS)) - (math.pi / 2)
    elevation = y * scale
    return math.degrees(lat), lon, elevation

def main():
    print("Choose an option:")
    print("1. Convert GPS to Minecraft coordinates")
    print("2. Convert Minecraft to GPS coordinates")
    option = input("Enter 1 or 2: ")

    if option == "1":
        lat = float(input("Enter latitude (decimal degrees): "))
        lon = float(input("Enter longitude (decimal degrees): "))
        elevation = float(input("Enter elevation (meters): "))
        scale = float(input("Enter scale (default is 1, 1 block = 1 meter): ") or 1)
        x, y, z = gps_to_mc_coords(lat, lon, elevation, scale)
        print(f"Minecraft coordinates: X={x:.2f}, Y={y:.2f}, Z={z:.2f}")

    elif option == "2":
        x = float(input("Enter Minecraft X coordinate: "))
        y = float(input("Enter Minecraft Y coordinate: "))
        z = float(input("Enter Minecraft Z coordinate: "))
        scale = float(input("Enter scale (default is 1, 1 block = 1 meter): ") or 1)
        lat, lon, elevation = mc_coords_to_gps(x, y, z, scale)
        print(f"Real-world GPS coordinates: Latitude={lat:.6f}, Longitude={lon:.6f}, Elevation={elevation:.2f}")

    else:
        print("Invalid option. Please run the program again.")

if __name__ == "__main__":
    main()

