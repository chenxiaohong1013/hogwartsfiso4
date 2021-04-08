import os#导入os模块，os模块是python系统自带的，不需要安装

#os.mkdir("testos")#创建目录

#os.removedirs("testos")#删除目录

#print(os.getcwd())#查询当前目录的全路径地址

print(os.path.exists("b"))#读取当前路径有没有b文件
if not os.path.exists("b"):#如果没有b文件
    os.mkdir("b")#就创建b文件
if not os.path.exists("b/test.txt"):#如果没有"b/test.txt"文件
    f = open("b/test.txt","w")#打开"b/test.txt"可写文件
    f.write("hello,os using")#写入hello,os using
    f.close()#关闭文件


