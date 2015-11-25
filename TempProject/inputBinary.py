''' XOR Operation '''

# Core Concepts of Funny Windows
'''
# Test the Binary Inputs
binary1 = input('Enter Ans for image 1 in 0, 1, 2:')
binary2 = input('Enter Ans for Image 2 in 0, 1, 2:')

answer = 02111120

result = binary1 + binary2

if answer == result:
	print "success"
else:
	print "WRONG"

TODO:
list to get each value of the binary values which correspond to specify Windows
'''

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
from kivy.uix.textinput import TextInput



# To load the Specific KV file
Builder.load_file('Binary.kv')

class MainScreen(Screen):
    txt1 = ObjectProperty(None)
    txt2 = ObjectProperty(None)
    btn1 = ObjectProperty(None)
    result_Label = ObjectProperty(None)

    def Result(self, a, b):
        result = []
        for i in range(len(a)):
            result.append(a[i] + b[i])
        return result
        
    def buttonClicked(self):
    	input1 = self.txt1.text
        input2 = self.txt2.text
        list1 = []
        list2 = []
        for digit in input1:
            list1.append(int(digit))

        for digit in input2:
            list2.append(int(digit))

        answer_User = self.Result(list1, list2)
        user_string = "".join(str(x) for x in answer_User)
        self.result_Label.text = "Your addition result is " + user_string

        
        

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

