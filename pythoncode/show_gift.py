import demo_gift
def shw_gift():
    have_gift=demo_gift.have_gift
    if have_gift == True:
        print("收到礼物啦")
    else:
        print("等待礼物中")