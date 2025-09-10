import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class WikipediaTest(unittest.TestCase):

    def setUp(self):
        # 웹 드라이버를 초기화하고 위키백과 홈페이지로 이동
        self.driver = webdriver.Chrome()
        self.driver.get("https://ko.wikipedia.org/wiki/위키백과:대문")
        time.sleep(2)  # 페이지 로딩 대기

    def test_navigate_and_verify(self):
        # 1. '오늘의 글' 링크를 클릭하여 페이지 이동
        # XPath를 사용하여 '오늘의 글' 링크를 찾습니다.
        # 이 경로는 위키백과 페이지 구조에 따라 변경될 수 있습니다.
        try:
            today_article_link = self.driver.find_element(By.XPATH, '//*[@id="main-page-toc"]/ul/li[1]/a')
            today_article_link.click()
            time.sleep(3)  # 페이지 이동 대기

            # 2. 이동한 페이지의 제목(title)이 올바른지 확인
            self.assertIn("위키백과", self.driver.title)

            # 3. 페이지의 첫 번째 문단 텍스트를 검증
            # p 태그의 첫 번째 문단을 찾습니다.
            first_paragraph = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]')
            print(f"첫 번째 문단 내용: {first_paragraph.text[:50]}...")
            self.assertTrue(len(first_paragraph.text) > 50, "문단의 길이가 50자 이상이어야 합니다.")

        except Exception as e:
            self.fail(f"테스트 중 오류 발생: {e}")

    def tearDown(self):
        # 테스트 종료 후 웹 드라이버 종료
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()