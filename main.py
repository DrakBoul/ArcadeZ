import numpy as np
import matplotlib.pyplot as plt
import random
import time
from matplotlib.colors import ListedColormap, BoundaryNorm

import sys
sys.path.insert(0, './keyboard-0.13.5')
import keyboard 

z_pixels =  np.empty((0,2), int)
data = np.zeros((50, 50)) 
p_pixel_position = np.array([0,0])
round_count = 1

scrMenu = 'menu'
scrHTP = 'HowToPlay'
 
def main():
    '''
    The main function initialize the code
    '''
    menuList = loaddata('Menu')
    menuInteraction(menuList)

def loaddata(filename):
    '''
    This function loads the data from the .txt file which contains numbers in the for 
    of a string and this function process the text in order remove the tab-lines 
    and spaces, and convert it into and array
    '''
    file = open(filename + '.txt','r')
    list1 = file.readlines()
    file.close()
    
    #This forLoop removes newline characters and split into columns
    for i in range(len(list1)):
        row = list1[i].strip()  # remove '\n'
        columns = row.split('\t')  # split by '\t'
        list1[i] = columns
    list1 = [[int(comp) for comp in row] for row in list1] #converts the str-list into integers
    # print(list1)
    return list1
    
def menuInteraction(menuList):
    '''
    In this function, the typical home screen of an arcade video game was programmed, 
    with the message that tells the user which key to press to start.
    '''
    
    #The arrays a and b are created to later use them as alpha 
    #values for the text on the screen
    
    a = np.arange(0.2,1.1,0.2)
    b = np.arange(0.8, 0.2, -0.2)
    alphas = np.concatenate((a,b))
    trueKey = True
    
    #This while loop is for refreshing the screen with a new 
    #alpha value for the text
    while trueKey:
        for i in range(len(alphas)):
            
            alpha1 = alphas[i]
            plt.text(9, 35,'PRESS SPACE TO START', fontsize=12, color='white', alpha=alpha1)
            plotting(menuList)
            time.sleep(0.09)
            
            if keyboard.is_pressed("space"):
                select(menuList, scrMenu)
                trueKey = False
                time.sleep(0.09)
                break

def text(x,y,list2, textKey):
    '''
    This functions displays the text, according to the textKey which is in charge of
    determining what screen is the user looking at in order to display the right texts
    '''
    if textKey == 'menu': 
        xfac = 0 #Shifts all x-positions
        yfac = 0 #Shifts all y-positions
        plt.text(x + xfac, y + yfac,'>', fontsize=12, color='white')
        plt.text(20 + xfac, 28 + yfac,'Play', fontsize=12, color='white')
        plt.text(15 + xfac, 32 + yfac,'How To Play', fontsize=12, color='white')
        
        #Instructions
        plt.text(0,48, 'Exit = "ESC" | Up = "W"  \nDown = "S" | Select = "K"', fontsize=8, color='white')
        
    elif textKey == 'HowToPlay':
        x1 = -2 #Horizontal factor to displace the text
        plt.text(12 + x1, 3, '"Run for your life', fontsize=12, color='white', fontweight='bold')
        plt.text(10.5 + x1, 6.2, 'escape the zombies,', fontsize=12, color='white', fontweight='bold')
        plt.text(23 + x1, 9, 'and', fontsize=12, color='white', fontweight='bold')
        plt.text(8 + x1, 12, ' don'+"'t"+' let them bite you"', fontsize=12, color='white', fontweight='bold')
        plt.text(0, 26,'Move Left', fontsize=11, color='white')
        plt.text(28.5, 18,'Move Up', fontsize=11, color='white')
        plt.text(1, 37.5,'Move Down', fontsize=11, color='white')
        plt.text(34.5, 26,'Move Right', fontsize=11, color='white')
        plt.text(0, 48.7, 'Go back = "J"', fontsize=8, color='white')
    plotting(list2)
    return

def select(menuList,textKey):
    '''
    In this function its evaluated the keyboard input from the user, to determine which selection is 
    making in the menu and give the right response back to user. 
    '''
    text(17,27.8,menuList,textKey) #Invokes the text function with the needed array and textKey
    CoordX = [17,12]               #This array stores the x-coordinates of the menu cursor
    CoordY = [27.8,32]             #This array stores the y-coordinates of the menu cursor 
    selection = 0                  #Initialize a counter for the selection, in to identify where the cursor is. (Initially is divisible by 2, therefore is on the "Play option") 
    delay = 0.3                    #Delays the functions to avoid runtime errors
    
    trueFalse = True               #This trueFalse-key breaks the loop when needed
    
    while trueFalse:
        
        if keyboard.is_pressed('k'):
            trueFalse = False
            time.sleep(delay)
            if selection % 2 ==0:
                # print("You've selected Play") 
                gameloop()          #gameloop being invoked
                break
                time.sleep(delay)
            else:
                select(loaddata(scrHTP), scrHTP) #Loads and plots the How to play instructions with the required textKey
                time.sleep(delay)
                
        #Go back to menu screen
        if keyboard.is_pressed('J') and textKey == scrHTP:
            select(loaddata(scrMenu),scrMenu) #Executes Main Menu when user press go back in the How-To-Play screen
            time.sleep(delay)
                
        if keyboard.is_pressed('esc'):
            raise SystemExit #Stops the program and exits

        #The following if conditionals evaluate the textKey to make sure the input is detected in the right screen
        if keyboard.is_pressed('w') and textKey == scrMenu:
            if selection % 2 ==0:   
                selection = ((selection-1) % len(CoordX))
                x = CoordX[selection]
                y = CoordY[selection]
                text(x,y,menuList,scrMenu)
                time.sleep(delay)
            else:
                selection = ((selection+1) % len(CoordX))
                x = CoordX[selection]
                y = CoordY[selection]
                text(x,y,menuList,scrMenu)
                time.sleep(delay)
            
        elif keyboard.is_pressed('s') and textKey == scrMenu:
            if selection % 2 ==0:
                selection = ((selection-1) % len(CoordX))
                x = CoordX[selection]
                y = CoordY[selection]
                text(x,y,menuList,scrMenu)
                time.sleep(delay)
            else:
                selection = ((selection+1) % len(CoordX))
                x = CoordX[selection]
                y = CoordY[selection]
                text(x,y,menuList,scrMenu)
                time.sleep(delay)  
    return

def plotting(menuList):
    '''
    In this function a color palette is created for the menu pixel art, assigning 
    a dictionary the keys according to the number in the array being plotted
    and each key contain a hexadecimal color for mapping and plotting
    '''
    #Defines the letter to the hexadecimal color mapping
    color_dict = {1: '#7658A0', #Purple
                  2: '#3D81C2', #Blue
                  3: '#8CD6F1', #Baby Blue
                  4: '#4b6043', #Green
                  5: '#BF2C34', #Red
                  6: '#A9C2A1', #Ligth Green
                  7: '#BE9C2F', #Yellow
                  8: '#CA783B',  #Orange
                  9: '#A85450',  #Ligth red
                  10: '#373630', #Brown
                  11: '#000000', #Black
                  12: '#FFFFFF', #White
                  13: '#9E9D9D'} #Gray
    
    #Defines the boundaries for each value in the array list comparing with the dictionary
    bounds = np.arange(1, len(color_dict) + 2)
    norm = BoundaryNorm(bounds, len(color_dict) + 1)
    
    #Defines the colors for the colormap
    colors1 = [color_dict.get(i) for i in bounds[:-1]]
    cmap = ListedColormap(colors1)
    
    #The menu is plotted 
    plt.axis('off')
    plt.imshow(menuList, cmap=cmap, norm=norm)
    plt.show()
    return

def gameloop():
    global p_pixel_position, round_count, data #declaring global 
    
    game_over, spawn_truth = False, False # truth variables    
    start = time.time()             # start of game time
    round_time = 10                 # initial round time
    amount_z_pixel = 10             # initial amount of z_pixels
    p_pixel_y, p_pixel_x = 25, 25   # player initial position
    
    while True:         #game loop
    #block initiate if game has started or new round begins
        if spawn_truth == False:        
            spawn_truth = True
            p_pixel_y, p_pixel_x, start, data = resetgrid(start, data, p_pixel_y, p_pixel_x)
            spawnZ_pixel(amount_z_pixel, round_time, start)
            
        p_pixel_y, p_pixel_x, p_pixel_position, game_over = actionloop(start, p_pixel_y, p_pixel_x, round_time, p_pixel_position, game_over)
        #checks if game over condition is met
        
        if keyboard.is_pressed('esc'):
            raise SystemExit #Stops the program and exits
        
        if game_over == True: 
            print('GAME OVER!!! you survived', str(round_count), 'rounds.')
            time.sleep(1)
            select(loaddata(scrMenu), scrMenu)
            
        # checks if timer is out of time
        if countdown(round_time, start) < 1:

            round_count, round_time, amount_z_pixel, spawn_truth = roundIncrease(round_count, round_time, amount_z_pixel, spawn_truth)
        
def resetgrid(start, data, p_pixel_y, p_pixel_x):
    """takes in 4 arguments start, data, p_pixel_y, and p_pixel_x, the function resets
    the map, start time and pixel coordinates each time a new round begins. it 
    returns these values as tuples and then stores them in there corresponding variable
    when invoked in main."""
    start = time.time()         
    data = np.zeros((50, 50))
    p_pixel_x = 25         
    p_pixel_y = 25
    data[p_pixel_y][p_pixel_x] = -1
    return (p_pixel_y, p_pixel_x, start, data)
    
def spawnZ_pixel(amount_z_pixel, round_time, start):
    """spawnZ_pixel takes in three arguments amount_z_pixel, round_time, and start. it 
    spawns in the number of designated z_pixels in random positions around the perimeter 
    the pixel grid, update screen is also invoked from within this function as to 
    ensure that the screen is updated with the addition of each zombie pixel."""
    global z_pixels
    z_pixels =  np.empty((0,2), int)
    for i in range(amount_z_pixel):
        rand_int = random.randint(0, 1)
        rand_int2 = random.randint(0, 1)
        if rand_int % 2 == 0:
            if rand_int2 % 2 == 0:
                z_pixels = np.append(z_pixels, np.array([[random.randint(0,3),random.randint(0,49)]]), axis=0)
            else:
                z_pixels = np.append(z_pixels, np.array([[random.randint(0,49),random.randint(47,49)]]), axis=0)
        elif rand_int % 2 != 0: 
            if rand_int2 % 2 == 0:
                z_pixels = np.append(z_pixels, np.array([[random.randint(0,49),random.randint(0,3)]]), axis=0)
            else:
                z_pixels = np.append(z_pixels, np.array([[random.randint(47,49),random.randint(0,49)]]), axis=0)
        updatescreen(data, round_time, start)
            # appends a randomized pixel within a range to the end of the z_pixels array
            # rand_int 1 and 2 supply the spawn randomness, the conditional statements test
            # if the random number is divisible by 2 or not
            
def actionloop(start, p_pixel_y, p_pixel_x, round_time, p_pixel_position, game_over):
    """this is the main for loop that the game runs from. it takes 6 arguments
    start, p_pixel_y, p_pixel_x, round_time, p_pixel_position, and game_over. it starts
    by iterating over each element in z pixels. it first checks if a game over condition
    is met by the checkZandP function. then it moves the player pixel, then the zombie pixels.
    it returns the players pixel coordinates, an array of its position and then the game_over
    truth variable."""
    
  
    for i in range(z_pixels.shape[0]):    
        # move the player pixel
        p_pixel_y, p_pixel_x, p_pixel_position = moveP_pixel(p_pixel_y, p_pixel_x)
        # move the zombie pixel
        moveZ_pixel(p_pixel_y, p_pixel_x, i)
        # update the screen
        #check if zombie pixel has touched player pixel
        if checkZandP(game_over, p_pixel_position, z_pixels) == True or keyboard.is_pressed("f"):
            game_over = True
        updatescreen(data, round_time, start)

    
    
    
    return  (p_pixel_y, p_pixel_x, p_pixel_position, game_over)
            

def moveZ_pixel(p_pixel_y, p_pixel_x, i):
    """takes three arguments p_pixel_y, p_pixel_x, and an integer i. it loops through the
    columns of the arrary z_pixels and moves them one unit closer to the players pixel.
    if the random integer's remainder when divided by 2 = 0 then it will move
    one closer in the x direction, if the remainder does not = 0 then it will
    move one unit closer in the y direction. it does not return anything but does
    modify the value of the data and z_pixels arrays."""
    
    rand_int = random.randint(0,1)  
    data[z_pixels[i,1]][z_pixels[i,0]] = 0
    if z_pixels[i,1] < p_pixel_y and rand_int % 2 == 0:
        z_pixels[i,1] += 1
    elif z_pixels[i,0] > p_pixel_x and rand_int % 2 != 0:
        z_pixels[i,0] += -1
    elif z_pixels[i,1] > p_pixel_y and rand_int % 2 == 0:
        z_pixels[i,1] += -1
    elif  z_pixels[i,0] < p_pixel_x and rand_int % 2 != 0:
        z_pixels[i,0] += 1
    data[z_pixels[i,1]][z_pixels[i,0]] = 1
    
    
    
def moveP_pixel(p_pixel_y, p_pixel_x):
    """moveP_pixel function takes in two arguments p_pixel_y, and p_pixel_x. it moves
    the players pixel by using a keyboard listener with the movement keys being w,a,s,d
    the wrap_coordinates function checks if the coordinates have been wrapped before storing
    the coordinates in the data array to prevent crashing. finally the function
    returns the updated coordinates for the player as well as an array containing 
    the players coordinates which is later compared to the positions of the zombies."""
    data[p_pixel_y][p_pixel_x] = 0 # erases current current p-pixel location
    
    if keyboard.is_pressed("w"):    #move player up
        p_pixel_y += 1                      
    elif keyboard.is_pressed("a"):  #move player left
        p_pixel_x += -1
    elif keyboard.is_pressed("s"):  #move player down
        p_pixel_y += -1
    elif keyboard.is_pressed("d"):  #move player right
        p_pixel_x += 1
    p_pixel_y, p_pixel_x = wrap_coordinates(p_pixel_y, p_pixel_x) #checks for wrapping and gives new coordinates if true
    data[p_pixel_y, p_pixel_x] = -1 # position is stored in data and given -1 value (blue)
    return  (p_pixel_y, p_pixel_x, np.array([p_pixel_x, p_pixel_y]))
    
def updatescreen(data, round_time, start):
    """The update screen function takes in 3 arguments data, round_time, and start. 
    it returns nothing and serves to update the screen. the title is a formatted string
    containing both the round count and the duration left in the round for the player to see."""
    plt.figure() 
    plt.axis('off')
    plt.title('timer: {0} || Round number: {1}'.format(str(countdown(round_time, start)), round_count))
    plt.imshow(data, cmap='coolwarm', origin='lower')
    plt.show()

def checkZandP(game_over, p_pixel_position, z_pixels): 
    """the checkZandP function takes three arguments. the game_over varible
    the players pixel position, and the z pixels positions in the form of arrays.
    the conditional statement checks to to see if the player position is contained 
    in the z pixels array. if true it sets the game over varible equal to True 
    signifying that the player has made contact with zombie pixel for a sustained time.
    the game over variable is then returned."""
    
    if any(np.array_equal(p_pixel_position, row) for row in z_pixels):
        game_over = True
        
    return game_over

def countdown(round_time, start):
    """countdown function takes two arguments, the round_time and the start variable
    it initiates the end variable at the current time and subtracts it from start and then
    stores it into the timer_duration variable. this variable is then returned as an integer.
    this is the function which keeps track of the round duration."""
    
    end = time.time()
    total = end - start
    timer_duration = round_time - total
    
    return int(timer_duration)

def roundIncrease(round_count, round_time, amount_z_pixel, spawn_truth):
    """the round increase function takes in 4 arguments, round_count, round_time, 
    amount_z_pixel, and spawn_truth. this function is activated when a new round has
    started. it increases the round time, and round count and the amount of zombie
    pixels being spawned for the next round. it also sets the spawn truth variable to 
    false. these variables are then returned as a tuple of values which are assigned to
    there corresponding variables when provoked in main"""
    
    spawn_truth = False #reset spawn truth
    round_time += 10 #increase round time
    round_count += 1 #increase round count
    amount_z_pixel += 5 #increase zombie pixel amount
    
    return (round_count, round_time, amount_z_pixel, spawn_truth)

def wrap_coordinates(p_pixel_y, p_pixel_x):
    """The wrap coordinates function takes two arguments and returns the players, x and y
    pixel coordinates. the purpose of thiss function is to prevent the program 
    from crashing when the player goes out of bounds of the data array. instead 
    the function wraps the coordinates to the opposite side of from where it went out of bounds."""
    # Wraps coordinates around vertically
    if p_pixel_y < 0:
        p_pixel_y = 49
    elif p_pixel_y > 49:
        p_pixel_y = 0
        
    # Wraps coordinates around horizontally
    if p_pixel_x < 0:
        p_pixel_x = 49
    elif p_pixel_x > 49:
        p_pixel_x = 0 
        
    return p_pixel_y, p_pixel_x
main()

        
        
        
