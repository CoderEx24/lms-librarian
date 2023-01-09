from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.app import App
from os import path
import requests
import json

Builder.load_file(path.join(path.dirname(__file__), 'mainscreen.kv'))

class MainScreen(Screen):
    
    record_id = NumericProperty()

    def refresh(self):
        token = App.get_running_app().token
        headers = {'Authorization': f'Token {token}'}
        
        res = requests.get('http://127.0.0.1:8000/api/librarian/borrow/', headers=headers) 
        parsed_data = json.loads(res.text)
        
        records_list = self.ids['borrow_records']
        records_list.data.clear()
        records_list.refresh_from_data()

        for record in parsed_data:
            borrow_id = record['id']
            borrower = record['borrower']['user']['username']
            checker = record['checker']['user']['username']
            book_title = record['book']['title']
            date_of_borrowing = record['date_of_borrowing']
            date_of_retrival = record['date_of_retrival']

            records_list.data.append({ 'text': f'{borrow_id} | {borrower} | {checker} | {book_title} | {date_of_borrowing} | {date_of_retrival}' })
            
    def return_book(self):
        token = App.get_running_app().token
        headers = {'Authorization': f'Token {token}'}
        data = {'record_id': int(self.record_id)}
        
        res = requests.post('http://127.0.0.1:8000/api/books/return/', data=data, headers=headers)

        if res.status_code != 200:
            self.ids['err_msg'].text = res.text


