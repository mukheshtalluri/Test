*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handle static dropdown
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Select From List By Value    country    india
    Close Browser

Handle listbox
    Open Browser    ${url}    chrome
    Select From List By Label    colors    Yellow
    Close Browser

Handle sorted listbox
    Open Browser    ${url}    chrome
    Select From List By Index    animals    7
    Close Browser


*** Keywords ***
