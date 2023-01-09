from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.app import App
import requests
import time
from os import path

Builder.load_file(path.join(path.dirname(__file__), 'loginscreen.kv'))

class LoginScreen(Screen):
    username = StringProperty()
    password = StringProperty()

    def login(self):
        data = { 'username': self.username, 'password': self.password }
        response = requests.post('http://127.0.0.1:8000/api/librarian/login/', data)

        if response.status_code != 200:
            self.ids['err_msgs'].text = response.text
            return False

        App.get_running_app().token = response.text[7:-1]
        return True

