import qrcode
while True:
    content = input("请输入扫码后想显示的内容：")
    if content == 'q':
        break
    else:
        img = qrcode.make(content)
        pic = content + '.png'
        with open('test.png', 'wb') as f:
            img.save(pic)
        # img.save(pic)
        print('二维码' + pic + '已生成！ \n')
# 没用的代码