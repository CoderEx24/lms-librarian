from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
from os import path
import requests
import json

Builder.load_file(path.join(path.dirname(__file__), 'mainscreen.kv'))

class MainScreen(Screen):
    def refresh(self):
        token = App.get_running_app().token
        headers = {'Authorization': f'Token {token}'}
        
        res = requests.get('http://127.0.0.1:8000/api/librarian/borrow/', headers=headers) 
        parsed_data = json.loads(res.text)
        
        records_list = self.ids['borrow_records']
        records_list.data.clear()
        for record in parsed_data:
            borrow_id = record['id']
            borrower = record['borrower']['user']['username']
            checker = record['checker']['user']['username']
            book_title = record['book']['title']
            date_of_borrowing = record['date_of_borrowing']
            date_of_retrival = record['date_of_retrival']

            records_list.data.append({ 'text': f'{borrow_id} | {borrower} | {checker} | {book_title} | {date_of_borrowing} | {date_of_retrival}' })
            


