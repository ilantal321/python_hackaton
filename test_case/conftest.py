import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from applitools.selenium import Eyes

import utilities.commonOps
from page_object.api_demo_electron.api_demo import APIDemoElectron
from page_object.calculator.calculator_page import CalculatorPage
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
eyes = Eyes()


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
    request.cls.eyes = eyes
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
    url = 'http://localhost:3000'
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
    driver = webdriver.Remote('http://localhost:4729/wd/hub', dc)
    home_page = HomePage(driver)
    request.cls.home_page = home_page
    pc = PercentagePage(driver)
    request.cls.pc = pc
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    driver.implicitly_wait(5)
    cp = CalculatorPage(driver)
    request.cls.cp = cp
    yield
    driver.quit()

@pytest.fixture(scope='class')
def init_electron(request):
    electron_app = utilities.commonOps.get_data('electron_app')
    edriver = utilities.commonOps.get_data('electron_driver')
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    driver.implicitly_wait(5)
    request.cls.driver=driver
    epo=APIDemoElectron(driver)
    request.cls.epo=epo
    yield
    driver.close()
