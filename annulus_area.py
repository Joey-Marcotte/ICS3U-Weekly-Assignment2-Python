#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: September 2019
# This program calculates the surface area of an annulus


import math


def main():
    # this function calculates area of an annulus

    # input
    outer_radius = int(input("Enter Outer Radius of Annulus (R) in cm: "))
    inner_radius = int(input("Enter Inner Radius of Annulus (r) in cm: "))

    # process
    area = math.pi*(outer_radius**2-inner_radius**2)

    # output
    print("")
    print("Area of Annulus is {:,.2f}cm".format(area))


if __name__ == "__main__":
    main()
