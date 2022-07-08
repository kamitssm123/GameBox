import ctypes
from tkinter import Button, Label, messagebox
import random
import settings
import sys


class cell():
    all = []
    cell_count = settings.cell_count
    cell_count_label_obj = None
    cell_title = None
    def __init__(self,x ,y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_obj = None
        self.x = x
        self.y = y

        cell.all.append(self)

    def create_btn_obj(self, location):
        btn = Button(
            location,
            bg='grey',
            width=6,
            height=2,
            # text=f'{self.x}, {self.y}'
        )
        btn.bind('<Button-1>', self.left_click_action) #left_click
        btn.bind('<Button-3>', self.right_click_action) #right_click
        self.cell_btn_obj = btn

    @staticmethod
    def crete_cell_count_lable(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{cell.cell_count}",
            font=("", 25)
        )
        cell.cell_count_label_obj = lbl

    @staticmethod
    def create_cell_title(location):
        lbl1 = Label(
            location,
            bg='black',
            fg='white',
            text=f"MineSweeper",
            font=("", 50),
        )
        cell.cell_title = lbl1


    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_mine_count == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()

            self.show_cell()

    def get_cell_by_axis(self, x, y):
        for cel in cell.all:
            if cel.x==x and cel.y==y:
                return cel

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y -1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cel for cel in cells if cel is not None]
        return cells

    @property
    def surrounded_mine_count(self):
        counter = 0
        for cel in self.surrounded_cells:
            if cel.is_mine:
                counter += 1

        return counter


    def show_cell(self):
        if not self.is_opened:
            cell.cell_count -= 1
            self.cell_btn_obj.configure(
                text=self.surrounded_mine_count,
                # bg='white'
            )
            if cell.cell_count_label_obj:
                cell.cell_count_label_obj.config(
                    text=f"Cells Left:{cell.cell_count}"
                )
        self.is_opened = True

        self.cell_btn_obj.configure(
            bg='white'
        )

    def show_mine(self):
        self.cell_btn_obj.configure(bg="red")
        messagebox.showerror("Game Over", "Amit")
        sys.exit()

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_obj.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_obj.configure(
                bg='grey'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            cell.all, settings.mine_count
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    def __repr__(self):
        return f"cell({self.x}, {self.y})"
