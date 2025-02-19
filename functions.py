import query
from outfuctions import *

class loggin_gui_action():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def log_button_action(self, username, password):
        if not clear_entry_data(username) or not clear_entry_data(password):
            return False, None
        
        login_success, access_type = self.query.login(username, password)

        if login_success:
            return True, access_type
        
        return False, None
    

class subject_gui_action():
    def __init__(self):
        self.query = query.Postgresqueries()
    def add_subject_button_action(self, subject):
        if not validate_and_clean_subject_entry_query(subject):
            return False
        
        if self.query.insert_subject(subject) == False:
            return False
        
        self.query.show_data_subjects()
        return True