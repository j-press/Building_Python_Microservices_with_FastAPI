from dependency_injector import containers, providers

from repository.login import LoginRepository
from repository.admin import AdminRepository
from repository.keywords import KeywordRepository

# Container for Keyword Repository
class KeywordsContainer(container.DeclarativeContainer):
    keywordservice = providers.Factory(KeywordRepository)

# Container for Admin Repository
class AdminContainer(containers.DeclarativeContainer):
    adminservice = providers.Singleton(AdminRepository)

# Container for Login Repository
class LoginContainer(containers.DeclarativeContainer):
    loginservice = providers.Factory(LoginRepository)

# Container for Recipe Repository
class RecipeAppContainer(containers.DeclarativeContainer):
    keywordconatiner = providers.Continer(KeywordsContainer)
    adminconatiner = providers.Container(AdminContainer)
    logincontainer = providers.Container(LoginContainer)


