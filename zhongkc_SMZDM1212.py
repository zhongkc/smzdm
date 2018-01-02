# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:37:37 2017
数据 url：https://faxian.smzdm.com/h1s183t0f0c1p1/#filter-block


@author: J17020017
"""
import ssl
import urllib.request
import re
from selenium import webdriver
import time
#import os
#from selenium.webdriver.common.by import By
from lxml import etree
# import tkinter.messagebox

# # 打开网页读取html
def get_info():  #读取网页为res文本
    url = "https://faxian.smzdm.com/h1s183t0f0c1p1/#filter-block"
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:55.0) Gecko/20100101 Firefox/57.0'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(url=url,headers = headers)
    try:    
        with urllib.request.urlopen (req) as f:
            html = f.read()
            selector = etree.HTML(html)
            name = selector.xpath('//*[@id="feed-main-list"]/li[1]/div/h5/a/text()')[0]   # 商品名
            jg = selector.xpath('//*[@id="feed-main-list"]/li[1]/div/div[2]/text()')[0]   # 价格
            sm = selector.xpath('//*[@id="feed-main-list"]/li[1]/div/div[4]/text()')[0]   # 介绍说明
            js = (sm + name + jg).replace(' ','')
            zdm_url =selector.xpath('//*[@id="feed-main-list"]/li[1]/div/div[5]/div[2]/div/div/a/@href')[0]  #链接
            info = selector.xpath('//*[@id="feed-main-list"]/li[1]/div/div[5]/div[2]/div/div/a/@onclick')[0]  # 信息
            req1 = re.compile('\'price\':\'(.*?)\'')    #价格的正则表达式
            res1 = req1.search(info).group(1)
            #print (res1)
            req = re.compile('category\':\'(.*?/.*?)/', re.S)  #分类的正则表达式
            # res = req.findall(req,info)
            res = req.search(info).group(1)
            code = d.get(res,1503)
        return zdm_url,js,jg,code,res1
    except :
        print ('读取页面错误')


def get_jd_code(url):   #由京东的推广链接地址拿到京东的商品号
    driver.switch_to_window(handles[1])
    try:
        driver.get(url) #得到当前打开加载后页面的链接url
        url_t = driver.current_url
        jd_code = re.findall('(\d+)\.html',url_t)
        print (jd_code)
    except:
        jd_code = 0
    finally:
        return jd_code
    
def open_web():
    driver.switch_to_window(handles[0])
#    driver = handles[0]
    username ="zhongkc"
    passwd = "3541756"
    driver.get("http://www.178hui.com/zdm/add.html")
    driver.implicitly_wait(10)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(passwd)
    driver.find_element_by_id("login_submit").click()
    time.sleep(5)
    
def fill_from(url, yh, js,code,price):
    driver.switch_to_window(handles[0])
    driver.get('http://www.178hui.com/zdm/add.html')
#    time.sleep(1)
#    driver.find_element_by_id("username").send_keys(user)
#    driver.find_element_by_id("password").send_keys('3541756')
#    driver.find_element_by_id("login_submit").click()
    time.sleep(2)
    driver.find_element_by_name("url").send_keys(url)
    driver.find_element_by_id("bl_h_cuxiao").click()
    driver.find_element_by_id("step_get_info").click()
    # locator = (By.ID, 'submit') #加入加载判定条件
    time.sleep(2)
    try:
        # WebDriverWait(driver,5, 0.5).notuntil(EC.presence_of_element_located(locator)) #隐形等待判定
        #类别选择代码
        driver.find_element_by_id("price").clear()
        driver.find_element_by_id("price").send_keys(price)
        driver.find_element_by_id("youhui").send_keys(yh)
        driver.find_element_by_id('myEditor').send_keys(js)
        m1 = driver.find_element_by_xpath('//*[@id="fenlei"]')
        m1.find_element_by_xpath('//*[@id="fenlei"]/option[%d]'%(code//100)).click()
        time.sleep(1)
        m2 = driver.find_element_by_xpath('//*[@id="child_cats"]')
        m2.find_element_by_xpath('//*[@id="child_cats"]/option[%d]'%(code%100)).click()
        # os.system("pause")
        driver.find_element_by_id("submit").click()  # 点击确定爆料
        time.sleep(2)
        driver.find_element_by_class_name("res_baoliao").click()
        return True
    except:
        return False
#    finally:
#        driver.quit()   
        
    
#分类字典    
d = {'电脑数码/手机通讯':204,'电脑数码/摄影摄像':208,'电脑数码/数码配件':206,'电脑数码/影音播放':207,'电脑数码/存储设备':208,'电脑数码/网络设备':203,'电脑数码/电脑外设':203,'电脑数码/电脑整机':201,'电脑数码/电脑配件':202,'电脑数码/软件游戏':1404,'电脑数码/虚拟产品':1503,'电脑数码/智能设备':209,'电脑数码/电脑数码包':411,'家用电器/大家电':302,'家用电器/生活电器':303,'家用电器/厨房电器':301,'家用电器/个护健康':305,'运动户外/运动服饰':503,'运动户外/户外服饰':501,'运动户外/户外装备':504,'运动户外/体育项目':506,'运动户外/运动鞋袜':505,'运动户外/运动器材':506,'运动户外/户外鞋袜':502,'服饰鞋包/男装':402,'服饰鞋包/女装':401,'服饰鞋包/男鞋':405,'服饰鞋包/女鞋':406,'服饰鞋包/服装配饰':407,'服饰鞋包/女包':409,'服饰鞋包/男包':410,'服饰鞋包/功能箱包':411,'服饰鞋包/家居内衣':404,'个护化妆/面部护理':902,'个护化妆/身体护理':904,'个护化妆/女性护理':906,'个护化妆/彩妆产品':901,'个护化妆/口腔护理':905,'个护化妆/男性护理':906,'个护化妆/眼睛护理':907,'个护化妆/美发护发':903,'母婴用品/童装':403,'母婴用品/奶粉':1001,'母婴用品/营养辅食':1002,'母婴用品/喂养用品':1005,'母婴用品/尿裤湿巾':1003,'母婴用品/洗护用品':1004,'母婴用品/孕产妇用品':1008,'母婴用品/婴儿玩具':1010,'母婴用品/婴儿家居安全':1006,'日用百货/宠物用品':604,'日用百货/厨房用具':602,'日用百货/生活用品':601,'日用百货/家居清洁':603,'日用百货/成人用品':605,'食品保健/保健品':804,'食品保健/酒水饮料':802,'食品保健/粮油调味':805,'食品保健/有机食品':806,'食品保健/生鲜食品':806,'食品保健/休闲食品':801,'食品保健/节日食品':801,'食品保健/奶产品':807,'礼品钟表/礼品':1503,'礼品钟表/钟表':1102,'礼品钟表/珠宝首饰':1101,'图书音像/电子书刊':1403,'图书音像/音像制品':1402,'图书音像/图书杂志':1401,'玩模乐器/玩具':1010,'玩模乐器/模型':1010,'玩模乐器/动漫周边':1010,'玩模乐器/乐器':1503,'办公设备/办公仪器':1201,'办公设备/办公用品':1202,'办公设备/学生用品':1203,'家居家装/家装主材':702,'家居家装/五金电工':703,'家居家装/住宅家具':701,'家居家装/家纺布艺':706,'家居家装/灯具灯饰':705,'家居家装/园艺用品':707,'家居家装/家居饰品':702,'汽车消费/车载电器':1305,'汽车消费/美容清洁':1304,'汽车消费/安全自驾':1305,'汽车消费/汽车整车':1301,'汽车消费/摩托相关':1503,'汽车消费/汽车服务':1307,'汽车消费/汽车装饰':1303,'汽车消费/维修保养':1307,'金融服务/保险':1503,'金融服务/消费金融':1503,'金融服务/其他金融':1503,'金融服务/投资理财':1503,'金融服务/众筹':1503,'旅游出行/国内旅游':1503,'旅游出行/国外旅游':1503,'旅游出行/出行必备':1503,'旅游出行/旅游周边':1503,'文化娱乐/票务':1503,'文化娱乐/在线教育':1503,'文化娱乐/其他文化娱乐':1503,'房产置业/新房':1503,'房产置业/二手房':1503,'房产置业/租房':1503,'房产置业/海外置业':1503,'房产置业/其他房产置业':1503}
driver = webdriver.Firefox()
#driver.set_window_size(80,80)
driver.get('https://baidu.com')
js='window.open("https://www.sogou.com");'
driver.execute_script(js)
handles = driver.window_handles
open_web()
joyj_code = []
while True:
    while joyj_code != get_info()[0]:
        joyj_code = get_info()[0]
        yh = get_info()[2]
        js = get_info()[1]
        # js = "".join(get_info()[1:4])
        price = get_info()[4]
        flei = get_info()[3]
        jd_code = get_jd_code(joyj_code)
        if jd_code != []:
            jd_url = 'https://item.jd.com/%s.html' % jd_code[0]
        else :
            continue
        print(jd_url)
        while fill_from(jd_url, yh, js,flei,price) == True:
            print('OK')
            time.sleep(110)
            break
        else:
            continue
    else:
        continue

