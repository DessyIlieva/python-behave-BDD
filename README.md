# python-behave-BDD
An example of BDD testing framework using Python with behave to test Swagger Petstore.

## Setup

* Setup your Virtual Environment with Python (preferably > 3.10.8)
* Clone the repository
* Install the required packages using this command:
`pip install -r requirements.txt`
* To run the test cases use: `behave` or for reports `behave -f allure_behave.formatter:AllureFormatter -o AllureReports` 
* Note: Reports are generated in .json format. In order to view you need to have allure installed (https://docs.qameta.io/allure/) and run: `allure server <path to reports folder>`
