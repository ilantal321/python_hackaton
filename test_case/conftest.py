import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page_object.real_world.page_side_bar import PageSideBar
from page_object.real_world.page_signin import PageSignin
from page_object.real_world.page_signup import PageSignup

driver = None
action = None


@pytest.fixture(scope='class')
def init_web(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://localhost:4000/")
    login = PageSignin(driver)
    side_bar = PageSideBar(driver)
    request.cls.driver = driver
    request.cls.login = login
    request.cls.side_bar = side_bar
    signup = PageSignup(driver)
    request.cls.signup = signup

    yield
    driver.quit()



