# Base Rotation
front_row = ['John','Alex','Steve']
back_row = ['Jane','Mary','Bob']

# We need to insert the end of the front_row to the back of the back_row
# We need to insert the first of the back_row to the front of the front_row

rotations = 6

for i in range(rotations):
    front_row.insert(0, back_row.pop(0)) 
    back_row.append(front_row.pop(-1))

    print(f"Rotation {i+1}")
    print(f"Front Row: {front_row}")
    print(f"Back Row: {back_row}")
    print("--------------------------------")





