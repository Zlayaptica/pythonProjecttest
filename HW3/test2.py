import time

from testpage import OperationHelper

username = "Petrr"
password = "fa258a35d9"


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("Petrr")
    test_page1.enter_pswd("fa258a35d9")
    test_page1.click_button()
    time.sleep(3)

    test_page1.click_contact()
    time.sleep(3)

    test_page1.enter_cont_name("Petrr")
    test_page1.enter_cont_email("mail@mail.ru")
    test_page1.enter_cont_text("Hello!")
    time.sleep(1)

    test_page1.click_button()
    time.sleep(1)

    assert test_page1.get_alert_text() == "Form successfully submitted"
