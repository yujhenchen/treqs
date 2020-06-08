from src.elements import UseElement
from src import parameters as param
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
# data_db = processObj.getAllDataFromDB(param.US_REQ)
# print(data_db)
# print(type(data_db))
# print(type(data_db[0]))

# # temp table
# data_db = processObj.getAllDataFromDB(param.US_REQ, param.table_reqType)
# print(data_db)



# # write database
# # main table
# set_data = "'usuid12457', 'US', 'test US insert', 'eee@g.com', '2020-08-14 00:00:00', 0"
# processObj.writeDataToDB(param.US_REQ,set_data)
# print("done")

# # temp table
# processObj.writeDataToDB(param.US_REQ,set_data, param.table_reqType)
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

# processObj.read_content(param.US_REQ, path)
# print(processObj.get_content(param.US_REQ))
#print(list(processObj.get_content(param.US_REQ).columns.values))

# processObj.read_content(param.SR_REQ, path)
# print(processObj.get_content(param.SR_REQ))
# # print(list(processObj.get_content(param.SR_REQ).columns.values))

# processObj.read_content(param.QR_REQ, path)
# print(processObj.get_content(param.QR_REQ))
# # print(list(processObj.get_content(param.QR_REQ).columns.values))

# processObj.read_content(param.TC_REQ, path)
# print(processObj.get_content(param.TC_REQ))
# # print(list(processObj.get_content(param.TC_REQ).columns.values))
# =====================================================================





# =====================================================================
# # format data from dataframe
# # write formated data into _.md file
# processObj.writContent(param.US_REQ)
# processObj.writContent(param.SR_REQ)
# processObj.writContent(param.QR_REQ)
# processObj.writContent(param.TC_REQ)
# =====================================================================





# =====================================================================
# # dump dataframe into database
# processObj.writeDataFrameToDB(param.US_REQ)
# processObj.writeDataFrameToDB(param.SR_REQ)
# processObj.writeDataFrameToDB(param.QR_REQ)
# processObj.writeDataFrameToDB(param.TC_REQ)
# =====================================================================





# =====================================================================
# # dump database into dataframe
# processObj.readDBToDataFrame(param.US_REQ)
# print(processObj.get_content(param.US_REQ))

# processObj.readDBToDataFrame(param.SR_REQ)
# print(processObj.get_content(param.SR_REQ))

# processObj.readDBToDataFrame(param.QR_REQ)
# print(processObj.get_content(param.QR_REQ))

# processObj.readDBToDataFrame(param.TC_REQ)
# print(processObj.get_content(param.TC_REQ))
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
# print(processObj.create_element("content", "uid", "TC", "us", "sr", "mail", "date"))
# =====================================================================


# generateReq.generate()


generateReqDoc.generate_doc()


# f_path = r"C:\Users\zn\Desktop\test_templates\SR_.md"
# with open(f_path) as f:
#     content = f.read()
#     print(type(content))
#     print((content))


# dir_path = r"C:\Users\zn\Desktop\recur_dir"
# content = checkConsistency.read_all_content(dir_path)
# print(content)

# checkConsistency.check()


# with open(r"C:\Users\zn\Desktop\recur_dir\dir_sub\bxx\c.py") as f:
#     content = f.read()
#     ls = re.findall(param.ELEMENT_BEGIN+'.*?'+param.ELEMENT_END, content)
    #print(ls)
            
    #for line in f:
    #    line = line.rstrip()
    #    print(param.ELEMENT_BEGIN in line)
    #    print(line.endswith(param.ELEMENT_END))
    #    if (param.ELEMENT_BEGIN in line) and (line.endswith(param.ELEMENT_END)):
    #        print(line)