# -*- coding: utf-8 -*-
import scrapy
import re
import json


# 相关文档： https://doc.scrapy.org/en/1.3/topics/spiders.html?highlight=parse
class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']

    # 头文件
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0"
    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhihu.com",
        "User-Agent": agent
    }

    def parse(self, response):
        pass

    # 登录账号
    def start_requests(self):
        # 获取首页
        return [scrapy.Request('https://www.zhihu.com/#signin', headers=self.headers, callback=self.login)]

    # 登录账号
    def login(self, response):
        response_text = response.text
        match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text, re.DOTALL)
        xsrf = ''
        if match_obj:
            xsrf = match_obj.group(1)
        if xsrf:
            post_url = "https://www.zhihu.com/login/phone_num"
            post_data = {
                "_xsrf": xsrf,
                "phone_num": "17727641650",
                "password": "a123456789",
                "captcha": ""
            }

            import time
            t = str(int(time.time() * 1000))
            captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
            # yield的目的为了cookie一样
            yield scrapy.Request(captcha_url, headers=self.headers, meta={"post_data":post_data}, callback=self.login_after_captcha)


    # 验证码登录
    def login_after_captcha(self, response):
        with open("captcha.jpg", "wb") as f:
            f.write(response.body)
            f.close()

        from PIL import Image
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            pass
        # python2为raw_input()
        captcha = input("输入验证码\n")
        # 取出post_data
        # response官方文档：https://doc.scrapy.org/en/latest/topics/request-response.html?highlight=response
        post_data = response.meta.get("post_data", {})
        post_data["captcha"] = captcha
        return [scrapy.FormRequest(
            url="https://www.zhihu.com/login/phone_num",
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login
        )]

    def check_login(self, response):
            # 验证服务器的返回数据判断是否成功
            text_json = json.loads(response.text)
            if "msg" in text_json and text_json["msg"] == "登录成功":
                for url in self.start_urls:
                    yield scrapy.Request(url, dont_filter=True, headers=self.headers)



