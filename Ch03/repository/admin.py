# Import User from Repository
from repository.users import login_details, user_profiles
from repository.login import logs_vistor

# Admin Repository
class AdminRepository:
    def __init__(self):
        pass 
    # Get all login details
    def query_login_details(self):
        return list(login_details.values())

    # Get all user profiles
    def query_user_profiles(self):
        return list(user_profiles.values())

    # Get all logs
    def query_logs_vistor(self):
        return list(logs_vistor.values())