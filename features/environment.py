from selenium import webdriver


def before_all(context):
    context.web = webdriver.Chrome('C:\\Temp\\ChromeDriver\\chromedriver.exe')


def after_step(context, step):
    print()


def after_all(context):
    context.web.quit()
