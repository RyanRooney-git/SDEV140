"""
Author:  Ryan Rooney
Date written: 6/9/2025
Assignment:   Module 1 exercise 2 part 2
Short Desc:   This program should take the length of an edge as input 
and prints the cube’s surface area as output.

It should accomplish this by doing the following steps:
1. Input intCubeEdge
2. Calculate the surface area of the cube
3. Print the cube's calculated surface area

"""
intCubeEdge = int(input("Length of cube edge: ")) # user input for length of cube edge
surfaceArea = 6*intCubeEdge**2 # surface area calculation
print(f'Total surface area: {surfaceArea}.') # prints the surface area to the user