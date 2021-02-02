def findCoords(dimensions):
    dimensions = sorted(dimensions, key=lambda element: (element[0], element[1]))
    print('INPUT:', dimensions)
    result = []
    for i, d in enumerate(dimensions):
        if i == 0:
            # To solve cases when starting point is same but height is different
            result.append((d[0], d[2]))
            print('1st Case')
        else:
            if dimensions[last_coord][0] <= d[0] and dimensions[last_coord][1] >= d[1]:
                if dimensions[last_coord][2] >= d[2]:
                    #print('Submerged Case')
                    # fully Submerged case Do nothing
                    continue
                else:
                    #print('Submerged but more height Case')
                    # Semi Submerged case with diff height
                    result.append((d[0], d[2]))
                    result.append((d[1], dimensions[last_coord][2]))
                    continue
            elif d[0] > dimensions[last_coord][1]:
                #print('No Intersection Case')
                # When there is no intersecting point. NOTE: This case comes first before intersecting
                result.append((dimensions[last_coord][1], 0))
                result.append((d[0], d[2]))
            elif dimensions[last_coord][0] <= d[0] and dimensions[last_coord][1] <= d[1]:
                #print('Intersecting Case')
                # When they have intersecting point
                if dimensions[last_coord][2] > d[2]: 
                    result.append((dimensions[last_coord][1], d[2]))
                else:
                    result.append((d[0], d[2]))
        last_coord = i
    #print('Last case')
    result.append((dimensions[last_coord][1], 0))
    print(result)
    print('-------------------------------------')



INPUT = [[(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)],
         [(1, 10, 4), (1, 8, 6), (1, 6, 8)],
         [(0, 6, 2), (5, 10, 8), (7, 8, 12)]
]

for inp in INPUT:
    findCoords(inp)     

