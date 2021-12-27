import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from page_object.page_notification import PageNotification
from page_object.real_world.page_side_bar import PageSideBar
from page_object.real_world.page_signin import PageSignin
from page_object.real_world.page_signup import PageSignup
from utilities.listeners import EventListener
import mysql.connector

driver = None
action = None


@pytest.fixture(scope='class')
def init_web(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = EventFiringWebDriver(driver, EventListener())
    driver.maximize_window()
    driver.get("http://localhost:4000/")
    login = PageSignin(driver)
    side_bar = PageSideBar(driver)
    request.cls.driver = driver
    request.cls.login = login
    request.cls.side_bar = side_bar
    signup = PageSignup(driver)
    request.cls.signup = signup
    notifiaction = PageNotification(driver)
    request.cls.notifiaction = notifiaction

    mydb = mysql.connector.connect(
        host="remotemysql.com",
        database='HgcKGz4q8T',
        user="HgcKGz4q8T",
        password="x0MLwiZ7im"
    )
    request.cls.mydb = mydb

    yield
    mydb.close()
    driver.quit()
