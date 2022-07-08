from tkinter import *
from cells import cell
import settings
import utils

root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.width,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

centre_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
centre_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)



for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c1 = cell(x, y)
        c1.create_btn_obj(centre_frame)
        c1.cell_btn_obj.grid(
            column=x, row=y
        )

cell.crete_cell_count_lable(left_frame)
cell.cell_count_label_obj.place(
    x=15, y=0
)
cell.create_cell_title(top_frame)
cell.cell_title.place(
    x=300, y=30
)

cell.randomize_mines()


root.mainloop()