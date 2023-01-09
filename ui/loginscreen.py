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
            err_content = Label(text=f'An error occured\n{response.content}', size=(100, 100))
            err_msg = Popup(title='Error', content=err_content, auto_dismiss=True)
            err_msg.open()


