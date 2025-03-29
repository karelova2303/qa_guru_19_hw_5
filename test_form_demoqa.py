import os
from selene import browser, have, be, command


def test_form_demoqa(browser_options):
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Veronika')
    browser.element('#lastName').should(be.blank).type('Fila')
    browser.element('#userEmail').should(be.blank).type('Veronika_Fila@mail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('9999872282')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="1"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1996"]').click()
    browser.all('.react-datepicker__day').element_by(have.exact_text('21')).click()
    browser.element('#subjectsInput').perform(
        command.js.scroll_into_view).should(be.blank).type('Chemistry').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('girafe.jpg'))
    browser.element('#currentAddress').should(be.blank).type('41 Eastern Avenue APT 243 San Francisco, 77338')
    browser.element('#state').click().element('#react-select-3-option-3').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(
        have.exact_text('Thanks for submitting the form'))

    browser.element('.table').all('tr').should(
        have.exact_texts('Label Values',
                         'Student Name Veronika Fila',
                         'Student Email Veronika_Fila@mail.com',
                         'Gender Female',
                         'Mobile 9999872282',
                         'Date of Birth 21 February,1996',
                         'Subjects Chemistry',
                         'Hobbies Sports',
                         'Picture girafe.jpg',
                         'Address 41 Eastern Avenue APT 243 San Francisco, 77338',
                         'State and City Rajasthan Jaiselmer',
        )
    )
