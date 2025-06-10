*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://testautomationpractice.blogspot.com/

*** Test Cases ***
Working on waits
    Open Browser    ${url}    chrome
    
    ${default_selenium_speed}    Get Selenium Speed
    Log To Console    ${default_selenium_speed}  
    
    Set Selenium Speed    5    # Selenium speed will be how much time need to wait in between each step
    
    ${user_selenium_speed}    Get Selenium Speed
    Log To Console    ${user_selenium_speed}
    
    
    ${default_implicit_wait}    Get Selenium Implicit Wait
    Log To Console    ${default_implicit_wait}

    Set Selenium Implicit Wait    10    # Implicit wait applicable to all elements is element not found it will wait till the time specified and then through exception.

    ${user_implicit_wait}    Get Selenium Implicit Wait
    Log To Console    ${user_implicit_wait}
    
    
    ${default_selenium_timeout}    Get Selenium Timeout
    Log To Console    ${default_selenium_timeout}
    
    Set Selenium Timeout    10    # Default timeout for explicit timeout condition
    
    ${user_selenium_timeout}    Get Selenium Timeout
    Log To Console    ${user_selenium_timeout}
    

    Sleep    5    # It is static wait it will wait how much time we provided


*** Keywords ***
