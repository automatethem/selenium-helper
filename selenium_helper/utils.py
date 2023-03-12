import socket
from pathlib import Path
import subprocess
import os

def get_chrome_web_browser_path():
    #windows 7
    path1 = "C:\Program Files\Google\Chrome\Application\\chrome.exe"
    path2 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    #windows 10
    home = str(Path.home())
    #print(home) #C:\Users\hello
    path3 = home + "\\AppData\\Local\\Google\\Chrome\Application\\chrome.exe"
    if os.path.exists(path1):
        return path1
    elif os.path.exists(path2):
        return path2
    elif os.path.exists(path3):
        return path3

def kill_all_chrome_web_browser_processes():
    #https://stackoverflow.com/questions/57792469/kill-certain-chrome-process-in-python-not-all
    subprocess.call("TASKKILL /f /IM CHROME.EXE")

def open_chrome_web_browser(user_data_dir=None, proxy_server=None):
    chrome_web_browser_path = get_chrome_web_browser_path()
    #https://not-to-be-reset.tistory.com/454
    user_data_dir_option = ""
    if user_data_dir:
        user_data_dir_option = f"--user-data-dir={user_data_dir}"
    #https://www.chromium.org/developers/design-documents/network-stack/socks-proxy/
    proxy_server_option = ""
    if proxy_server:
        proxy_server_option = f"--proxy-server={proxy_server}"
    subprocess.Popen(f'{chrome_web_browser_path} {user_data_dir_option} {proxy_server_option}  --disk-cache-dir=null --disk-cache-size=0') 

def open_chrome_web_browser_with_remote_debugging_mode(remote_debugging_port, remote_debugging_address, user_data_dir=None, proxy_server=None, headless=False):
    chrome_web_browser_path = get_chrome_web_browser_path()
    #https://not-to-be-reset.tistory.com/454
    user_data_dir_option = ""
    if user_data_dir:
        user_data_dir_option = f"--user-data-dir={user_data_dir}"
    #https://www.chromium.org/developers/design-documents/network-stack/socks-proxy/
    proxy_server_option = ""
    if proxy_server:
        proxy_server_option = f"--proxy-server={proxy_server}"
    headless_option = ""
    if headless:
        headless_option = f"--headless={headless}"
    subprocess.Popen(f'{chrome_web_browser_path} --remote-debugging-port={remote_debugging_port} --remote-debugging-address={remote_debugging_address} {user_data_dir_option} {proxy_server_option} {headless_option} --disk-cache-dir=null --disk-cache-size=0') 
    
def check_port_open(ip, port):
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_result = tcp_sock.connect_ex((ip, port))
    tcp_sock.close()
    #print(tcp_result)

    if tcp_result == 0:
        return True
    else:
        return False
