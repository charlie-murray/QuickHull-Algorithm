"""Implementation of Quickhull algorithm"""

import math

# List to save all the convex functions
convexHull = []

# Function to calculate gradient and intercept
def calculateLine(A, B):
    # Calculate the gradient
    m = safeDivis(A[1]-B[1], A[0]-B[0])
    # Calculate the intercept
    b = A[1] - (A[0] * m)
    return m,b

# Function to divide by zero
def safeDivis(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x/y

# Function to start the running of my program
def quickHall(points):
    # Calculate the min and max coordinate dependent on the point of x
    maxium = points[0]
    minium = points[0]
    
    for ele in points:
        if ele[0] > maxium[0]:
            maxium = ele
        if ele[0] < minium[0]:
            minium = ele
    
    # Work out the data for the original line
    m,b = calculateLine(maxium, minium)
    
    # Declaring list for the two segments
    segment1 = []
    segment2 = []
    
    # Work out which coordinates go into each segment
    for ele in points:
        y = (m*ele[0]) + b
        if y > ele[1]:
            segment1.append(ele)
        elif y < ele[1]:
            segment2.append(ele)
    
    # Append the max and min to the convex list
    convexHull.append(maxium)
    convexHull.append(minium)
    
    # Run function to find out the other convex coordinates
    findHall(segment1, maxium, minium)
    findHall(segment2, minium, maxium)
    
    
# Function to find out the other convex coordinates
def findHall(segment, P, Q):
    # Return if the segment is empty
    if len(segment) == 0:
        return
    # Calculate the data for the new line
    m,b = calculateLine(P,Q)
    # Work out the perpendictual gradient
    perpGradient = safeDivis(-1, m)
    
    c1 = P[1] - (P[0]*perpGradient)
    c2 = Q[1] - (Q[0]*perpGradient)
    
    # Declaring information for the new point
    newPoint = []
    distance = 0
    
    # Filter through the elements in segment to find the farthest one
    for ele in segment:
        # Calculate the perpindicular gradient at the point
        y1 = (perpGradient*ele[0]) + c2
        y2 = (perpGradient*ele[0]) + c1
        # If inside perpendicular then calculate distance through that
        if y1 <= ele[1] and ele[1] <= y2:
            x0 = safeDivis(1, m-(perpGradient))*(ele[1] +(perpGradient*ele[0])-b)
            y0 = (perpGradient*x0) + (ele[1] - (perpGradient*ele[0]))
            dis = math.sqrt((ele[0] - x0)**2 + (ele[0] - y0)**2)
            # Update Distance and new point
            if dis >= distance:
                newPoint = ele
                distance = dis
        # If not in perpendiular then calculate more simply 
        else:
            dis1 = math.sqrt((ele[0] - P[0])**2 + (ele[1] - P[1])**2)
            dis2 = math.sqrt((ele[0] - Q[0])**2 + (ele[1] - Q[1])**2)
            if dis1>=dis2:
                # Update Distance and new point
                if dis2 >= distance:
                    newPoint = ele
                    distance = dis2
            else:
                # Update Distance and new point
                if dis1 >= distance:
                    newPoint = ele
                    distance = dis1
    
    # Calculate the two new lines with the new point
    m1, b1 = calculateLine(newPoint, P)
    m2, b2 = calculateLine(Q, newPoint)
    
    segment1 = []
    segment2 = []
    
    # Remove the new point from the current segmant
    segment.remove(newPoint)
    
    # Go through the segment to find which side of the line the point is
    for ele in segment:
        # Calculate the x value at elements y
        x1 = safeDivis(ele[1] - b1, m1)
        x2 = safeDivis(ele[1] - b2, m2)
        # If lies between both then remove from pool
        if x1 < ele[0] and x2 > ele[0]:
            segment.remove(ele)
            continue
        # If on the right of line 1 add to that segment
        if x1 < ele[0]:
            segment1.append(ele)
        # If on the right of line 2 add to that segmant
        if x2 > ele[0]:
            segment2.append(ele)
    
    # Update convex list with new point
    convexHull.append(newPoint)
    
    # Repeat the function until all segments are sorted through
    findHall(segment1, newPoint, P)
    findHall(segment2, Q, newPoint)
    
    return

# Some of my test cases
#[0, 3], [1, 1], [2, 2], [4, 4],[0, 0], [1, 2], [3, 1], [3, 3]
#[0, 0],[0, 4], [-4, 0], [5, 0],[0, -6], [1, 0]
# Initalize the function with point
print('---Implementation of Quickhull Algorithm---')
# change points to vary input, some example imputs are above
points = [[0, 0],[0, 4], [-4, 0], [5, 0],[0, -6], [1, 0]]
quickHall(points)
print('\nConvex Hull Results are: ' + str(convexHull))