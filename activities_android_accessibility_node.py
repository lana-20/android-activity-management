import time
from appium import webdriver

APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "Android",
    "appium:options": {
        "platformVersion": "13.0",
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "appPackage": "io.appium.android.apis",
        "appActivity": ".accessibility.AccessibilityNodeProviderActivity"
    }
}

driver = webdriver.Remote(APPIUM, CAPS)

try:
    time.sleep(3)   # for demo only -  to observe the activity launch
    print(f"The current app activity is: {driver.current_activity}.")
    print(f"The current app package is: {driver.current_package}.")
finally:
    if driver is not None:
        driver.quit()