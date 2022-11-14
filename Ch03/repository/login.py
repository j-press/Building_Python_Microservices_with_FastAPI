from datetime import date 

# Dict to store all the logs for visitors
logs_vistor = dict()

class LoginRepository:
    def __init__(self):
        pass 

    def login_audit(self, username: str, password: str):
        logs_vistor[username] = date.today()