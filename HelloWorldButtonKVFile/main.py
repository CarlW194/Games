'''
Application built from a .kv file
===========================

this shows how to implicitly use a .kv file fro your application. You
should see a full screen button labelled "Hello from test.kv".

after Kivy instantiates a subclass of App, it implicitly searches for a .kv
file. The file test.kv is selected because the name of the subclass of App is TestApp, 
which implies that kivy should try to load "test.kv". That file containes a root widget.
'''

import kivy
kivy.require('1.9.0')

from kivy.app import App

class TestApp(App):
	pass
	
if __name__ == '__main__':
	TestApp().run()
	
	