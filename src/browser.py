from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pyvirtualdisplay

def create_chrome(hide=False): 
    options = webdriver.ChromeOptions()
    #options.add_argument(f'user-agent={user_agent}')
    display = None
    if hide:
        display = pyvirtualdisplay.Display(visible=0, size=(800, 600))
        display.start()
        
        # https://stackoverflow.com/questions/48450594/selenium-timed-out-receiving-message-from-renderer
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument("start-maximized") # https://stackoverflow.com/a/26283818/1689770
        options.add_argument("enable-automation") # https://stackoverflow.com/a/43840128/1689770
        # options.add_argument("--disable-infobars"); # https://stackoverflow.com/a/43840128/1689770
        # options.add_argument("--disable-dev-shm-usage"); # https://stackoverflow.com/a/50725918/1689770
        # options.add_argument("--disable-browser-side-navigation"); # https://stackoverflow.com/a/49123152/1689770
        # options.add_argument("--disable-gpu"); # https://stackoverflow.com/questions/51959986/how-to-solve-selenium-chromedriver-timed-out-receiving-message-from-renderer-exc

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options = options)
    return driver
