from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from os import path

Builder.load_file(path.join(path.dirname(__file__), 'mainscreen.kv'))

class MainScreen(Screen):
    def refresh(self):
        borrow_records_list = self.ids['borrow_records']
        borrow_records_list.data.append({'text': 'tept'})

