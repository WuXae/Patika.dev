import math

points = [(1,2),(2,4),(4,7),(3,9)]



def euclideanDistance(point1,point2):
    x1,y1 = point1
    x2,y2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Distance calculate

distances = []

for i in range(len(points)):
    for x in range(i+1, len(points)):
        distance = euclideanDistance(points[i],points[x])
        distances.append(distance)


# Minimum distance

min_distance = min(distances)

print("Minimum Distance = ", min_distance)