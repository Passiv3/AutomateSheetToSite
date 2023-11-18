from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mileage_url = "https://app.informedk12.com/link_campaigns/morgan-hill-travel-reimbursement-claim-electronic-form?token=fgtwSdEWCn8npWkHbYDbjfQH"


#first 48829198
#last 48829359


def entrypoint(list_of_rows=[]):
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get(mileage_url)


def get_user_info():
    print("Enter your name: ")
    name = input()
    print("Enter your email: ")
    email = input()
    user_info = {name: name, email: email}
    return user_info


def locate_first_cell():
    pass

entrypoint()
