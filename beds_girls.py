rooms=int(input("enter the rooms:"))
girls=int(input("enter the girls:"))
if rooms>girls:
    print("we want",rooms-girls,"girl")
elif girls>rooms:
    print("girls" ,girls-rooms, "left")     
else:
    print("filled")
                  