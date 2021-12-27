import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from applitools.selenium import Eyes

from page_object.financial_calculator.home_page import HomePage
from page_object.financial_calculator.percentage_calc import PercentagePage
from page_object.real_world.page_notification import PageNotification
from page_object.real_world.page_side_bar import PageSideBar
from page_object.real_world.page_signin import PageSignin
from page_object.real_world.page_signup import PageSignup
from utilities.listeners import EventListener
import mysql.connector

driver = None
action = None
eyes=Eyes()

@pytest.fixture(scope='class')
def init_web(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    EventFiringWebDriver(driver, EventListener())
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
    eyes.api_key = 'CxOsxCzmfCLQj7Lj0zTmtss3agBhaZ7SROg102103rSkSow110'
    request.cls.eyes=eyes
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
    eyes.abort()

@pytest.fixture(scope='class')
def init_api(request):
    url='http://localhost:3000'
    request.cls.url = url


@pytest.fixture(scope='class')
def init_mobile(request):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    dc['reportDirectory'] = reportDirectory
    dc['reportFormat'] = reportFormat
    dc['testName'] = testName
    dc['udid'] = '32e0d8e5df3f7ece'
    dc['appPackage'] = 'com.financial.calculator'
    dc['appActivity'] = '.FinancialCalculators'
    dc['platformName'] = 'android'
    driver = webdriver.Remote('http://localhost:4729/wd/hub',dc)
    home_page = HomePage(driver)
    request.cls.home_page = home_page
    pc = PercentagePage(driver)
    request.cls.pc = pc
    yield
    driver.quit()
