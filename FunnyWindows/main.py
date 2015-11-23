import kivy

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.vector import Vector
from kivy.graphics import Color

# To default to fullscreen
#Window.fullscreen = True
#need to builder the kivy file before anything for Screen Manager
Builder.load_file('FunnyWindows.kv')

# Declare both screens
class MenuScreen(Screen):
    pass

class Game01Screen(Screen):
    pass

class LeftBoatViewScreen(Screen):
    pass

class EmptyBoatScreen(Screen):
	c1 = ObjectProperty(None)
	c2 = ObjectProperty(None)
	c3 = ObjectProperty(None)
	c4 = ObjectProperty(None)
	c5 = ObjectProperty(None)
	c6 = ObjectProperty(None)
	c7 = ObjectProperty(None)
	c8 = ObjectProperty(None)



	
class Circle1(Widget):
	def on_touch_down(self, touch):
		with self.canvas.before:
			Color(0, 3, 0, 3)

class Circle2(Widget):
	def on_touch_down(self, touch):
		with self.canvas.before:
			Color(0, 9, 0, 9)

class Circle3(Widget):
	def on_touch_down(self, touch):
		with self.canvas.before:
			Color(0, 4, 0, 4)

class Circle4(Widget):
	def on_touch_down(self, touch):
		with self.canvas.before:
			Color(0, 6, 0, 6)

class Circle5(Widget):
	def on_touch_down(self, touch):
		with self.canvas.before:
			Color(0, 18, 0, 18)

class Circle6(Widget):
	def on_touch_down(self, touch):
		with self.canvas.before:
			Color(0, 15, 0, 15)

class Circle7(Widget):
	def on_touch_down(self, touch):
		with self.canvas.before:
			Color(0, 12, 0, 12)

class Circle8(Widget):
	def on_touch_down(self, touch):
		with self.canvas.before:
			Color(0, 19, 0, 19)

class FinishScreen(Screen):
	def on_touch_down(self, touch):
		with self.canvas.before:
			Color(0, 7, 0, 7)

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Game01Screen(name='game01'))
sm.add_widget(LeftBoatViewScreen(name='leftboatview'))
sm.add_widget(EmptyBoatScreen(name='emptyboat'))
sm.add_widget(FinishScreen(name='finish'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()