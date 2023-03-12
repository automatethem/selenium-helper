'''
pip install webdriver-manager
'''
import platform
from PIL import Image
from io import StringIO
from PIL import Image
from io import BytesIO
from io import BytesIO
from pathlib import Path
import sys
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
try:
    import pyautogui
except:
    pass
import time
import sys
sys.path.append('../')
import cranberry.logging_lib
import logging
import getpass
import traceback

class ChromeDriver():
    #def __init__(self, user_data_dir="C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\".format(getpass.getuser()), profile_directory="Default"):
    #def __init__(self, user_data_dir, profile_directory):
    def __init__(self, user_data_dir=None):
    #def __init__(self):
        super().__init__()

        #executable_path = "chromedriver_98.0.4758.102/chromedriver.exe"
        executable_path = ChromeDriverManager().install()
        service = Service(executable_path=executable_path)
        if platform.system() == 'Windows': #윈도우
            from subprocess import CREATE_NO_WINDOW #윈도우에만
            service.creationflags = CREATE_NO_WINDOW #콘솔창 숨기기 https://stackoverflow.com/questions/66953190/selenium-hide-chromdriver-console-window

        options = webdriver.ChromeOptions() 
        #https://forum.katalon.com/t/open-browser-with-custom-profile/19268
        #'''
        #options.add_argument(f"user-data-dir={user_data_dir}")
        #options.add_argument(f"profile-directory=\"{profile_directory}\"")
        #print(f"profile-directory=\"{profile_directory}\"")
        #'''
        #user_data_dir="C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default".format(getpass.getuser())
        #options.add_argument(f"user-data-dir={user_data_dir}")



        '''
        #options.add_argument("user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\".format(getpass.getuser()))
        options.add_argument("user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data".format(getpass.getuser()))
        #options.add_argument("user-data-dir=\"C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 17\"".format(getpass.getuser())) #
        #options.add_argument("user-data-dir=\"C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\"".format(getpass.getuser())) #
        options.add_argument("profile-directory=\"Default\"")
        '''

        #!!
        #options.add_argument("user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\".format(getpass.getuser()))

        if user_data_dir:
            options.add_argument(f"--user-data-dir=\"{user_data_dir}\"")

        #x
        #options.add_argument("user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default".format(getpass.getuser()))
        
        #x
        #options.add_argument("profile-directory=\"Default\"")

        #options.add_argument("--user-data-dir=\"D:\\크랜베리_제작\\작업 봇\\input\\chrome\"") #
        #options.add_argument("--profile-directory=\"Profile test\"")


        #options.add_argument("user-data-dir=\"D:\\크랜베리_제작\\작업 봇\\input\\chrome\\Profile test\"") #
        #options.add_argument("--disable-extensions") #



        #options.add_argument(f"user-data-dir={user_data_dir}\\{profile_directory}")
        


        #https://stackoverflow.com/questions/70534875/typeerror-init-got-an-unexpected-keyword-argument-service-error-using-p
        #https://www.pythonanywhere.com/forums/topic/29068/
        try: 
            self.driver = webdriver.Chrome(service=service, options=options) 
        except:
            logging.debug(traceback.format_exc())
            try: 
                self.driver = webdriver.Chrome(options=options)
            except:
                logging.debug(traceback.format_exc())
                self.driver = webdriver.Chrome(executable_path=executable_path, options=options)

    def get_driver(self):
        return self.driver

    def get(self, url):
        self.driver.get(url)

    def get_with_proxy_username_and_password(self, url, proxy_username, proxy_password):
        self.driver.get(url)
        if proxy_username and proxy_password:
            time.sleep(1)
            pyautogui.typewrite(proxy_username)
            pyautogui.press('tab')
            pyautogui.typewrite(proxy_password)
            pyautogui.press('enter')

class ChromeDebuggingDriver():
    def __init__(self, chrome_debugger_address=None):
        super().__init__()

        #executable_path = "chromedriver_98.0.4758.102/chromedriver.exe"
        executable_path = ChromeDriverManager().install()
        service = Service(executable_path=executable_path)
        if platform.system() == 'Windows': #윈도우
            from subprocess import CREATE_NO_WINDOW #윈도우에만
            service.creationflags = CREATE_NO_WINDOW #콘솔창 숨기기 https://stackoverflow.com/questions/66953190/selenium-hide-chromdriver-console-window

        options = webdriver.ChromeOptions() 
        if not chrome_debugger_address:
            chrome_debugger_address = "127.0.0.1:9222"
        options.add_experimental_option("debuggerAddress", chrome_debugger_address)

        #https://stackoverflow.com/questions/70534875/typeerror-init-got-an-unexpected-keyword-argument-service-error-using-p
        #https://www.pythonanywhere.com/forums/topic/29068/
        try: 
            self.driver = webdriver.Chrome(service=service, options=options) 
        except:
            try: 
                self.driver = webdriver.Chrome(options=options)
            except:
                self.driver = webdriver.Chrome(executable_path=executable_path, options=options)

    '''
    def __init__(self, proxy_server=None, proxy_username=None, proxy_password=None):
        super().__init__()
   
        self.proxy_server = proxy_server
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password

        #executable_path = "chromedriver_98.0.4758.102/chromedriver.exe"
        executable_path = ChromeDriverManager().install()
        service = Service(executable_path=executable_path)
        if platform.system() == 'Windows': #윈도우
            from subprocess import CREATE_NO_WINDOW #윈도우에만
            service.creationflags = CREATE_NO_WINDOW #콘솔창 숨기기 https://stackoverflow.com/questions/66953190/selenium-hide-chromdriver-console-window

        options = webdriver.ChromeOptions() 
        #https://botproxy.net/docs/how-to/setting-chromedriver-proxy-auth-with-selenium-using-python/
        if proxy_server:
            manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
            """

            background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
            """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

            options.add_argument(f"--proxy-server={self.proxy_server}")

        if self.proxy_username and self.proxy_password:
            pluginfile = 'proxy_auth_plugin.zip'
            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)
            options.add_extension(pluginfile)
        
        #https://stackoverflow.com/questions/70534875/typeerror-init-got-an-unexpected-keyword-argument-service-error-using-p
        #https://www.pythonanywhere.com/forums/topic/29068/
        try: 
            self.driver = webdriver.Chrome(service=service, options=options) 
        except:
            try: 
                self.driver = webdriver.Chrome(options=options)
            except:
                self.driver = webdriver.Chrome(executable_path=executable_path, options=options)
    '''

    def get_driver(self):
        return self.driver

    def get(self, url):
        self.driver.get(url)

    def get_with_proxy_username_and_password(self, url, proxy_username, proxy_password):
        self.driver.get(url)
        if proxy_username and proxy_password:
            time.sleep(1)
            pyautogui.typewrite(proxy_username)
            pyautogui.press('tab')
            pyautogui.typewrite(proxy_password)
            pyautogui.press('enter')

def save_partial_screenshot(element, image_file):
    #'''
    png = element.screenshot_as_png
    with open(image_file, "wb") as f:
        f.write(png)
    #'''
    '''
    #https://www.tutorialspoint.com/how-to-take-partial-screenshot-with-selenium-webdriver-in-python
    captcha_image_element.screenshot(image_file)
    '''

def save_full_screenshot(driver, image_file):     
    driver.save_screenshot(image_file)

def save_full_screenshot_with_scroll(driver, image_file): 
    # initiate value

    #image_file = image_file.with_suffix(".png") if not image_file.match("*.png") else image_file
    img_li = []  # to store image fragment
    offset = 0  # where to start

    # js to get height
    height = driver.execute_script("return Math.max(" "document.documentElement.clientHeight, window.innerHeight);")

    # js to get the maximum scroll height
    # Ref--> https://stackoverflow.com/questions/17688595/finding-the-maximum-scroll-position-of-a-page
    max_window_height = driver.execute_script(
        "return Math.max("
        "document.body.scrollHeight, "
        "document.body.offsetHeight, "
        "document.documentElement.clientHeight, "
        "document.documentElement.scrollHeight, "
        "document.documentElement.offsetHeight);"
    )

    # looping from top to bottom, append to img list
    # Ref--> https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
    while offset < max_window_height:
        # Scroll to height
        driver.execute_script(f"window.scrollTo(0, {offset});")

        # === uncomment the line and edit id to hide persistent elements when scrolling ===
        # driver.execute_script("document.getElementById('navbar').innerHTML = '';")

        img = Image.open(BytesIO((driver.get_screenshot_as_png())))
        img_li.append(img)
        offset += height

    # In case it is not a perfect fit, the last image contains extra at the top.
    # Crop the screenshot at the top of last image.
    extra_height = offset - max_window_height
    if extra_height > 0 and len(img_li) > 1:
        pixel_ratio = driver.execute_script("return window.devicePixelRatio;")
        extra_height *= pixel_ratio
        last_image = img_li[-1]
        width, height = last_image.size
        box = (0, extra_height, width, height)
        img_li[-1] = last_image.crop(box)

    # Stitch image into one
    # Set up the full screen frame
    img_frame_height = sum([img_frag.size[1] for img_frag in img_li])
    img_frame = Image.new("RGB", (img_li[0].size[0], img_frame_height))
    offset = 0
    for img_frag in img_li:
        img_frame.paste(img_frag, (0, offset))
        offset += img_frag.size[1]
    img_frame.save(image_file)

def save_partial_screenshot_with_scroll(driver, partial_element, image_file):
    save_full_screenshot_with_scroll(driver, image_file)

    #https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python
    location = partial_element.location
    size = partial_element.size
    from PIL import Image
    from io import StringIO
    image = Image.open(image_file)
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    image = image.crop((int(left), int(top), int(right), int(bottom)))
    image.save(image_file)
    
def set_value(driver, element, value):
    #element.send_keys(value)
    driver.execute_script(f"""
    arguments[0].value='{value}';
    """, element)

def set_attribute(driver, element, attribute, value):
    driver.execute_script(f"""
    arguments[0].setAttribute('{attribute}', '{value}')
    """, element)

def remove_element(driver, element):
    #https://stackoverflow.com/questions/22515012/python-selenium-how-can-i-delete-an-element
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)

def remove_x_scrollbar(driver):
    #https://stackoverflow.com/questions/22515012/python-selenium-how-can-i-delete-an-element
    driver.execute_script("""
    document.getElementsByTagName("body")[0].style.overflowX = "hidden";
    """)

'''
def click(driver, element):
    #element.click()
    #from selenium.webdriver.common.keys import Keys
    #button_element.send_keys(Keys.ENTER)
    driver.execute_script("arguments[0].click();", element)
'''

def click(driver, element):
    element.click()
    
def send_keys_click(driver, element):    
    element.send_keys(Keys.ENTER)

def javascript_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

if __name__ == "__main__":
    level = logging.DEBUG
    #level = logging.INFO
    #level = logging.ERROR
    cranberry.logging_lib.basic_config(level)

    #chrome_debugger_address = "127.0.0.1:9222"
    #proxy_server = "45.159.155.25:61302"
    #chrome_driver = ChromeDriver(chrome_debugger_address, "C:\\Users\\hello\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
    #chrome_driver = ChromeDriver(chrome_debugger_address, "C:\\Users\\hello\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
    ##chrome_driver = ChromeDriver(chrome_debugger_address, "C:\\Users\\hello\\AppData\\Local\\Google\\Chrome\\User Data")
    #
    #chrome_driver = ChromeDriver(chrome_debugger_address)
    chrome_driver = ChromeDriver()

    '''
    url = "http://www.naver.com"
    proxy_username = "run"
    proxy_password = "FS1484rs"
    chrome_driver.get_with_proxy_username_and_password(url, proxy_username, proxy_password)
    '''
    #'''
    chrome_driver.get("https://www.naver.com")
    save_full_screenshot_with_scroll(chrome_driver.get_driver(), 'test.png')
    #'''


