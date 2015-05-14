# Curviness

Calculates the curviness number of an animals path given it's location over time. Assuming the animal starts at the first point and ends at the last point. If the first and last point are the same, then it assumes the animal didn't move along the path.

Path points are inputted in a file in the form:

[{"x":"1", "y":"5", "t":"0"},
{"x":"1", "y":"9", "t":"5"},
{"x":"1", "y":"21", "t":"10"},
.
.
.
{"x":"25", "y":"23", "t":"25"}]

Pass the filename to the path points file as the first argument on the command line. If no argument is given, the test_points file will be used.


This should run in python 2.7 and 3.3.

# To Run

$ python curviness.py path_to_points_file


*Edits*


Lines 42-43: Calculate the distance of each line segment and store it
45-46: Added variables for half the distance of the path
48-55: For loop to figure out what line segment the half way point lies in
57-58: Calculate the x, y coordinates of the midpoint of the path 
59-61: Breakup list into first half points and second half points
69-70: Added a function to calculate distance between two points
72-78: Added a function to calculate curviness number

