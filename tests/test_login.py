import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        """
        각 테스트 케이스가 실행되기 전에 호출됩니다.
        웹 드라이버를 초기화하고, 테스트할 URL로 이동합니다.
        """
        # Chrome 드라이버 초기화
        self.driver = webdriver.Chrome()
        # 테스트할 로그인 페이지 URL로 이동
        # 실제 웹사이트 URL로 변경해야 합니다.
        self.driver.get("http://your-website-url.com/login")

    def test_successful_login(self):
        """
        올바른 사용자 이름과 비밀번호로 로그인 성공을 테스트합니다.
        """
        # 사용자 이름, 비밀번호, 로그인 버튼 요소를 찾습니다.
        # ID, Class Name, XPath 등 실제 웹페이지의 요소 식별자로 변경해야 합니다.
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        # 요소에 값을 입력하고 클릭합니다.
        username_field.send_keys("testuser")
        password_field.send_keys("password123")
        login_button.click()

        # 페이지 로딩을 위해 잠시 대기
        time.sleep(3)

        # 로그인 후 나타나는 요소(예: 환영 메시지)가 있는지 확인하여 로그인 성공을 검증합니다.
        # 실제 웹페이지의 요소 식별자로 변경해야 합니다.
        try:
            welcome_message = self.driver.find_element(By.CLASS_NAME, "welcome-message")
            # 예상하는 텍스트가 요소에 포함되어 있는지 단언(assert)합니다.
            self.assertIn("Welcome, testuser!", welcome_message.text)
        except Exception as e:
            self.fail(f"Login successful but welcome message not found: {e}")

    def test_failed_login(self):
        """
        잘못된 사용자 이름과 비밀번호로 로그인 실패를 테스트합니다.
        """
        # 사용자 이름, 비밀번호, 로그인 버튼 요소를 찾습니다.
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        # 잘못된 값을 입력하고 클릭합니다.
        username_field.send_keys("invalid_user")
        password_field.send_keys("wrong_password")
        login_button.click()

        # 페이지 로딩을 위해 잠시 대기
        time.sleep(3)

        # 로그인 실패 시 나타나는 오류 메시지를 확인하여 실패를 검증합니다.
        # 실제 웹페이지의 요소 식별자로 변경해야 합니다.
        try:
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            # 예상하는 오류 텍스트가 요소에 포함되어 있는지 단언(assert)합니다.
            self.assertIn("Invalid credentials", error_message.text)
        except Exception as e:
            self.fail(f"Login failed but error message not found: {e}")

    def tearDown(self):
        """
        각 테스트 케이스가 끝난 후 호출됩니다.
        웹 드라이버를 종료합니다.
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()