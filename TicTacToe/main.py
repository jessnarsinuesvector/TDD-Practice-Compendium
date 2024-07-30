# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TicTacToe.src.input_controller import InputController
from TicTacToe.src.result_checker import ResultChecker

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TicTacToe.src.gui import GUI

if __name__ == '__main__':

    slot_state = [""] * 9
    input_controller = InputController(slot_state)
    result_checker = ResultChecker(input_controller)
    gui = GUI(input_controller, result_checker)
    gui.draw_elements_on_canvas(gui.create_canvas())
    gui.window.mainloop()