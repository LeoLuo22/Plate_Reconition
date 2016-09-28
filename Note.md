#基于openALPR的车牌识别系统
##*2016/9/24
***
今天是开发的第一天，感触颇多。早上起来一直在想自己基于opencv造个轮子，
但事实证明不大现实，大二学的数字图像处理忘得差不多。然后开始在网上
寻找现成的开源库，搜索到了[openALPR](https://github.com/openalpr/openalpr)
下面是官方对它的介绍
>OpenALPR is an open source Automatic License Plate Recognition library written in C++ with bindings in C#, Java, Node.js, Go, and Python. The library analyzes images and video streams to identify license plates. The output is the text representation of any license plate characters.OpenALPR is written in C++ and has bindings in C#, Python, Node.js, Go, and Java. Please see this guide for examples showing how to run OpenALPR in your application: http://doc.openalpr.com/bindings.html

下午一开始下载了opencv,还有openALPR自己编译，问题颇多。后来下载了预编译版本的
（说到这里不得不吐槽一下官方目前的2.3版本没有python的代码）。从2.3一路下载到了2.0.1，
各种问题都遇到过。但最主要的问题是是下面两个（耗费了整个下午):
1- 运行包里自带的test.py,显示cannot import the name "ALPR"
    这个问题的解决实验过在site-package里新增.pth文件，还有就是放在一个目录下，
    统统不行。最后只能将源代码合并到一个文件。
2- **ctypes.ArgumentError: argument 1: <class 'TypeError'>: wrong type
    第一个问题解决后紧接着的哥个问题就来了，说是类型错误。
这个问题困扰我好久。因为arguments的类型都是ctypes.c_char_p，对应的就是字符串类型。
但是无论传什么字符串都不行。万能的Google上关于这方面的搜索结果只有寥寥几个。
后来在StackOverFlow上面找到一个类似的问题，I quote，>Basically you need to specify that you are passing byte data rather than a string using b'Window Title'。
就是在字符串前加b,转换成bytes类型。抱着试一试的心态真的成功了。后来又遇到一下
关于json的问题，不过这些都是关于str和bytes转换的简单问题。很好解决。

##*2016/9/27
    nothing
##*2016/9/28
    1.rest:REpresentational State Transfer
