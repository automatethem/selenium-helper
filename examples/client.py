import pynecone as pc
import selenium_supporter
import time

debugger_address = "127.0.0.1:1001"
chrome_driver = selenium_supporter.drivers.ChromeDebuggingDriver(debugger_address)
driver = chrome_driver.get_driver()

url = driver.current_url
print(url)

driver.get("https://www.jobkorea.co.kr/Corp/Person/PositionOfferList?offerIdx=9745296")