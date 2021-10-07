## 简介

用于识别正方教务管理系统的验证码模块



## 调用方法
注意： `model`文件夹和`captcha.pyd`文件是必需的

1. 下载本仓库的压缩包并解压
2. 在解压后的文件夹中创建`py`文件，代码中调用方式如下

```python
import captcha
a = captcha.recognize('code.jfif')  # 参数为验证码图片路径
print(a)
```



## 要求

验证码图片与示例文件`code.jiff`类似，大小为`72x25`

![示例](https://cdn.jsdelivr.net/gh/suxss/ZF_captcha/code.jfif)



第三方库：

```
numpy
tensorflow
PIL
```



