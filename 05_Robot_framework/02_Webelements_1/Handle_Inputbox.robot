*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://parabank.parasoft.com/parabank/index.htm

*** Test Cases ***
Handle inputbox
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Input Text    name:username    Mukhesh.Test
    Input Password    name:password    1234567890
    Click Element    xpath://input[@value = 'Log In']
    Wait Until Element Is Visible    xpath://a[text() = 'Log Out']
    Close Browser

*** Keywords ***
