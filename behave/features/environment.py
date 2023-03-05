import requests
from utilities.resources import deletePet
from utilities.configurations import readConfig as conf

def after_scenario(context, scenario):
    if 'noCleanUp' not in scenario.tags:
        urlDelete = conf.getBaseURL() + deletePet(context.petId)
        requests.delete(urlDelete)