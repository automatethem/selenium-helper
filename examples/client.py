import selenium_supporter

debugger_address = "127.0.0.1:1001"
chrome_driver = selenium_supporter.drivers.ChromeDebuggingDriver(debugger_address)
driver = chrome_driver.get_driver()

driver.get("http://www.automatethem.com")
