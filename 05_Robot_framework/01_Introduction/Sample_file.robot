*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${browser}    chrome
${url}    https://demowebshop.tricentis.com/
${user_name}    mukhesh.test@gmail.com
${password}    1234567890


*** Test Cases ***
Login to the application
    Open Browser    ${url}    ${browser}
    Click Link    Log in
    Input Text    Email    ${user_name}
    Input Password    Password    ${password}
    Click Button    //input[@value = 'Log in']
    Wait Until Element Is Visible    //a[text() = 'mukhesh.test@gmail.com']
    Close Browser

*** Keywords ***
