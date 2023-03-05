import configparser
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(current_dir, 'properties.ini')
config = configparser.RawConfigParser()
config.read(file)


class readConfig():

    @staticmethod
    def getBaseURL():
        url = config.get('API', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        usernameData = config.get('Credentials', 'username')
        return usernameData

    @staticmethod
    def getPassword():
        passwordData = config.get('Credentials', 'password')
        return passwordData
    
    @staticmethod
    def getPetId():
        petIdData = config.get('Data', 'petId')
        return petIdData


    @staticmethod
    def getPetName():
        petNameData = config.get('Data', 'petName')
        return petNameData