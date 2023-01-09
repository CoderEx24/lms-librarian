from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.app import App
from os import path
import requests
import json

Builder.load_file(path.join(path.dirname(__file__), 'mainscreen.kv'))

class BorrowBook(Popup):
    borrower_username = StringProperty()
    checker_username = StringProperty()
    date_of_retrival = StringProperty()
    book_id = NumericProperty()

    def borrow_book(self):
        token = App.get_running_app().token
        headers = {'Authorization': f'Token {token}'}
        data = {'borrower': self.borrower_username, 
                'checker_username': self.checker_username,
                'date_of_retrival': self.date_of_retrival}

        res = requests.post(f'http://127.0.0.1:8000/api/books/{int(self.book_id)}/borrow/',
                           headers=headers, data=data)

        if res.status_code != 200:
            self.ids['err_msg'].text = res.text
            return

        self.dismiss()


class MainScreen(Screen):
    
    record_id = NumericProperty()

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
        
        records_list.refresh_from_data()
            
    def return_book(self):
        token = App.get_running_app().token
        headers = {'Authorization': f'Token {token}'}
        data = {'record_id': int(self.record_id)}
        
        res = requests.post('http://127.0.0.1:8000/api/books/return/', data=data, headers=headers)

        if res.status_code != 200:
            self.ids['err_msg'].text = res.text

    def init_user_info(self):
        token = App.get_running_app().token
        headers = {'Authorization': f'Token {token}'}

        res = requests.get('http://127.0.0.1:8000/api/customer/', headers=headers)

        parsed_data = json.loads(res.text)
        user_records = self.ids['customers_records']

        user_records.data.clear()

        for record in parsed_data:
            user_id = record['user']['id']
            username = record['user']['username']
            allowed_to_borrow = record['allowed_to_borrow']

            user_records.data.append({ 'text': f'{user_id} | {username} | {allowed_to_borrow}' })

        user_records.refresh_from_data()
            
