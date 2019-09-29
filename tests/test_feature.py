import unittest
from configs import config
from page import page
from tests import helpers as helper


class TestFeature(unittest.TestCase):
	cf = config.Config()
	cf.base_url = 'erikwhiting.com'
	cf.subdomain = ''
	cf.base_url += '/newsOutlet'

	def test_write_and_click_with_headless(self):
		self.cf.options_list = ["headless"]
		bp = page.Page(self.cf)
		bp.go()
		bp.element_by("id", "sourceNews").input_text("Hello")
		bp.element_by("id", "transmitter").click()
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)
		bp.close()

	def test_write_and_click_without_headless(self):
		self.cf.options_list = []
		bp = page.Page(self.cf)
		bp.go()
		bp.element_by("id", "sourceNews").input_text("Hello")
		bp.element_by("id", "transmitter").click()
		english_div = helper.evaluate_element_text(bp.element_by("id", "en1"), "Hello")
		self.assertTrue(english_div)
		bp.close()

	def test_page_source_feature(self):
		self.cf.options_list = ["headless"]
		bp = page.Page(self.cf)
		bp.go()
		source = bp.page_source()
		self.assertIn('<body onload="defaultBreaking()">', source)

	def test_page_url(self):
		self.cf.options_list = ["headless"]
		bp = page.Page(self.cf)
		bp.go()
		current_url = bp.get_url()
		if current_url[current_url.__len__()-1] == "/":
			current_url = current_url[:-1]
		self.assertEqual(self.cf.url(), current_url)
