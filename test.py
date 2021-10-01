import captcha


if __name__ == '__main__':
    a = captcha.recognize('code.jfif')    # 参数为验证码图片路径
    print(a)
