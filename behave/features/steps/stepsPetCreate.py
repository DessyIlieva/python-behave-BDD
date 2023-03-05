import requests
import json
from behave import given, when, then
from utilities.resources import *
from utilities.configurations import readConfig as conf
from features.payLoad import addPetPayload, addImagePayload


@given(u'the user is authenticated')
def step_impl(context):
    urlLogin = conf.getBaseURL() + login()
    username = conf.getUsername()
    password = conf.getPassword()

    context.s = requests.session()
    context.s.auth = (username, password)
    context.s.headers.update({'content-type':'application/json'})
    context.loginResponse = context.s.get(urlLogin, timeout=2)
    assert context.loginResponse.status_code == 200


@when(u'a POST requests is sent to the /pet endpoint with {name} and {id}')
def step_impl(context, name, id):
    urlCreate = conf.getBaseURL() + addPet()
    context.petId = id
    context.createResponse = context.s.post(urlCreate, json=addPetPayload(name, id), timeout=2)
    assert context.createResponse.status_code == 200

@then(u'a new pet is created')
def step_impl(context):
    context.execute_steps(u"""
        when a GET request is sent to the /pet/(petId) endpoint
        then the pet information is retrieved""")


@given(u'a pet has been created')
def step_impl(context):
    urlCreate = conf.getBaseURL() + addPet()
    context.petId = conf.getPetId()
    context.petName = conf.getPetName()
    context.createResponse = context.s.post(urlCreate, json=addPetPayload(context.petName, context.petId), timeout=2)
    assert context.createResponse.status_code == 200


@when(u'a GET request is sent to the /pet/(petId) endpoint')
def step_impl(context):
    urlGetPet = conf.getBaseURL() + getPetById(context.petId)
    context.getPetResponse = context.s.get(urlGetPet, timeout=2)


@then(u'the pet information is retrieved')
def step_impl(context):
    assert context.getPetResponse.text == context.createResponse.text


@when(u'a POST request is sent to the /pet/(petId)/uploadImage endpoint')
def step_impl(context):
    urlUploadImage = conf.getBaseURL() + addPetImg(context.petId)
    context.getPetImgResponse = requests.post(urlUploadImage,files=addImagePayload())


@then(u'the pet information is updated with image')
def step_impl(context):
    context.s.headers.update({'content-type':'multipart/form-data'})
    assert context.getPetImgResponse.status_code == 200


@when(u'DELETE request is sent to /pet/(petID) endpoint')
def step_impl(context):
    urlDelete = conf.getBaseURL() + deletePet(context.petId)
    context.deleteResponse = context.s.delete(urlDelete, timeout=2)
    assert context.deleteResponse.status_code == 200


@then(u'the pet is deleted')
def step_impl(context):
    context.execute_steps(u"""when a GET request is sent to the /pet/(petId) endpoint""")
    response = context.getPetResponse.json()
    assert context.getPetResponse.status_code == 404
    assert response['message'] == "Pet not found"
