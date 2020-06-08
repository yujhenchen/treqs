from src.elements import UseElement
from src import parameters
from src.scripts import generateReq
from src.scripts import generateReqDoc
from src.scripts import checkConsistency
import os
import shutil
import ntpath
import re
from html.parser import HTMLParser


# =====================================================================
# database
# read batabase
# main table
# processObj = UseElement.UseElement()
# data_db = processObj.getAllDataFromDB(parameters.usReq)
# print(data_db)
# print(type(data_db))
# print(type(data_db[0]))

# # temp table
# data_db = processObj.getAllDataFromDB(parameters.usReq, parameters.table_reqType)
# print(data_db)



# # write database
# # main table
# set_data = "'usuid12457', 'US', 'test US insert', 'eee@g.com', '2020-08-14 00:00:00', 0"
# processObj.writeDataToDB(parameters.usReq,set_data)
# print("done")

# # temp table
# processObj.writeDataToDB(parameters.usReq,set_data, parameters.table_reqType)
# print("done")


# clean tables: resetDBTable 

# =====================================================================




# =====================================================================
# # red write files
# # read file and split by spcial word
# with open(r"C:\Users\zn\Desktop\Chalmers\ProjectWork\template_files\SR_.md") as f:
#     #content = f.readlines()
#     content = f.read()#.replace("\n", " ")

#     print (content) 
#     print(type(content))

#     # get each requirement
#     content_split = content.split("&nbsp")
#     print (content_split) 
#     print(type(content_split))
#     print(content_split[0])

#     # get each element of each requirement
#     content_split_split = content_split[0].split("\n")
#     print (content_split_split) 
#     print(type(content_split_split))
#     print(len(content_split_split))
    
#     print(content_split_split[0])

#     # remove substring in a string
#     str_rreplaced = content_split_split[0].replace('<!-- ', '').replace(' -->', '') 
#     print(str_rreplaced)

#     # split with ,
#     ls_str_rreplaced = str_rreplaced.split(",")
#     print(ls_str_rreplaced)
#     print(ls_str_rreplaced[0])



# # filter test
# str_list = ['', 'dfdsfsdfd','ggg','','rbf','5df','fs g','erew','','',]
# str_list = filter(None, str_list)
# print(str_list)
# print(type(str_list))
# str_list = [ x for x in str_list ]
# print(type(str_list))
# print(str_list)

# # elements doc
# docP = docElement.docElement()
# ls_precessed = docP.getRecord(r"C:\Users\zn\Desktop\Chalmers\ProjectWork\template_files\SR_.md")
# print(ls_precessed)
# =====================================================================







# =====================================================================
# # copy file under a path
# f_path = r"C:\Users\zn\Desktop\test\US_.md"
# def navigate_and_rename(f_path):
#     for item in os.listdir(f_path):
#         s = os.path.join(f_path, item)
#         if os.path.isdir(s):
#             navigate_and_rename(s)
#         elif s.endswith(".md"):
#             shutil.copy(s, os.path.join(f_path, s +"_bk.md"))

# def navigate_and_rename( requirement, fn_full):
#     if fn_full.endswith(".md") and requirement in fn_full:
#         tuple_fn = ntpath.split(fn_full)
#         #print(type(data))
#         shutil.copy(fn_full, os.path.join(tuple_fn[0], tuple_fn[1]+"_bk.md"))
#navigate_and_rename("US",f_path)
# =====================================================================






# =====================================================================
# # read doc into pandas dataframe
# processObj = UseElement.UseElement()
# path = r"C:\Users\zn\Desktop\Chalmers\ProjectWork\cse\research\treqs\treqs\templates\US_.md"
# path = r"C:\Users\zn\Desktop\Chalmers\ProjectWork\cse\research\treqs\treqs\templates\SR_.md"
# path = r"C:\Users\zn\Desktop\Chalmers\ProjectWork\cse\research\treqs\treqs\templates\QR_.md"
# path = r"C:\Users\zn\Desktop\Chalmers\ProjectWork\cse\research\treqs\treqs\templates\TC_.md"

# processObj.readContent(parameters.usReq, path)
# print(processObj.getContent(parameters.usReq))
#print(list(processObj.getContent(parameters.usReq).columns.values))

# processObj.readContent(parameters.srReq, path)
# print(processObj.getContent(parameters.srReq))
# # print(list(processObj.getContent(parameters.srReq).columns.values))

# processObj.readContent(parameters.qrReq, path)
# print(processObj.getContent(parameters.qrReq))
# # print(list(processObj.getContent(parameters.qrReq).columns.values))

# processObj.readContent(parameters.tcReq, path)
# print(processObj.getContent(parameters.tcReq))
# # print(list(processObj.getContent(parameters.tcReq).columns.values))
# =====================================================================





# =====================================================================
# # format data from dataframe
# # write formated data into _.md file
# processObj.writContent(parameters.usReq)
# processObj.writContent(parameters.srReq)
# processObj.writContent(parameters.qrReq)
# processObj.writContent(parameters.tcReq)
# =====================================================================





# =====================================================================
# # dump dataframe into database
# processObj.writeDataFrameToDB(parameters.usReq)
# processObj.writeDataFrameToDB(parameters.srReq)
# processObj.writeDataFrameToDB(parameters.qrReq)
# processObj.writeDataFrameToDB(parameters.tcReq)
# =====================================================================





# =====================================================================
# # dump database into dataframe
# processObj.readDBToDataFrame(parameters.usReq)
# print(processObj.getContent(parameters.usReq))

# processObj.readDBToDataFrame(parameters.srReq)
# print(processObj.getContent(parameters.srReq))

# processObj.readDBToDataFrame(parameters.qrReq)
# print(processObj.getContent(parameters.qrReq))

# processObj.readDBToDataFrame(parameters.tcReq)
# print(processObj.getContent(parameters.tcReq))
# =====================================================================





# =====================================================================
# read HTML format text
# class MyHTMLParser(HTMLParser):
    # def handle_starttag(self, tag, attrs):
        # attr = dict(attrs)
        # self.links.append(attr)
# 
# text = "<treqs-element id='437f09c6-9613-11ea-bb37-0242ac130002' type='requirement'  link_us='b860686e-9b6f-11ea-bb37-0242ac130002' link_sr='b8606b20-9b6f-11ea-bb37-0242ac130002' email='person1' date='20200101 00:00:00' >This is the content of requirement</treqs-element>\n<treqs-element id='437f09c6-9613-11ea-bb37-0242ac130002' type='requirement'  link_us='b860686e-9b6f-11ea-bb37-0242ac13000' link_sr='b8606b20-9b6f-11ea-bb37-0242ac130002' email='person1' date='20200101 00:00:00' >This is the content of requirement22222222222</treqs-element>"

# parser = MyHTMLParser()
# parser.links = []
# parser.feed(text)
#for element_dic in parser.links:
#    print(element_dic)
#    print(type(element_dic))
# =====================================================================





# =====================================================================
# create html tag
#from htmltag import element
#print(element("requirement content", id="437f09c6-9613-11ea-bb37-0242ac130002", type="requirement", link_us="437f09c6-9613-11ea-bb37-0242ac130002", link_sr="437f09c6-9613-11ea-bb37-0242ac130002", email="yyy@yahii", date="20200101 00:00:00"))

# processObj = UseElement.UseElement()
# print(processObj.createElement("content", "uid", "TC", "us", "sr", "mail", "date"))
# =====================================================================


# generateReq.generate()


# generateReqDoc.generate_doc()


# f_path = r"C:\Users\zn\Desktop\test_templates\SR_.md"
# with open(f_path) as f:
#     content = f.read()
#     print(type(content))
#     print((content))


# dir_path = r"C:\Users\zn\Desktop\recur_dir"
# content = checkConsistency.readAllContent(dir_path)
# print(content)

checkConsistency.check()


# with open(r"C:\Users\zn\Desktop\recur_dir\dir_sub\bxx\c.py") as f:
#     content = f.read()
#     ls = re.findall(parameters.element_begin+'.*?'+parameters.element_end, content)
    #print(ls)
            
    #for line in f:
    #    line = line.rstrip()
    #    print(parameters.element_begin in line)
    #    print(line.endswith(parameters.element_end))
    #    if (parameters.element_begin in line) and (line.endswith(parameters.element_end)):
    #        print(line)