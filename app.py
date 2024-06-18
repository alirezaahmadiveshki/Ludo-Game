# library importing
from tkinter import *
import tkinter.font as tkFont
from time import sleep
from random import randint



def making_new_window(color):
    # root window configurment
    root = Tk()
    root.title("ludo game")
    root.geometry("1100x700")
    root.minsize(1100,700)


    # fonts
    _font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)


    # making frames and devideing the root
    places_frame = Frame(root, bg="#d2b589",bd=1 , relief="ridge")
    button_frame = Frame(root, bg='lavender',bd=1 , width=370, relief="ridge")
    screen_frame = Frame(root, bg="lavender",bd=1 , width=370, relief="ridge")


    # placing main frames
    places_frame.pack(padx=12, pady=12, side="left", expand=True, fill="both")
    screen_frame.pack(padx=12, pady=12, expand=True, fill="both")
    button_frame.pack(padx=12, pady=12, expand=True, fill="both")



    # grid placing the places in the places_frame
    for i in range(11):
        places_frame.rowconfigure(i, weight=1)
    for i in range(11):
        places_frame.columnconfigure(i, weight=1)




    Label(places_frame, bg="#6190f1").grid(row=0, column=6, sticky="nswe", padx=15, pady=15)
    Label(places_frame, bg="#fb9977").grid(row=4, column=0, sticky="nswe", padx=15, pady=15)
    Label(places_frame, bg="#8af096").grid(row=6, column=10, sticky="nswe", padx=15, pady=15)
    Label(places_frame, bg="#d2cd21").grid(row=10, column=4, sticky="nswe", padx=15, pady=15)


    white_places = [(0,4),(1,4),(2,4),(3,4),(4,4),(6,4),(7,4),(8,4),(9,4),(5,0),(5,10),(10,5),(0,5),(1,6),(2,6),(3,6),(4,6),(10,6),(6,6),(7,6),(8,6),(9,6),
                    (4,1),(4,2),(4,3),(4,4),(4,10),(4,6),(4,7),(4,8),(4,9),(6,0),(6,1),(6,2),(6,3),(6,4),(6,6),(6,7),(6,8),(6,9)]
    for s in white_places:
        Label(places_frame, bg="snow").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)


    red_places = [(0,0), (0,1), (1,0), (1,1), (5,1),(5,2),(5,3),(5,4)]
    for s in red_places:
        Label(places_frame, bg="#eb0d06").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)



    green_places = [(9,9), (9,10), (10,9), (10,10), (5,6),(5,7),(5,8),(5,9)]
    for s in green_places:
        Label(places_frame, bg="#0f8005").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)


    blue_places = [(0,9), (0,10), (1,9), (1,10), (1,5), (2,5), (3,5), (4,5)]
    for s in blue_places:
        Label(places_frame, bg="#0203f6").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)


    yellow_places = [(9,0), (9,1), (10,0), (10,1), (6,5), (7,5), (8,5), (9,5)]
    for s in yellow_places:
        Label(places_frame, bg="#f7fb07").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)



    # headings
    button_frame_label = Label(master=button_frame, text="Function Buttons", height=3, bd=2, relief="ridge", bg="gray87")
    screen_frame_label = Label(master=screen_frame, text="Status", height=3, bd=2, relief="ridge", bg="gray87")
    button_frame_label.pack(fill="x")
    screen_frame_label.pack(fill="x")


    # main buttons frame
    main_button_frame = Frame(master=button_frame, width=370, bg="lavender")
    main_button_frame.pack(expand=True, fill="both")



    # main status frame
    states = Frame(master=screen_frame, width=370, bg="lavender")
    states.pack(expand=True, fill="both")



    def die():
        return randint(1,6)
        


    green_movement_places = [(6,10),(6,6),(6,7),(6,8),(6,9),(7,6),(8,6),(9,6),(10,6),(10,5),(10,4),(6,4),(7,4),(8,4),(9,4),(6,0),(6,1),(6,2),(6,3),(5,0)
                             ,(4,0),(4,1),(4,2),(4,3),(4,4),(0,4),(1,4),(2,4),(3,4),(0,5),(0,6),(1,6),(2,6),(3,6),(4,6),(4,7),(4,8),(4,9),(4,10),(5,10),(5,9),(5,8),(5,7),(5,6)]



    red_movement_places = [(4,0),(4,1),(4,2),(4,3),(4,4),(0,4),(1,4),(2,4),(3,4),(0,5),(0,6),(1,6),(2,6),(3,6),(4,6),(4,7),(4,8),(4,9),(4,10),(5,10),
                           (6,10),(6,6),(6,7),(6,8),(6,9),(7,6),(8,6),(9,6),(10,6),(10,5),(10,4),(6,4),(7,4),(8,4),(9,4),(6,0),(6,1),(6,2),(6,3),(5,0)
                           (5,1),(5,2),(5,3),(5,4)]

    

    root.mainloop()






 

def your_color():
    root = Tk()
    root.geometry("600x100")
    root.minsize(300, 400)
    _font = tkFont.Font(family="Arial", size=25, weight=tkFont.BOLD)


    def green_button_function():
        root.destroy()
        making_new_window("green")

        


    def red_button_function():
        root.destroy()
        making_new_window("red")



    _label = Label(master=root, text="Choose your color: ", font=_font, height=1)
    button_frame = Frame(master=root)
    green_button =  Button(master=button_frame, text="green", bg = "#0f8005", command=green_button_function, fg="white", font=tkFont.Font(family="Arial", size=20, weight=tkFont.BOLD))
    red_button =  Button(master=button_frame, text="red", bg = "#eb0d06", command=red_button_function, fg="white", font=tkFont.Font(family="Arial", size=20, weight=tkFont.BOLD))

    _label.pack(fill="x" , pady=80)
    button_frame.pack(expand=True, fill="both", padx=40, pady=50)
    green_button.pack(side="left", expand=True, fill="both")
    red_button.pack(side="left", expand=True, fill="both")
    root.mainloop()






if __name__ == "__main__":
    your_color()
