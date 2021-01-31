def rand_select(option):
    import random
    rand = random.random()
    for i in range(len(option)):
        if rand < 1 / len(option) * (i + 1):
            return option[i]

def word(text):
    from docx import Document
    from docx.shared import Pt
    from docx.shared import Inches
    from docx.oxml.ns import qn
    font = ["萌妹子体", "李国夫手写体", "陈静的字完整版"]
    doc = Document()
    para = doc.add_paragraph(" ")
    for i in text:
        run = para.add_run(i)
        run.font.name = rand_select(font)
        run.font.size = 300000
        run._element.rPr.rFonts.set(qn('w:eastAsia'), run.font.name)
    doc.save("temporary\\text.docx")
word("功能：读取txt文本，然后将目的字符串标红，再将处理过的字符串写入docx中txt文本内容：啊打发发烧鳌太路线点击点击诶的骄傲计划将鳌太标红代码：")