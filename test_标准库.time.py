import time#导入时间模块，python自带的，不需要额外安装

print(time.time())
print(time.asctime())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

#获取两天前的时间
now_timestamp = time.time()#当前时间戳
two_day_before = now_timestamp - 60*60*24*2#两天前的时间=当前时间减去”一份钟60秒，一小时60分钟，一天24小时，一共2天“
time_tuple = time.localtime(two_day_before)#将时间戳转换成时间元组
print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))#将时间戳转换成带格式的时间
