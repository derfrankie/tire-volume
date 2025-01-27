import math
import argparse

def calculate_tire_volume(diameter, width):
    """
    Calculate the approximate air volume of a tire based on its diameter and width.
    :param diameter: Inner diameter of the tire in mm (ETRTO first number).
    :param width: Width of the tire in mm (ETRTO second number).
    :return: Approximate air volume in liters.
    """
    # Convert diameter from mm to meters
    diameter_m = diameter / 1000
    
    # Assume the tire is a torus shape
    # Torus volume formula: V = 2 * π² * R * r²
    # R = diameter / 2 (radius of the torus centerline)
    # r = width / 2 (radius of the tire cross-section)
    R = diameter_m / 2
    r = width / 2000  # Convert width from mm to meters
    volume_m3 = 2 * (math.pi ** 2) * R * (r ** 2)
    
    # Convert cubic meters to liters (1 cubic meter = 1000 liters)
    volume_liters = volume_m3 * 1000
    return volume_liters

def main():
    parser = argparse.ArgumentParser(description="Calculate the air volume of a tire based on ETRTO dimensions.")
    parser.add_argument("tire_size", type=str, help="Tire size in ETRTO format (e.g., 622x45)")
    
    args = parser.parse_args()
    
    # Parse the tire size
    try:
        diameter, width = map(int, args.tire_size.lower().split('x'))
    except ValueError:
        print("Invalid tire size format. Use ETRTO format like 622x45.")
        return
    
    # Calculate the volume
    volume = calculate_tire_volume(diameter, width)
    print(f"Approximate air volume for tire {args.tire_size}: {volume:.2f} liters")

if __name__ == "__main__":
    main()