def getArea(radius):
    return 3.14*radius**2

radius_list = [0.1,0.5,2,3,8,12]

areas = list(map(getArea, radius_list))
area2 = list(filter(lambda r:r>1, radius_list))
print(area)
print(area2)