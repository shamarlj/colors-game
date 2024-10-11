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
pantone="101 000 010"
white="111 111 111"
darkgreen="001 100 010"
teal="001 100 100 "
darkpurple="100 001 101"
darkgrey="011 011 011"
navyblue="000 000 010"
shamar="014 024 019"
brown="101 011 000"
lavender="011 100 111"
banna="111 111 110"
aqua14="000ffff"
jaiden="loser"
miami="dolphins"
score=0

scorewrong=0

rng_COLORS=[aqua,red,lightblue,magenta,yellow,green,purple,grey,darkpink,orange,lightpurple,blue,black,pantone,white,darkgreen,teal,darkpurple,darkgrey,navyblue,brown,shamar,lavender
       ,miami ,jaiden  ,aqua14 ,banna]


while True:
    print("user what color is this in Binary")
    #randomly pick a color#
    rng_COLOR=random.choice(rng_COLORS)
    print(rng_COLOR)




    #(red green blue) with the random picker it will pick a random color/binary
    #hey user what color is this
    #is what the user typed in the same as the random choice (red)  #data validation
    #red true:) then print correct




    if rng_COLOR==black and input("input colors ") == "black":
            print("correct 😍")
            score += 4



    elif rng_COLOR==miami and input("input colors ") == "miami":
            print("right👍🏿")
            score +=1972



      
    elif rng_COLOR==jaiden and input("input colors ") == "jaiden":
            print("right👍🏿")
            score -=10020

            
    elif rng_COLOR==banna and input("input colors ") == "banna":
            print("right👍🏿")
            score +=1


    elif rng_COLOR==red and input("input colors ") == "red":
            print("right👍🏿")
            score +=1


    elif rng_COLOR==aqua and input("input colors ") == "aqua":
            print("great👍🏿")
            score +=10


    elif rng_COLOR==lightblue and  input("input colors ") == "lightblue":
            print("right👍🏿")
            score +=1
    elif rng_COLOR==magenta and input("input colors ") == "magenta":
            print("฿Ɽ₳VØ👍🏿")
            score +=3
    elif rng_COLOR==yellow and  input("input colors ") == "yellow":
            print("ₐₘₐᶻᵢₙᴳ👍🏿")
            score +=1  
    elif rng_COLOR==green and input("input colors ") == "green":
            print("ⳏⲉⲅ⳨ⲥⲧ👍🏿")
            score +=1
    elif rng_COLOR==purple and  input("input colors ") == "purple":
            print("ꝒƸⱤƑƇƬ👍🏿")
            score +=1
    elif rng_COLOR==grey and input("input colors ") == "grey":
            print("@ⲙⲁⲹⳕⲛⳋ👍🏿")
            score +=1
    elif rng_COLOR==darkpink and  input("input colors ") == "darkpink":
            print("𝒸ℴ𝓇𝓇ℯ𝒸𝓉👍🏿")
            score +=1
    elif rng_COLOR==orange and  input("input colors ") == "orange":
            print("c̶o̶r̶r̶e̶c̶t̶👍🏿")
            score +=1  
    elif rng_COLOR==lightpurple and input("input colors ") == "lightpurple":
            print("¢ðrrê¢†👍🏿")
            score +=1
    elif rng_COLOR==blue and input("input colors ") == "blue":
            print("ƇⰙⱤⱤƸƇƬ👍🏿")
            score +=1
    elif rng_COLOR==pantone and  input("input colors ") == "pantone":
            print("₵ØⱤⱤɆ₵₮👍🏿")
            score +=5


    elif rng_COLOR==darkgreen and  input("input colors ") == "darkgreen":
            print("w👍🏿")


            score +=1  
    elif rng_COLOR==teal and  input("input colors ") == "teal":
            print("ni₵E👍🏿")


            score +=1


    elif  rng_COLOR==darkpurple and  input("input colors ") == "darkpurple":
            print("ni₵E👍🏿")
            score +=1


    elif  rng_COLOR==aqua14 and  input("input colors ") == "aqua14":
            print("ni₵E👍🏿")
            score +=9999


    elif  rng_COLOR==darkgrey and  input("input colors ") == "darkgrey":
            print("ni₵E👍🏿")
            score +=1





    elif  rng_COLOR== brown and  input("input colors ") == "brown":
            print("ni₵E👍🏿")
            score +=1


 

    elif  rng_COLOR==navyblue and  input("input colors ") == "navyblue":
         print("ni₵E👍🏿")
         score +=1



   

    elif  rng_COLOR==lavender and  input("input colors ") == "lavender":
            print("ni₵E👍🏿")
            score +=1


    elif  rng_COLOR==shamar and  input("input colors ") == "shamar":
            print("ni₵E👍🏿")
            score +=14





    else:
            print("wrong")
            scorewrong+=1


    print(score,"correct")
    print(scorewrong,"wrong")


    print("")


    gamecontinue = input("Do you want to end the game?  y/n:     ")


    if gamecontinue == "y":
        break










