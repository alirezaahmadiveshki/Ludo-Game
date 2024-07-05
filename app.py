# library importing
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from random import randint
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage


# ------------ the class of the pieces in the board ----------- #
# the red and green pieces
# the moving buttons in the board


class Green:
    # storing the green piece data
    def __init__(self) -> None:
        self.pos = 0  # using property
        self.color = "green"
        # the coordinates in the grid
        self.green_movement_places = [(6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (10, 5),
                                      (10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (5, 0),
                                      (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4), (0, 5),
                                      (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 10),
                                      (5, 9), (5, 8), (5, 7), (5, 6)]
        self.winner = False

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, new_pos):
        # the green movement places list's length is 44
        # indexes are between 0 and 43
        if new_pos >= 44:
            pass
        elif 40 <= new_pos <= 43:
            self._pos = new_pos
            self.winner = True  # using this in the rolling_dice function
        else:
            self._pos = new_pos

    # returns the coordinate of given position
    def place(self) -> tuple[int, int]:
        return self.green_movement_places[self.pos]

    def image(self) -> PhotoImage:
        # initializing the pawn picture(it doesn't move)
        # it's just decorative
        green_peace_img = Image.open('green_piece.png')
        green_peace_img = green_peace_img.resize((8, 18))
        green_peace_img = ImageTk.PhotoImage(green_peace_img)
        return green_peace_img


class Red:
    # storing the red piece data
    def __init__(self) -> None:
        self._pos = 0
        self.color = "red"
        # the coordinates in the grid
        self.red_movement_places = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4), (0, 5),
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 10),
                                    (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (10, 5),
                                    (10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (5, 0),
                                    (5, 1), (5, 2), (5, 3), (5, 4)]
        self.winner = False

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, new_pos):
        # the green movement places list's length is 44
        # indexes are between 0 and 43
        if new_pos >= 44:
            pass
        elif 40 <= new_pos <= 43:
            self._pos = new_pos
            self.winner = True  # using this in the rolling_dice function
        else:
            self._pos = new_pos

    def place(self) -> tuple[int, int]:
        return self.red_movement_places[self.pos]

    def image(self) -> PhotoImage:
        # initializing the pawn picture(it doesn't move)
        # it's just decorative
        red_peace_img = Image.open('red_piece.png')
        red_peace_img = red_peace_img.resize((8, 18))
        red_peace_img = ImageTk.PhotoImage(red_peace_img)
        return red_peace_img


# Our Button Collector
# the attributes are added through the object
# for storing the temporary button of green and red piece
class OurButton:
    def __init__(self) -> None:
        pass

    # -------------- The Windows ------------- #


def your_color() -> None:
    """the panel that you choose your team;
    your team is either red or green
    and then based on your choice
    the ludo board window is invoked with the chosen color as input
    """

    # --------- configuring the window ----------#
    root = Tk()
    root.geometry("600x100")
    root.minsize(300, 400)

    # --------- the button functions ----------#
    def green_button_function() -> None:
        root.destroy()  # destroying the current window and invoke the main one
        making_new_window("green")  # the input is your team

    def red_button_function() -> None:
        root.destroy()  # destroying the current window and invoke the main one
        making_new_window("red")  # the input is your team

    _label = Label(master=root, text="Choose your color: ",
                   font=tkFont.Font(family="Arial", size=25, weight=tkFont.BOLD), height=1)
    _label.pack(fill="x", pady=80)

    button_frame = Frame(master=root)
    button_frame.pack(expand=True, fill="both", padx=40, pady=50)

    green_button = Button(master=button_frame, text="green", bg="#0f8005", command=green_button_function, fg="white",
                          font=tkFont.Font(family="Arial", size=20, weight=tkFont.BOLD))
    green_button.pack(side="left", expand=True, fill="both")
    red_button = Button(master=button_frame, text="red", bg="#eb0d06", command=red_button_function, fg="white",
                        font=tkFont.Font(family="Arial", size=20, weight=tkFont.BOLD))
    red_button.pack(side="left", expand=True, fill="both")

    root.mainloop()


def making_new_window(color: str) -> None:
    """
    makes the board of the ludo game
    and also controlling the flow of the game

    :param color: the chosen color (your team) in your_color function
    :type color: String
    """
    # ------------ making the bases of our board ------------ #

    # root window configure
    root = Tk()
    root.title("ludo game")
    root.geometry("1100x700")
    root.minsize(1100, 700)

    # making frames and dividing the root window
    places_frame = Frame(root, bg="#d2b589", bd=1, relief="ridge")
    button_frame = Frame(root, bg='lavender', bd=1, width=370, relief="ridge")
    screen_frame = Frame(root, bg="lavender", bd=1, width=370, relief="ridge")

    # placing main frames
    places_frame.pack(padx=12, pady=12, side="left", expand=True, fill="both")
    screen_frame.pack(padx=12, pady=12, expand=True, fill="both")
    button_frame.pack(padx=12, pady=12, fill="both")

    # grid placing the places in the places_frame
    for i in range(11):
        places_frame.rowconfigure(i, weight=1)
    for i in range(11):
        places_frame.columnconfigure(i, weight=1)

    # --------- initializing our pieces --------- #

    # green piece
    green = Green()
    # the pawn image in the starting place for green piece
    green_piece_img = green.image()

    # red piece
    red = Red()
    # the pawn image in the starting place for red piece
    red_piece_img = red.image()

    # ----------- coloring the Ludo Board ------------ #

    # coloring start places on the screen
    Label(places_frame, bg="#6190f1").grid(row=0, column=6, sticky="nswe", padx=15, pady=15)
    Label(places_frame, bg="#fb9977", image=red_piece_img).grid(row=4, column=0, sticky="nswe", padx=15,
                                                                pady=15)  # notice the inserted image
    Label(places_frame, bg="#8af096", image=green_piece_img).grid(row=6, column=10, sticky="nswe", padx=15,
                                                                  pady=15)  # notice the inserted image
    Label(places_frame, bg="#d2cd21").grid(row=10, column=4, sticky="nswe", padx=15, pady=15)

    white_places = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (6, 4), (7, 4), (8, 4), (9, 4), (5, 0), (5, 10), (10, 5),
                    (0, 5), (1, 6), (2, 6), (3, 6), (4, 6), (10, 6), (6, 6), (7, 6), (8, 6), (9, 6),
                    (4, 1), (4, 2), (4, 3), (4, 4), (4, 10), (4, 6), (4, 7), (4, 8), (4, 9), (6, 0), (6, 1), (6, 2),
                    (6, 3), (6, 4), (6, 6), (6, 7), (6, 8), (6, 9)]
    for s in white_places:
        Label(places_frame, bg="snow").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)

    red_places = [(0, 0), (0, 1), (1, 0), (1, 1), (5, 1), (5, 2), (5, 3), (5, 4)]
    for s in red_places:
        Label(places_frame, bg="#eb0d06").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)

    green_places = [(9, 9), (9, 10), (10, 9), (10, 10), (5, 6), (5, 7), (5, 8), (5, 9)]
    for s in green_places:
        Label(places_frame, bg="#0f8005").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)

    blue_places = [(0, 9), (0, 10), (1, 9), (1, 10), (1, 5), (2, 5), (3, 5), (4, 5)]
    for s in blue_places:
        Label(places_frame, bg="#0203f6").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)

    yellow_places = [(9, 0), (9, 1), (10, 0), (10, 1), (6, 5), (7, 5), (8, 5), (9, 5)]
    for s in yellow_places:
        Label(places_frame, bg="#f7fb07").grid(row=s[0], column=s[1], sticky="nswe", padx=15, pady=15)

    # headings
    button_frame_label = Label(master=button_frame, text="Function Buttons", height=3, bd=2, relief="ridge",
                               bg="gray87")
    screen_frame_label = Label(master=screen_frame, text="Status", height=3, bd=2, relief="ridge", bg="gray87")
    button_frame_label.pack(fill="x")
    screen_frame_label.pack(fill="x")

    # ---------------- status frame ---------------- #

    # making the frame and it's gridlines
    status = Frame(master=screen_frame, width=370, bg="lavender")
    status.pack(expand=True, fill="both")
    status.rowconfigure(0, weight=1)
    status.rowconfigure(1, weight=2)
    status.rowconfigure(2, weight=1)
    status.rowconfigure(3, weight=2)

    # making the dice images' objects that will show in status frame
    dice_1 = Image.open("dice1.jpg")
    dice_1 = ImageTk.PhotoImage(dice_1)
    dice_2 = Image.open("dice2.jpg")
    dice_2 = ImageTk.PhotoImage(dice_2)
    dice_3 = Image.open("dice3.jpg")
    dice_3 = ImageTk.PhotoImage(dice_3)
    dice_4 = Image.open("dice4.jpg")
    dice_4 = ImageTk.PhotoImage(dice_4)
    dice_5 = Image.open("dice5.jpg")
    dice_5 = ImageTk.PhotoImage(dice_5)
    dice_6 = Image.open("dice6.jpg")
    dice_6 = ImageTk.PhotoImage(dice_6)
    dices = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]

    # the first two row of the status frame
    def your_dice(your_team, your_num: int) -> None:
        # the label
        # background is based on your team's color
        Label(master=status, text="your dice", bg=f"{your_team.color}",
              font=tkFont.Font(family="Cascadia Code", size=22, weight=tkFont.BOLD)).grid(row=0, sticky='nesw')
        # the image
        # your_num : the number of the rooling dice
        dice_img = dices[your_num - 1]
        Label(master=status, image=dice_img).grid(row=1)

        # the second two row of the status frame

    def opponent_dice(opponent_team, opponent_num: int) -> None:
        # the label
        # background is based on your team's color
        Label(master=status, text=f"opponent's dice", bg=f"{opponent_team.color}",
              font=tkFont.Font(family="Cascadia Code", size=19, weight=tkFont.BOLD)).grid(row=2, sticky='nesw',
                                                                                          ipadx=65)
        # the image
        # your_num : the number of the rooling dice
        dice_img = dices[opponent_num - 1]
        Label(master=status, image=dice_img).grid(row=3)

        # --------------------- GAME ------------------- #

    # the buttons that move in the board
    button = OurButton()
    button.your_button = Button(master=places_frame)
    button.opponent_button = Button(master=places_frame)

    # choosing which team you are
    # and which team is your opponent
    if color.lower() == 'green':
        your_team = green
        opponent_team = red
    else:
        your_team = red
        opponent_team = green

    def rolling_dice() -> None:
        """controlling the flow of the game
        invokes when you hit the dice button
        """
        # destroying the previous button
        button.your_button.destroy()
        button.opponent_button.destroy()

        # -------- your action ------------#

        your_num = randint(1, 6)

        your_dice(your_team, your_num)  # for status Frame

        your_team.pos += your_num  # the index
        pos = your_team.place()  # the coordinate

        # making our piece using buttons
        button.your_button = Button(master=places_frame, bg=your_team.color)
        button.your_button.grid(row=pos[0], column=pos[1], sticky='nwse')

        # showing the winner using the messagebox
        # ending the game
        # if in the self._pos property the self.winner attribute is changed to True
        if your_team.winner:
            messagebox.showinfo("winner", f"you({your_team.color}) won")
            root.destroy()
            return

        # ------- opponent's action ------- #

        opponent_num = randint(1, 6)

        opponent_dice(opponent_team, opponent_num)  # for status frame

        opponent_team.pos += opponent_num  # the index
        pos = opponent_team.place()  # the coordinate

        # making our piece using buttons
        button.opponent_button = Button(master=places_frame, bg=opponent_team.color)
        button.opponent_button.grid(row=pos[0], column=pos[1], sticky='nwse')

        # showing the winner using the messagebox
        # ending the game
        # if in the self._pos property the self.winner attribute is changed to True
        if opponent_team.winner:
            messagebox.showinfo("winner", f"opponent({opponent_team.color}) won")
            root.destroy()
            return

    # -------------- the Button Frame ----------- #

    # main buttons frame
    main_button_frame = Frame(master=button_frame, width=370, bg="lavender")
    main_button_frame.pack(expand=True, fill="both")
    Button(master=main_button_frame, text="dice", command=rolling_dice, height=2,
           font=tkFont.Font(family="Cascadia Code", size=20, weight=tkFont.BOLD), activebackground='tomato', bg='red3',
           fg='white').pack(expand=True, fill='both')

    root.mainloop()


if __name__ == "__main__":
    your_color()
