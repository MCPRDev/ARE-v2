import query
from outfuctions import *

class loggin_gui_action():
    def __init__(self):
        self.query = query.Postgresqueries()
    
    def log_button_action(self, username, password):
        if not clear_entry_data(username) or not clear_entry_data(password):
            return False
        
        if self.query.login(username, password):
            return True
    

    
