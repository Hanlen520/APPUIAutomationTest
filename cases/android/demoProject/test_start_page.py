# -*- coding:utf8 -*-
from base.android.demoProject.demoProjectClient import DemoProjectClient
from page_objects.android.demoProject.pages.startPage import StartPage
import pytest
class TestStartPage:
    def setup_class(self):
        self.demoProjectClient = DemoProjectClient()
        self.startPage=StartPage(self.demoProjectClient.appPerator)

    @pytest.fixture(autouse=True)
    def record_test_case_video(self):
        self.demoProjectClient.appPerator.start_recording_screen()
        yield self.record_test_case_video
        self.demoProjectClient.appPerator.stop_recording_screen()

    @pytest.fixture
    def fixture_test_click_start_btn(self):
        print 'start......'
        yield self.fixture_test_click_start_btn
        print 'end......'

    def test_click_start_btn(self,fixture_test_click_start_btn):
        self.startPage.click_start()

    def test_search_chinese(self):
        self.startPage.searh_city('大学')

    def test_search_en(self):
        self.startPage.searh_city('aaa')

    def test_choice_a_city(self):
        self.startPage.choice_a_city()

    def teardown_class(self):
        self.demoProjectClient.appPerator.reset_app()