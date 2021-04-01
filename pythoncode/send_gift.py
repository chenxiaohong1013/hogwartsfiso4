have_gift = False
def send_gift():
    global have_gift
    have_gift = True
    print("发礼物啦")
def show_gift():
    if have_gift == True:
        print("收到礼物啦")
    else:
        print("等待礼物中")

send_gift()
show_gift()

