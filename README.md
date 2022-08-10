# 作业生成器

*妈妈再也不用担心我交不上网课作业了*

## **1. 功能介绍**

  - 输入文本，输出带有手写字的作业本图片
  - 一定范围内随机字号，模拟潦草字迹
  - 三种字体随机切换，防止叠词露馅
  - 输出图片随机旋转裁切，模拟自然拍摄

## **2. 依赖安装**

在合适的目录下打开命令行执行以下命令(若无git则忽略第一行直接下载压缩包)

    git clone https://github.com/Yuxuan10086/homework_creator.git
    pip install python-docx
    pip install opencv-python
    pip install docx2pdf

以上命令执行速度预计会很慢，请耐心等待，若执行失败请重新执行

完成后安装font文件夹中的三个字体

## **3. 使用方法**

1. 在`input.txt`文件中输入要转换的文本
1. 如果程序目录下没有`temporary`文件夹则自行新建
1. 如果程序目录下没有`res`文件夹则自行新建
1. 在程序目录下输入以下命令

        python homework_creator.py

1. 出现提示`continue?(Y/N)`时，打开`temporary\text.docx`，检查文档中是否出现字体未覆盖到的字(表现为被替换成其他印刷字体)，若有则删除对应字或将其改为其他手写字体，直到通篇为手写字时关闭文档
2. 在命令行中键入`Y`
3. 等候程序执行完毕，在文件夹`res`中查看结果