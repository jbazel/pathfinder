import random
import numpy as np
from tkinter import *
import time

global WIDTH
global HEIGHT
global CITY


global OUTLINE
global BACKGROUND
global WALL
global START_COLOUR
global GOAL_COLOUR
global FRINGE_COLOUR
global PATH_COLOUR

OUTLINE = "#151F30"
BACKGROUND = "white"
WALL = "#151F30"
START_COLOUR = "green"
GOAL_COLOUR = "#BD2A2E"
FRINGE_COLOUR = "#FF7A48"
PATH_COLOUR = "#E3371E"




def start_event(e):
    x = e.x // 20
    y = e.y // 20

    global START
    START = (x, y)

    if 2 not in CITY:
        canvas.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill=START_COLOUR, outline=OUTLINE)
        CITY[x][y] = 2
        print(e.x, 500 - e.y)


def goal_event(e):
    x = e.x // 20
    y = e.y // 20

    if 2 not in CITY and 3 not in CITY:
        canvas.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill=START_COLOUR, outline=OUTLINE)
        CITY[x][y] = 2
        global START
        START = (x, y)

    elif 3 not in CITY:
        canvas.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill=GOAL_COLOUR, outline=OUTLINE)
        CITY[x][y] = 3
        global GOAL
        GOAL = (x, y)

def path_event(e):
    x = e.x // 20
    y = e.y // 20
    print(x, y)
    if CITY[x][y] == 0:
        CITY[x][y] = 1
        canvas.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill=WALL, outline=OUTLINE)

def paint(to_paint, colour):
    if to_paint != START and to_paint != GOAL:
        canvas.create_rectangle(to_paint[0] * 20, to_paint[1] * 20, to_paint[0] * 20 + 20, to_paint[1] * 20 + 20, fill=colour, outline=OUTLINE)
        canvas.update()
def A_star(e):
    print("A*")
    start = (START, np.inf, None)
    goal = (GOAL, 0, None)
    open_list = []
    closed_list = []

    def h(a, b):
        manhattan = np.abs(a[0] - b[0]) + np.abs(a[1] - b[1])
        diag_dist = min(np.abs(a[0] - b[0]), np.abs(a[1] - b[1]))
        return manhattan + (np.sqrt(2) - 2) * diag_dist

    open_list.append(start)
    while open_list:
        open_list.sort(key=lambda x: x[1])
        node = open_list.pop(0)
        paint(node[0], FRINGE_COLOUR)

        closed_list.append(node[0])
        if node[0] == goal[0]:
            print("found")
            while node[2] is not None:
                time.sleep(0.05)
                node = node[2]
                paint(node[0], PATH_COLOUR)
            return

        else:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 and j == 0 or i == 0 and j != 0:
                        try:
                            current_node = (node[0][0] + i, node[0][1] + j)
                            if CITY[current_node[0]][current_node[1]] != 1:
                                current_node = (current_node, h(current_node, GOAL) + 1, node)
                                if current_node[0] not in closed_list:
                                    open_list.append(current_node)

                        except IndexError:
                            pass
    print("not found")


def main():
    global CITY
    CITY = np.zeros((25, 25))
    app = Tk()
    app.geometry("500x500")

    global canvas
    canvas = Canvas(app, width=500, height=500, bg="black")
    canvas.pack(anchor="nw")

    for i in range(25):
        for j in range(25):
            canvas.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill=BACKGROUND, outline=OUTLINE)






    # canvas.bind("<Button-1>", start_event)
    canvas.bind("<Double-Button-1>", goal_event)
    canvas.bind("<B1-Motion>", path_event)
    canvas.bind("<Button-2>", A_star)

    app.title("pathfinder")

    app.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
