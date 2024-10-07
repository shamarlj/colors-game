import random
black="000 000 000"
red="111 000 000"
aqua="000 111 110"
lightblue="000 111 111"
magenta="111 000 111"
yellow="111 111 011"
green= "000 111 000"
purple="011 000 111"
grey="100 100 100"
darkpink="111 001 011"
orange="111 011 000"
lightpurple="100 011 111"
blue="000 000 111"

rng_COLORS=[aqua,red,lightblue,magenta,yellow,green,purple,grey,darkpink,orange,lightpurple,blue,black]


print("user what color is this in Binary")
#randomly pick a color#
rng_COLOR=random.choice(rng_COLORS)
print(rng_COLOR)


#(red green blue) with the random picker it will pick a random color/binary
#hey user what color is this
#is what the user typed in the same as the random choice (red)  #data validation
#red true:) then print correct


if rng_COLOR==black:
    if input("input colors ") == "black":
        print("correct")

elif rng_COLOR==red:
    if input("input colors ") == "red":
        print("correct")

elif rng_COLOR==aqua:
    if input("input colors ") == "aqua":
        print("correct")

elif rng_COLOR==lightblue:
    if input("input colors ") == "lightblue":
        print("correct")

elif rng_COLOR==magenta:
    if input("input colors ") == "magenta":
        print("correct")

elif rng_COLOR==yellow:
    if input("input colors ") == "yellow":
        print("correct")

elif rng_COLOR==green:
    if input("input colors ") == "green":
        print("correct")

elif rng_COLOR==purple:
    if input("input colors ") == "purple":
        print("correct")

elif rng_COLOR==grey:
    if input("input colors ") == "grey":
        print("correct")

elif rng_COLOR==darkpink:
    if input("input colors ") == "darkpink":
        print("correct")

elif rng_COLOR==orange:
    if input("input colors ") == "orange":
        print("correct")

elif rng_COLOR==lightpurple:
    if input("input colors ") == "lightpurple":
        print("correct")

elif rng_COLOR==blue:
    if input("input colors ") == "blue":
        print("correct")
else:
    print("Incorrect")