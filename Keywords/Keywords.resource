#RedditKeywords
*** Settings ***
Library             ../Library/TestLibrary.py
Resource            ../Variables/Variables.resource

*** Keywords ***
Create Body Request
    ${body}=                Create Body                     ${dateStart}    ${dateEnd}      ${education}        ${results}
    Set Test Variable       ${body}

Add Education
    ${education_id}=        Add New Education               ${education_api}    ${body}
    Set Suite Variable      ${education_id}
    Log To Console          ${education_id}

Get All User Educations
    ${response}             Get Response                    ${education_api}
    Set Suite Variable      ${response}

Verify That New Education Is Added
    ${check}=               Check New Education             ${response}         ${education_id}
    Should Be True          ${check}
    LOG MANY                ${response}        ${education_id}
    Log                     ${message}

Verify That Education
    ${check}=               Check The Education Value       ${response}         ${education}
    Should Be True          ${check}

Verify That Results
    ${check}=               Check The Results Value         ${response}         ${results}
    Should Be True          ${check}