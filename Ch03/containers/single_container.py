from dependency_injector import containers, providers 

from repository.users import login_details
from repository.login import LoginRepository
from repository.admin import AdminRepository
from repository.keywords import KeywordRepository
from service.recipe_utilities import get_recipe_names

# Container for for all services 
class Container(containers.DeclarativeContainer):
    # Container for Login Service 
    loginservcie = providers.Factory(LoginRepository)
    # Container for Admin Service
    adminservice = providers.Singleton(AdminRepository)
    # Container for Keyword Service
    keywordseervice = providers.Factory(KeywordRepository)
    # Container for Recipe Service
    recipe_util = providers.Callable(get_recipe_names)
    # Container for Login Details
    login_repo = providers.Dict(login_details)
