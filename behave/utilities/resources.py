def login():
    login = '/user/login'
    return login


def addPet():
    addPet = '/pet'
    return addPet


def getPetById(petId):
    getPetbyId = f'/pet/{petId}'
    return getPetbyId


def addPetImg(petId):
    addPetImg = f'/pet/{petId}/uploadImage'
    return addPetImg


def deletePet(petId):
    deletePet = f'/pet/{petId}'
    return deletePet