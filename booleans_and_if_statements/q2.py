moths_in_house = False
mitch_is_home = True
# moths_in_house = False

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
else:
    print("Climb on Mitch.")