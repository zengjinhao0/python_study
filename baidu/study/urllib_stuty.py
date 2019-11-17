
import urllib.request

response = urllib.request.urlopen("http://www.python.org")
#它是一个 HTTPResposne 类型的对象
#主要包含 read （）【页面内容】 readinto （）、 getheader(name ）、gethea ders （） fileno （）等方法
# 以及 msg 、version、 status、 reason、 debuglevel、 closed 等属性
#得到这个对象之后，我们把它赋值为 response 变量，然后就可以调用这些方法和属性，得到返回结果的－系列信息了
print(type(response))
#print(response.read().decode("utf-8"))




data =  bytes(urllib.parse.urlencode({"word":"hello"}),encoding="utf-8")
response2 = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response2.read())