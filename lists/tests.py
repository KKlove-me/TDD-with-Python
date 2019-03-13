from django.test import TestCase
#resolve是Django内部用户解析url，并将其映射到相应的视图函数上
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        #检查解析网站根路径“/”时，是否能够找到名为home_page的函数
        self.assertEqual(found.func, home_page)

        def test_home_page_returns_correct_html(self):
            #创建了一个HttpRequest对象，用户在浏览器中请求网页，Django看到的就是HttpRequest对象
            request = HttpRequest()
            #把HttpRequest对象传给home_page视图，得到响应
            response = home_page(request)
            #提取响应的.content二进制，调用.decode把原始字节转换成发送给用户的html字符串
            html = response.content.decode('utf-8')
            #校验响应是以<html>标签开头
            self.assertTrue(html.startswith('<html>'))
            #校验响应中有一个<title>标签，其内容包含单词"To-Do lists"
            self.assertIn('<title>To-Do lists</title>', html)
            #校验响应是以<html>标签开头
            self.assertTrue(html.endswith('</html>'))
