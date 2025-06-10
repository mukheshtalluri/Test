*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handle simple alerts
    Open Browser    ${url}    chrome
    Set Selenium Speed    1
    Maximize Browser Window
    Click Element    alertBtn
    Handle Alert    accept
    Close Browser

Handle conformation alert
    Open Browser    ${url}    chrome
    Set Selenium Speed    1
    Maximize Browser Window
    Click Element    confirmBtn
    Handle Alert    accept
    Wait Until Element Is Visible    xpath://p[text() = 'You pressed OK!']
    Click Element    confirmBtn
    Handle Alert    dismiss
    Wait Until Element Is Visible    xpath://p[text() = 'You pressed Cancel!']
    Close Browser

Handle prompt alert
    Open Browser    ${url}    chrome
    Set Selenium Speed    1
    Maximize Browser Window
    Click Element    promptBtn
    Input Text Into Alert    Mukhesh    accept
    Sleep    5
    Wait Until Element Is Visible    xpath://p[contains(text(), 'Mukhesh')]
    Close Browser
    
    
Handle single frame
    Open Browser    https://demo.automationtesting.in/Frames.html    chrome
    Maximize Browser Window
    Set Selenium Speed    2
    Select Frame    singleframe
    Input Text    xpath://input[@type = 'text']    Mukhesh
    Sleep    5
    Unselect Frame
    Close Browser

Handle multiple frames
    Open Browser    https://demo.automationtesting.in/Frames.html    chrome
    Maximize Browser Window
    Set Selenium Speed    2
    Click Element    xpath://a[text() = 'Iframe with in an Iframe']
    Select Frame    xpath://iframe[@src = 'MultipleFrames.html']
    Select Frame     xpath://iframe[@src = 'SingleFrame.html']
    Input Text    xpath://input[@type = 'text']    Mukhesh
    Sleep    10
    Unselect Frame
    Unselect Frame
    Wait Until Element Is Visible    xpath://a[text() = 'Home']
    Close Browser

*** Keywords ***
