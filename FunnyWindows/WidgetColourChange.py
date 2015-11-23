from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file('WidgetColourChange.kv')



class MyPaintWidget(Widget):
    def add_global():
        global num_pressed

    c1 = ObjectProperty(None)
    c2 = ObjectProperty(None)
    def new(self):
        with self.c1.canvas:
            if num_pressed == 0:
                Color(.5, .5, .5)
                num_pressed = num_pressed + 1
                print num_pressed
            elif num_pressed == 1:
                Color(0, 0, 0)
                num_pressed = num_pressed + 1
            elif num_pressed == 2:
                Color(5, 5, 5)
                num_pressed = 0
            else:
                num_pressed = 0
            #black
                Color(0, 0, 0)
            #Grey
            '''Color(.5, .5, .5)'''
            #white
            '''Color(5, 5, 5)'''

class Circle1(Widget):
    pass

class Circle2(Widget):
    pass

class MyPaintApp(App):

    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()