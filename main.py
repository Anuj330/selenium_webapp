# from flask import Flask
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
# app = Flask(__name__)
# driver = webdriver.Chrome()
#
#
# @app.route('/signIn')
# def signIn():
#     driver.get("https://pep.vfirst.com/login")
#     username_input = driver.find_element(By.NAME, "email")
#     username_input.send_keys("anuj.mahto@vfirst.com")
#     user_pass = driver.find_element(By.NAME, "password")
#     user_pass.send_keys('1943@123')
#     login_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
#     )
#     login_button.click()
#     # signin_button = WebDriverWait(driver, 10).until(
#     #     EC.element_to_be_clickable((By.ID, "signin"))
#     # )
#     signin_button = driver.find_element(By.ID, "signin")
#
#     try:
#         signin_button.click()
#     except:
#         print("Sign In button not found, clicking Sign In.")
#
#     driver.quit()
#     return "Job executed successfully sign in."
#
#
# @app.route('/signOut')
# def signOut():
#     driver.get("https://pep.vfirst.com/login")
#     username_input = driver.find_element(By.NAME, "email")
#     username_input.send_keys("anuj.mahto@vfirst.com")
#     user_pass = driver.find_element(By.NAME, "password")
#     user_pass.send_keys('1943@123')
#     login_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
#     )
#     login_button.click()
#     # signout_button = WebDriverWait(driver, 10).until(
#     #     EC.element_to_be_clickable((By.ID, "signout"))
#     # )
#     signout_button = driver.find_element(By.ID, "signout")
#     try:
#         signout_button.click()
#     except:
#         print("Sign Out button not found, clicking Sign In.")
#
#     driver.quit()
#     return "Job executed successfully sign out."


import logging
from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)


def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--proxy-server=http://127.0.0.1:5000")

    return webdriver.Chrome(options=chrome_options)


@app.route('/')
def home():
    driver = get_driver()
    driver.get('http://www.google.com')
    print(driver.title)
    return "Home page"


@app.route('/signIn')
def signIn():
    try:
        driver = get_driver()
        driver.get("https://pep.vfirst.com/login")

        # Fill in username and password
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        username_input.send_keys("anuj.mahto@vfirst.com")

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys('1943@123')

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
        )
        login_button.click()
        signin_button = driver.find_element(By.ID, "signin")
        try:
            signin_button.click()
            driver.quit()
        except:
            print("Sign In button not found, clicking Sign In.")

    except Exception as e:
        error_message = {"error": str(e)}
        logging.error(error_message)  # Log the error
        return jsonify(error_message), 500

    return "sign in complete"


@app.route('/signOut')
def signOut():
    try:
        driver = get_driver()
        driver.get("https://pep.vfirst.com/login")

        # Fill in username and password
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        username_input.send_keys("anuj.mahto@vfirst.com")

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys('1943@123')
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
        )
        login_button.click()

        signout_button = driver.find_element(By.ID, "signout")
        try:
            signout_button.click()
            driver.quit()
        except:
            print("Sign Out button not found, clicking Sign In.")

    except Exception as e:
        error_message = {"error": str(e)}
        logging.error(error_message)  # Log the error
        return jsonify(error_message), 500
    return "sign out complete"


if __name__ == '__main__':
    app.run()