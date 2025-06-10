*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.techlistic.com/p/selenium-practice-form.html

*** Test Cases ***
Handle checkbox and radio button
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10
    Select Radio Button    sex    Male
    Select Radio Button    exp    6
    Select Checkbox    xpath://input[@value = 'Automation Tester']
    Close Browser
*** Keywords ***
