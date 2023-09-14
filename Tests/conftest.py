import glob
import os
import shutil
import time

import pytest
from selenium.webdriver.chrome import webdriver
from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pytest_html_reporter import attach
from utilities.BaseClass import BaseClass

driver = None

@pytest.fixture(scope="class")
def setup(request):
        global driver
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        options.add_experimental_option("detach", True)
        chromePath = Service("C:/Users/DanielHasid/chromedriver.exe")
        driver = webdriver.Chrome(service=chromePath, options=options)
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("https://demo2.okoora.com")

        request.cls.driver = driver
        yield
        driver.close()







@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

@pytest.fixture
def movePicture():
    source_folder = r"C:\Users\DanielHasid\PycharmProjects\Okoora\Tests"
    destination_folder = r"C:\Users\DanielHasid\PycharmProjects\Okoora\Tests\pytest_screenshots\\"
    pattern = "\*.png"
    files = glob.glob(source_folder + pattern)
    # move the files with txt extension
    for file in files:
        # extract file name form file path
        file_name = os.path.basename(file)
        shutil.move(file, destination_folder + file_name)
        print('Moved:', file)







