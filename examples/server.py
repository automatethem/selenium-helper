import selenium_supporter
  
debugger_address = "127.0.0.1:1001"
remote_debugging_address = debugger_address.split(':')[0]
remote_debugging_port = int(debugger_address.split(':')[1])
#print(remote_debugging_address) #127.0.0.1
#print(remote_debugging_port) #1001
selenium_supporter.utils.open_chrome_web_browser_with_remote_debugging_mode(remote_debugging_port, remote_debugging_address, user_data_dir=None, proxy_server=None, headless=False)
