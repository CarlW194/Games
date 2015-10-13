'''
Application from .kv in a template Directory
===================================

this example shows how you can change the directory for the .kv file. You
should see "Hello from the template1/test.kv" as a button.

As kivy instantiates the TestApp subclass of App, the variable kv_directory 
if set. Kivy the implicitly searches for a .kv file matching the name 
of the subclass in that directory, finding the file template1/test.kv. That 
file contains the root widget.

'''

import kivy
kivy.require('1.9.0')

from kivy.app import App

class TestApp(App):
	kv_directory = 'template1'
	
if __name__ == '__main__':
	 TestApp().run()