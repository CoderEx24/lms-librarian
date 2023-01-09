from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager
from ui import *

class MainApp(App):
    token = StringProperty()

if __name__ == '__main__':
    MainApp().run()

