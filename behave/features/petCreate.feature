Feature: Add a Pet API functionality

    @regression
    Scenario Outline: Create a Pet
        Given the user is authenticated
        When a POST requests is sent to the /pet endpoint with <name> and <id>
        Then a new pet is created

            Examples:
            |name      |id       |
            |takeshi   |9812757  |
            |morrigan  |837429   |


    @regression @smoke
    Scenario: Retrieve a Pet
        Given the user is authenticated
        And a pet has been created
        When a GET request is sent to the /pet/(petId) endpoint
        Then the pet information is retrieved

    @regression
    Scenario: Update a Pet with an Image
        Given the user is authenticated
        And a pet has been created
        When a POST request is sent to the /pet/(petId)/uploadImage endpoint
        Then the pet information is updated with image

    @regression @noCleanUp
    Scenario: Delete a Pet
        Given the user is authenticated
        And a pet has been created
        When DELETE request is sent to /pet/(petID) endpoint 
        Then the pet is deleted
