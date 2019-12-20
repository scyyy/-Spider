import xlwt,xlrd

wb = xlwt.Workbook()
sh = wb.add_sheet('test_1')
sh.write(0,0,'Index')
sh.write(0,1,'Titles')
sh.write(0,2,'Times')
sh.write(0,3,'Mains')
sh.write(0,4,'Urls')
sh.write(0,5,'Year')
sh.write(0,6,'Source')
wb.save('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/集合.xls')#保存
