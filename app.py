pl_name = str(input("Footballer name: "))
min = float(input("Mins: "))
distance = float(input("Distance: "))
max_speed = float(input("Max speed: "))
sprints = int(input("Sprints: "))
print(f"Player name: {pl_name}")
print(f"Minutes: {min}")
print(f"Distance: {distance}")
print(f"Max speed: {max_speed}")
print(f"Sprints: {sprints}")
if distance > 10000:
    print("High running load")
else:
    print("Normal running load")
    if max_speed > 32:
        print("Fast player")
    else: 
        print("Normal speed player")