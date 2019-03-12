#coding=utf-8
from selenium import webdriver
import unittest

#测试组织成类的形式,继承自unittest.TestCase
class NewVisitor(unittest.TestCase):
	#初始化
	def setUp(self):
		self.browser = webdriver.Chrome()
	#
	def tearDown(self):
		self.browser.quit()

	#测试方法
	def test_can_start_a_list_and_retrieve_it_later(self):
		#框框听说有一个很酷的在线待办事项应用
		#她去看了这个应用的首页
		self.browser.get('http://localhost:8000')
		#她注意到首页的标题和头部都包含“todo”这个词
		self.assertIn('To-Do',self.browser.title)
		self.fail('Finish the test !')

#应用邀请她输入了一个代办事项
#她在一个文本框中输入了“bug peacock feathers”
#框框的爱好是使用假蝇诱饵钓鱼

#她按回车键后，页面更新了
#待办事项表格中显示了“1：bug peacock feathers”

#页面中又显示了一个文本框，可以输入其他的待办事项
#她输入了“use peacock feathers to make a fly”
#框框做事很有条理

#页面再次更新，她的清单中显示了这两个待办事项

#框框想知道这个网站是否会记住他的清单
#他看到网站为她生成了一个唯一的url
#而且页面中有一些文字解说这个功能

#她访问了那个url，发现他的待办事项列表还在

#她很满意，去睡觉了


if __name__ == '__main__':
	#禁止抛出 ResourceWarning 异常
	unittest.main(warnings='ignore')