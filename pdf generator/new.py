# _*_ coding: utf-8 _*_
import codecs

F=codecs.open('final.csv')
content=F.read()
F.close()
print(content)