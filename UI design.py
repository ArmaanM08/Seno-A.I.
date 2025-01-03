#IMPORTS---------

from customtkinter import *
from PIL import Image
from time import *
import main

#-------xxxxxxxxx-------

root = CTk()
root.geometry("800x600")
root.title("SENO-AI")

#creating frames========
main_frame = CTkFrame(master = root,width = 650, height = 500,border_width=1)#main frame
main_frame.place(x = 150,y = 0)

side_frame = CTkFrame(master = root,width = 150,height = 500,border_width=0.5)#side frame
side_frame.place(x = 0,y = 0)

bottom_frame = CTkFrame(master = root, width = 650,height = 100,border_width = 0.5,fg_color="white")#bottom frame
bottom_frame.place(x = 150, y = 500)

clk_frame = CTkFrame(master = root,width = 150,height = 100,border_width=1,fg_color="white",corner_radius=25)#clock frame
clk_frame.place(x = 0,y = 500)

#======ELEMENTS==========

#=====Mainframe Elements=
seno = Image.open("/Users/armaanmulani/Desktop/Seno-A.I./Resources/seno.jpeg")
senopht = CTkImage(light_image = seno, size = (30,30))

img_lbl = CTkLabel(master = main_frame, image = senopht,text = "")
img_lbl.place(x = 0,y = 0)

txt1 = CTkLabel(master = main_frame, text = "Hey,I'm Seno A.I.", font = ("Verdana",16),corner_radius=50)
txt1.place(x = 35,y = 0)

#===Sideframe Elements==

hstry_lbl = CTkLabel(master = side_frame,text = "Previous Chats",font = ('Helvetica', 12,"underline"))
hstry_lbl.place(x = 40,y = 5)




#===Bottomframe_Elements=
mic = Image.open("/Users/armaanmulani/Desktop/Seno-A.I./Resources/mic.png")
micpht = CTkImage(light_image = mic)
vc_cmnd = CTkButton(master = bottom_frame,image = micpht,text = "",corner_radius=100,width = 4,command=main.start())
vc_cmnd.place(x = 595,y = 25)
vc_lbl = CTkLabel(master = bottom_frame,text = "Start Voice \nInput",font = ("Arial",12))
vc_lbl.place(x = 590,y = 55)

cmnd = CTkEntry(master = bottom_frame,placeholder_text="Search/Chat anything",justify = "center",width=500)
cmnd.place(x = 90,y=25)





#===Clockframe_Elements=
#defining_function_for_clock
def toggle_date_time():
    """Toggles between displaying date and time."""
    global show_date
    show_date = not show_date  # Toggle the flag
    update_display()

def update_display():
    """Updates the label with either date or time."""
    if show_date:
        text = strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
    else:
        text = strftime("%H:%M:%S")
    clock_label.configure(text=text)
    clock_label.after(1000, update_display)  # Update every second
show_date = False 

# Create the clock/date label
clock_label = CTkLabel(master = clk_frame, text="", font=("Helvetica", 22))
clock_label.place(x = 29,y = 20)

# Create the toggle button
toggle_button = CTkButton(master = clk_frame, text="Toggle Date/Tim", command=toggle_date_time)
toggle_button.place(x = 5,y = 50)

# Start updating the display
update_display()


root.mainloop()

