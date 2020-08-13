"""Welcome to GreenBot by Ryan Green! Here is my code:"""


#This adds the Sound library
add_library('sound')
#Variable Declaration
x = 0
up = 0
side = 0
speed = 1
textCount = 100
colour = 0
goText = True
wave = 0
waveup = 0
carCount = 100
altcolour = 0
raincolour = False

#Setup (Runs Once)
def setup():
    size(800, 600)
    #Jetsons Car Image Import
    global car, beeps, speedsound
    car  = loadImage("Jetsons.jpg")
    beeps = SoundFile (this, "Randomize18.wav") 
    speedsound = SoundFile(this, "Powerup5 2.wav")
    #Sounds are created by me using Increpare's BFXR Sound Effect Creation Program

#Repeated Draw Function    
def draw():
    #Background is in Draw Function to overwrite previous drawings
    background(255)
    #Global Variables
    global x, textCount, goText, up, side, wave, waveup, carCount
    #Introduction Text
    if goText:
        fill(0) #Text Coloured Black
        text("Beep! Beep! Boop! Welcome to GreenBot by Ryan Green! Move GreenBot by pressing WASD! Use the + and - keys to adjust GreenBot's speed! To customize GreenBot, use the arrow keys and SPACE! Press BACKSPACE to toggle this notification! Have Fun! - Ryan Green", textCount, 10)
        #The code below makes the text scroll across the screen (like on the news)
        if textCount > -1460:
            textCount -= 1.35
        else:
            textCount = 1350
    
    #Car that travels from bottom left to top right; repeats
    image(car, 0 - carCount, 425 + (carCount/2))
    if carCount > -1450:
        carCount -=1.25
    else:
        carCount = 1350
    
    #Metal Colour Changer (Changed with UP and DOWN arrow keys)
    if altcolour == 1:
        fill(175, 172, 167)
    elif altcolour == -1:
        fill(172, 188, 167)
    else:
        fill(188, 196, 186)
    
    #Main body of the Robot
    ellipse(499 + side, 97.5 + up, 28, 45) #Right "Ear"
    ellipse(349 + side, 97.5 + up, 28, 45) #Left "Ear"
    rect(425 + side, 25 + up, 2.5, 25) #Antenna
    ellipse(426.25 + side, 25 + up, 7.5, 7.5) #Top of Antenna
    ellipse(426.25 + side, 58.85 + up, 28, 26) #Bottom of Antenna
    rect(350 + side , 50 + up, 150, 150) #Main Structure
    


    #Eye & Teeth colour changer (Changed with LEFT & RIGHT arrow keys)
    if colour == 1:
        fill(232, 111, 77)
    elif colour == -1:
        fill(77, 234, 64)
    else:
        fill(245, 237, 89)
    
    #Eyes
    rect(375 + side, 75 + up, 45, 45)  #Left
    rect(430 + side, 75 + up, 45, 45)  #Right
    #White Mouth
    fill(255)
    rect(360 + side, 140 + up, 130, 35)
    #White Teeth
    rect(360 + side, 140 + up, 10, 17.5)
    rect(370 + side, 140 + up, 10, 17.5)
    rect(380 + side, 140 + up, 10, 17.5)
    rect(390 + side, 140 + up, 10, 17.5)
    rect(400 + side, 140 + up, 10, 17.5)
    rect(410 + side, 140 + up, 10, 17.5)
    rect(420 + side, 140 + up, 10, 17.5)
    rect(430 + side, 140 + up, 10, 17.5)
    rect(440 + side, 140 + up, 10, 17.5)
    rect(450 + side, 140 + up, 10, 17.5)
    rect(460 + side, 140 + up, 10, 17.5)
    rect(470 + side, 140 + up, 10, 17.5)
    rect(480 + side, 140 + up, 10, 17.5)
    
    #Colour (Changed with LEFT & RIGHT arrow keys) flashes across teeth
    if x != 130:
        if colour == 1:
            fill(232, 111, 77)
        elif colour == -1:
            fill(77, 234, 64)
        else:
            fill(245, 237, 89)
        if raincolour:
            fill(random(255), random(255), random(255))
        x += 10
        rect(350 + x + side, 140 + up, 10, 17.5)
        if x == 130:
            x = 0
    
    #When the robot goes off screen, brings it back on on opposite side (like Pacman)
    #Vertical
    if up < -200:
        up = 582.5
    elif up > 582.5:
        up = -200
    
    #Horizontal
    if side <-514:
        side = 464
    elif side > 464:
        side = -514
    
    #Radio wave produced by antenna; gets bigger as it travels
    wave -= 0.01
    stroke(22, 208, 216)
    noFill()
    waveup -= 1
    ellipse(426.25 + side, 25 + up + waveup, 15 - wave , 5 - wave)
    if waveup == -100:
        waveup = 0
        wave = 0
    stroke(0)

#Function for pressed keys on keyboard
def keyPressed():
    #Global Variables
    global up, side, speed, colour, goText, altcolour, raincolour
    #Movement with WASD
    if key == 'w':
        up -= speed
    elif key == 's':
        up += speed
    elif key == 'd':
        side += speed
    elif key == 'a':
        side -= speed
    #Speed increase/decrease with + and - respectively
    elif key == '+':
        if speed <= 10:
            speed += 1
            speedsound.play()
            speedsound.rate(-1+speed/1.5)
    elif key == '-':
        if speed > 2:
            speed -= 1
            speedsound.play()
            speedsound.rate(-1+speed/1.5)
    #Arrow keys & SPACE for customization (Change colours)
    if key == CODED:
        if keyCode == LEFT:
            if colour == -1:
                colour = 1
            else:
                colour -= 1
            beeps.play()
        elif keyCode == RIGHT:
            if colour == 1:
                colour = -1
            else:
                colour += 1
            beeps.play()
        elif keyCode == UP:
            if altcolour ==1:
                altcolour = -1
            else:
                altcolour += 1
            beeps.play()
        if keyCode == DOWN:
            if altcolour == -1:
                altcolour = 1
            else:
                altcolour -= 1
            beeps.play()
    elif key == ' ':
            if raincolour != True:
                raincolour = True
            else:
                raincolour = False
    #Toggle text        
    elif key == BACKSPACE:
        if goText == True:
            goText = False
        else:
            goText = True