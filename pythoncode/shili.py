have_gift = False
def send_gift():
    global  have_gift##global的意思是：当想要改变外部函数gave_gift的值时，使用这个进行更改
    have_gift = True
    print("发礼物啦")
def show_gift():
    if have_gift == True:
        print("收到礼物啦")
    else:
        print("等待礼物中")
send_gift()
show_gift()