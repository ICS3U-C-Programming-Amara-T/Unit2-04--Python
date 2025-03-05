#!/usr/bin/env python3

# Created By: Amara Tie

# Date: Month March 5, 2025

# Calculating the surface area and perimeter of a circle.
import math


def main():
    # Get Radius
    radius = float(input("Enter the radius of the circle (mn): "))

    # Calculate the area and perimeter
    Area = math.pi * radius**2
    perimeter = math.pi * radius * 2

    # Display the volume and surface area
    print("")
    print("Area = {} mn^2".format(Area))
    print("Perimeter = {} mn^2".format(perimeter))


if __name__ == "__main__":
    main()
