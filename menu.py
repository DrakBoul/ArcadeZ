import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import time
import numpy as np
import keyboard

scrMenu = 'menu'
scrHTP = 'HowToPlay'

def menu():
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
                
                
                
                print("You've selected Play") ####REPLACE THIS FOR THE PLAY FUNCTION###
                #to load the menu again type: select(loaddata(scrMenu),scrMenu)....wherever you want to invoke it#
                
                
                
                
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


menu()

