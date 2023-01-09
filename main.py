from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager

class MainApp(App):
    token = StringProperty()

if __name__ == '__main__':
    MainApp().run()

