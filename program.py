# Ritwik Takkar - Workout Routine Generator

# Randomness (in case user wants a random workout routine)
import random

# for GUI 
import tkinter as tk

# This class creates exercises
class Exercise():
    
    def __init__(self,b='',n='',e='',o=1):
        self.__bodypart = b # muscles worked by exercise
        self.__name = n # exercise name
        self.__equip = e # equipment needed by exercise
        self.order = o # orders exercise based on muscle worked
        
# This method sets the exercise volume based on user input
    def set_volume(self, ns=0, nr=0): 
        self.ns = ns
        self.nr = nr
        self.volume = str(ns) + ' x ' + str(nr)
# This method gets the equipment if needed
    def get_equipment(self):
        return self.__equip
# This method prints out a sentence for each exercise
    def __str__(self):
        return "For "+self.__bodypart+": "+self.__name+" with "+self.__equip

# This method checks if the routine contains exercises that require same equipment or not
    def compareEquipment(self, exercise2, exercise3, exercise4):
        e2equip = exercise2.get_equipment()
        e3equip = exercise3.get_equipment()
        e4equip = exercise4.get_equipment()
        if self.__equip == e2equip or self.__equip == e3equip or self.__equip == e4equip or e2equip == e3equip or e2equip == e4equip or e3equip == e4equip:
            return "This routine contains exercises that will be done on the same equipment."
        else:
            return "All exercises in this routine require different equipment."

# This method checks what equipment is available to the user and prints it out after user enters to ensure that it is right
def equip_checker(s):
    user_equip = "string"
    if "dumbbell" in s and "barbell" not in s and "nothing" not in s: # only dumbbell 
        u_confirm = input("So you only have dumbbells available. Is this true? Enter 'y' if true, else enter any other key to re-enter your equipment.\nEnter: ")
        if u_confirm == 'y':
            print("\nSince you have all the equipment, this routine will randomly select exercises for you.\nNow, let's decide what volume scheme you'd like.")
            ex_leg = s_dumbbell[0]
            ex_shoulder = s_dumbbell[1]
            ex_back = s_dumbbell[2]
            ex_chest = s_dumbbell[3]
            user_sets = input("How many sets would you like to do for each exercise?\nUser: ")
            user_reps = input("How many reps would you like to do for each exercise?\nUser: ")
            ex_leg.set_volume(int(user_sets),int(user_reps))
            ex_shoulder.set_volume(int(user_sets),int(user_reps))
            ex_chest.set_volume(int(user_sets),int(user_reps))
            ex_back.set_volume(int(user_sets),int(user_reps))
            l1 = 'Based on your input, here is the best workout routine for today:\n'
            l2 = str('\n'+str(ex_leg)+" in the following volume scheme: "+ex_leg.volume+'\n')
            l3 = str(str(ex_shoulder)+" in the following volume scheme: "+ex_shoulder.volume+'\n')
            l4 = str(str(ex_back)+" in the following volume scheme: "+ex_back.volume+'\n')
            l5 = str(str(ex_chest)+" in the following volume scheme: "+ex_chest.volume+'\n\n')
            l6 = str(ex_leg.compareEquipment(ex_shoulder, ex_back, ex_chest)) 
            writer(l1,l2,l3,l4,l5,l6)
        else:
            main()
    elif "barbell" in s and "dumbbell" not in s and "nothing" not in s: # only barbell 
        u_confirm = input("So you only have barbells available. Is this true? Enter 'y' if true, else enter any other key to re-enter your equipment.\nEnter: ")
        if u_confirm == 'y':
            print("\nNow, let's decide what volume scheme you'd like.")
            ex_leg = s_barbell[0]
            ex_shoulder = s_barbell[1]
            ex_back = s_barbell[2]
            ex_chest = s_barbell[3] 
            user_sets = input("How many sets would you like to do for each exercise?\nUser: ")
            user_reps = input("How many reps would you like to do for each exercise?\nUser: ")
            ex_leg.set_volume(int(user_sets),int(user_reps))
            ex_shoulder.set_volume(int(user_sets),int(user_reps))
            ex_chest.set_volume(int(user_sets),int(user_reps))
            ex_back.set_volume(int(user_sets),int(user_reps))
            l1 = 'Based on your input, here is the best workout routine for today:\n'
            l2 = str('\n'+str(ex_leg)+" in the following volume scheme: "+ex_leg.volume+'\n')
            l3 = str(str(ex_shoulder)+" in the following volume scheme: "+ex_shoulder.volume+'\n')
            l4 = str(str(ex_back)+" in the following volume scheme: "+ex_back.volume+'\n')
            l5 = str(str(ex_chest)+" in the following volume scheme: "+ex_chest.volume+'\n\n')
            l6 = str(ex_leg.compareEquipment(ex_shoulder, ex_back, ex_chest)) 
            writer(l1,l2,l3,l4,l5,l6)
        else:
            main()
    elif "nothing" in s and "dumbbell" not in s and "barbell" not in s: # only bodyweight 
        u_confirm = input("So you have no equipment available. Is this true? Enter 'y' if true, else enter any other key to re-enter your equipment.\nEnter: ")
        if u_confirm == 'y':
            print("\nNow, let's decide what volume scheme you'd like.")
            ex_leg = s_bweight[0]
            ex_shoulder = s_bweight[1]
            ex_back = s_bweight[2]
            ex_chest = s_bweight[3]
            user_sets = input("How many sets would you like to do for each exercise?\nUser: ")
            user_reps = input("How many reps would you like to do for each exercise?\nUser: ")
            ex_leg.set_volume(int(user_sets),int(user_reps))
            ex_shoulder.set_volume(int(user_sets),int(user_reps))
            ex_chest.set_volume(int(user_sets),int(user_reps))
            ex_back.set_volume(int(user_sets),int(user_reps))
            l1 = 'Based on your input, here is the best workout routine for today:\n'
            l2 = str('\n'+str(ex_leg)+" in the following volume scheme: "+ex_leg.volume+'\n')
            l3 = str(str(ex_shoulder)+" in the following volume scheme: "+ex_shoulder.volume+'\n')
            l4 = str(str(ex_back)+" in the following volume scheme: "+ex_back.volume+'\n')
            l5 = str(str(ex_chest)+" in the following volume scheme: "+ex_chest.volume+'\n\n')
            l6 = 'None of these exercises require any equipment.' 
            writer(l1,l2,l3,l4,l5,l6)
        else:
            main()
    elif "dumbbell" in s and "barbell" in s: # dumbbell and barbell and bodyweight
        u_confirm = input("So you have dumbbells and barbells available. Is this true? Enter 'y' if true, else\nenter any other key to re-enter your equipment.\nEnter: ")
        if u_confirm == 'y':
            ex_leg = random.choice(legs)
            ex_shoulder = random.choice(shoulders)
            ex_back = random.choice(back)
            ex_chest = random.choice(chest)
            print("\nNow, let's decide what volume scheme you'd like.")
            # asking user what type of volume scheme they would like
            user_sets = input("How many sets would you like to do for each exercise?\nUser: ")
            user_reps = input("How many reps would you like to do for each exercise?\nUser: ")
            ex_leg.set_volume(int(user_sets),int(user_reps))
            ex_shoulder.set_volume(int(user_sets),int(user_reps))
            ex_chest.set_volume(int(user_sets),int(user_reps))
            ex_back.set_volume(int(user_sets),int(user_reps))
            l1 = 'Based on your input, here is the best workout routine for today:\n'
            l2 = str('\n'+str(ex_leg)+" in the following volume scheme: "+ex_leg.volume+'\n')
            l3 = str(str(ex_shoulder)+" in the following volume scheme: "+ex_shoulder.volume+'\n')
            l4 = str(str(ex_back)+" in the following volume scheme: "+ex_back.volume+'\n')
            l5 = str(str(ex_chest)+" in the following volume scheme: "+ex_chest.volume+'\n\n')
            l6 = str(ex_leg.compareEquipment(ex_shoulder, ex_back, ex_chest))
            writer(l1,l2,l3,l4,l5,l6)       
        else:
            main()
    elif "dumbbell" not in s and "barbell" not in s and "nothing" not in s: # no equipment (only bodyweight)
        u_confirm = print("You have not entered 'dumbbell', 'barbell' or 'nothing'. Please re-enter what equipment is available from the available choices.\n")
        main()
            

# writing to a file (creating a function that writes an exercise routine to a text file)
def writer(l1,l2,l3,l4,l5,l6):
    text = open('Routine.txt','w')
    text.write(l1)
    text.write(l2)
    text.write(l3)
    text.write(l4)
    text.write(l5)
    text.write(l6)
    text.close()

# a sort method that you write that sorts this List or Dictionary based on a specified criterion. 
# creating a function that sorts exercise routine based on order of body parts (legs, shoulder, back then chest)
def e_sort(exercise):
    return exercise.order

# this function reads all lines from the 'Routine.txt' file and copies it to the GUI
def reader():
    routine = open('Routine.txt','r')
    lines = routine.read()
    routine.close()
    return lines

# this function creates a GUI by reading the information from the routine text file and printing it on the GUI window
def GUI():
    # a Graphical User Interface window (this window displays the workout routine.)
    main_window = tk.Tk()
    # Giving a title to the GUI window
    main_window.title('Routine')
    label1 = tk.Label(main_window, text=str(reader())+"\n \nThe information above is also available in a text file named 'Routine.txt'")
    label1.pack()

# The objects below are exercises of class "Exercise"
d_gobletsquat = Exercise('legs','goblet squats','dumbbells', 1)
d_onearmrow = Exercise('back','one arm dumbbell rows', 'dumbbells', 3)
d_arnoldpress = Exercise('shoulders','Arnold presses', 'dumbbells', 2)
d_chestpress = Exercise('chest','db chest presses', 'dumbbells', 4)

b_squat = Exercise('legs','low-bar or high-bar squats, up to you,','barbells', 1)
b_row = Exercise('back','Pendlay rows','barbells', 3)
b_shoulderpress = Exercise('shoulders','overhead shoulder presses', 'barbells', 2)
b_benchpress = Exercise('chest','bench press', 'barbells', 4)

w_squat = Exercise('legs','squats','your bodyweight', 1)
w_bridge = Exercise('back','bridges','your bodyweight', 3)
w_sideplank = Exercise('shoulders','side planks','your bodyweight', 2)
w_pushup = Exercise('chest','push ups','your bodyweight', 4)

# This list contains exercise objects organized by body part 
legs = [d_gobletsquat, b_squat, w_squat]
shoulders = [d_arnoldpress, b_shoulderpress, w_sideplank]
chest = [d_chestpress, b_benchpress, w_pushup]
back = [d_onearmrow, b_row, w_bridge]

# each list contains exercise with certain equipment
dumbell = [d_gobletsquat, d_arnoldpress, d_chestpress, d_onearmrow]
barbell = [b_squat, b_shoulderpress, b_benchpress, b_row]
bweight = [w_squat, w_sideplank, w_pushup, w_bridge]

# the lists below are sorted in terms of body part for routine
s_barbell = sorted(barbell, key = e_sort)
s_dumbbell = sorted(dumbell, key = e_sort)
s_bweight = sorted(bweight, key = e_sort)

# Defining main function: 
def main():
    user_equip = input("What equipment is available in your gym? Choices include: barbell, dumbbell and nothing.\nNote that nothing (bodyweight) is automatically included.\nEnter equipments with a space in between: ")
    user_equip = user_equip.lower()
    equip_checker(user_equip)

# Calling the main function
main()

# Let the user know that their routine is ready in a text file
print("\nYour routine is ready in a text file named 'Routine.txt' in the same directory as this program")

# Calling the GUI function to display the GUI window after the Routine.txt file has been updated
GUI()
