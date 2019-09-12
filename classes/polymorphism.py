from abc import ABC, abstractmethod


class UIControler(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControler):
    def draw(self):
        print('TextBox')


class DropDownList(UIControler):
    def draw(self):
        print('Dropdownlist')


def draw(controls):
    for control in controls:
        control.draw()


dropdown = DropDownList()
textbox = TextBox()
draw([dropdown,textbox])
