import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SearchTest(unittest.TestCase):

    def setUp(self):
        # 테스트 시작 전에 웹 드라이버를 초기화하고, 구글 홈페이지로 이동합니다.
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")

    def test_successful_search(self):
        # 성공적인 검색을 테스트하는 함수
        
        # 검색창 요소를 찾습니다.
        # 구글의 검색창은 'name' 속성이 'q'인 경우가 많습니다.
        search_box = self.driver.find_element(By.NAME, "q")
        
        # 검색어 "QA automation"을 입력하고 엔터키를 누릅니다.
        search_box.send_keys("QA automation")
        search_box.send_keys(Keys.ENTER)

        time.sleep(3)  # 검색 결과 페이지 로딩을 위해 잠시 대기
        
        # 검색 결과 페이지의 제목에 검색어가 포함되어 있는지 확인합니다.
        # 이는 페이지가 올바르게 로드되었음을 나타내는 좋은 지표입니다.
        self.assertIn("QA automation", self.driver.title)
        
        # 또는 검색 결과 중 특정 링크나 텍스트가 있는지 확인할 수도 있습니다.
        # try-except 블록을 사용해 요소가 존재하는지 확인하는 방법
        try:
            results_stats = self.driver.find_element(By.ID, "result-stats")
            print(f"검색 결과 통계: {results_stats.text}")
            self.assertTrue(results_stats.is_displayed())
        except Exception as e:
            self.fail(f"검색 결과가 표시되지 않았습니다: {e}")

    def tearDown(self):
        # 테스트 종료 후 웹 드라이버를 종료합니다.
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()