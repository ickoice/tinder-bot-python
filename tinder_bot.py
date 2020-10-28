from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        # Turn off popup cookies
        cookies_popup_btn = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')))
        cookies_popup_btn.click()

        # Click login button
        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_btn.click()

        sleep(2)

        # print(self.driver.window_handles)

        # click login with facebook
        # fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        # print(fb_btn)
        # fb_btn.click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "//button[@type = 'button' and @aria-label = 'Log in with Facebook']//span"))).click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(2)

        self.driver.switch_to_window(base_window)

        popup_1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
        popup_1.click()

        popup_2 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
        popup_2.click()

        # sleep(10)
        recieved_likes_popup = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="modal-manager"]/div/div/div/div[3]/button[2]')))
        if recieved_likes_popup:
            recieved_likes_popup.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        from random import random
        left_count, right_count = 0, 0
        while True:
            sleep(0.5)
            try:
                rand = random()
                if rand < .73:
                    self.like()
                    right_count = right_count + 1
                    print('{}th right swipe'.format(right_count))
                else:
                    self.dislike()
                    left_count = left_count + 1
                    print('{}th left swipe'.format(left_count))
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def message_all(self):
    	MESSAGE = 'heyy'
        while True:
            matches = self.driver.find_elements_by_class_name('matchListItem')
            print(matches)
            if len(matches) < 2:
                break
            matches[1].click()
            sleep(4)
            msg_box = self.driver.find_element_by_xpath(
                '//*[@id="chat-text-area"]')
            msg_box.send_keys(MESSAGE)

            sleep(2)
            send_btn = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button[2]')))
            send_btn.click()
            sleep(2)
            matches_tab = self.driver.find_element_by_xpath(
                '//*[@id="match-tab"]')
            matches_tab.click()
            sleep(1)


bot = TinderBot()
bot.login()
sleep(5)
# bot.auto_swipe()
# bot.message_all()
