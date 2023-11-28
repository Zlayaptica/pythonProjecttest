import pytest

@pytest.fixture()
def log_xpath():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def pass_xpath():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def btn_xpath():
    return """//*[@id="login"]/div[3]/button"""

@pytest.fixture()
def result_xpath():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""