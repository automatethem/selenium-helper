# selenium-helper

Supported APIs:
<pre>
import selenium_helper

selenium_helper.drivers.ChromeDriver()
selenium_helper.drivers.ChromeDebuggingDriver()

selenium_helper.utils.get_chrome_web_browser_path()
selenium_helper.utils.kill_all_chrome_web_browser_processes()
selenium_helper.utils.open_chrome_web_browser(user_data_dir=None, proxy_server=None)
selenium_helper.utils.open_chrome_web_browser_with_remote_debugging_mode(remote_debugging_port, remote_debugging_address, user_data_dir=None, proxy_server=None, headless=False)
selenium_helper.utils.check_port_open(ip, port)
selenium_helper.utils.save_partial_screenshot(element, image_file)
selenium_helper.utils.save_full_screenshot(driver, image_file)     
selenium_helper.utils.save_full_screenshot_with_scroll(driver, image_file)
selenium_helper.utils.save_partial_screenshot_with_scroll(driver, partial_element, image_file)
selenium_helper.utils.set_value(driver, element, value)
selenium_helper.utils.set_attribute(driver, element, attribute, value)
selenium_helper.utils.remove_element(driver, element)
selenium_helper.utils.remove_x_scrollbar(driver)
selenium_helper.utils.click(driver, element)
selenium_helper.utils.send_keys_click(driver, element)    
selenium_helper.utils.javascript_click(driver, element)
</pre>
