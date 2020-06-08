from src import parameters as param
import re
import datetime


def readFile(f_path):
    try:
        with open(f_path) as f:
            content = f.read()
            return content
    except Exception:
        print("readFile Exception")
        return ""


def writeFileAppend(f_path, title, content):
    try:
        with open(f_path, "a") as f:
            f.write(title+param.sep_newline)
            f.write(content+param.sep_newline+param.sep_newline)
    except Exception:
        print("writeFile Exception")


def readTestcodeElements(f_path):
    try:
        with open(f_path) as f:
            content = f.read()
            ls = re.findall(param.element_begin+'.*?'+param.element_end, content)
            return param.sep_newline.join(ls)
    except Exception:
        print("readTestcodeFile Exception")
        return ""


def getDateTimeStr():
    datetime_obj = datetime.datetime.now()
    str_date = datetime_obj.strftime("-%b%d%Y-%H%M%S")
    return str(datetime_obj.year)+str(datetime_obj.month)+str(datetime_obj.day)+'-'+str(datetime_obj.hour)+str(datetime_obj.minute)+str(datetime_obj.second)
