from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import os

Builder.load_file('button.kv')

class MyLayout(Widget):
    # def press(self):
    #     os.system('python snake.py')
    pass


class FirstApp(App):
    def build(self):
        Window.clearcolor = (137/255,196/255,244/255,1)
        return MyLayout()


if __name__ == '__main__':
    FirstApp().run()