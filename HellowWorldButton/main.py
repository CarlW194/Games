'''
Application example using build() + return
=========================================
and application can be built if you return a widget on build(), or if you set self.root.
'''

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
	def build(self):
		#return a Button() as a root widget
		return Button(text='hello world')
		
if __name__ =='__main__':
	TestApp().run()