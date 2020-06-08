from src import parameters as param
import re
from datetime import datetime
from git import Repo
import os


def read_file(f_path):
    try:
        with open(f_path) as f:
            content = f.read()
            return content
    except Exception:
        print("read_file Exception")
        return ""


def write_file_append(f_path, title, content):
    try:
        with open(f_path, "a") as f:
            f.write(title+param.SEP_NEWLINE)
            f.write(content+param.SEP_NEWLINE+param.SEP_NEWLINE)
    except Exception:
        print("write_file_append Exception")


def read_testcode_elements(f_path):
    try:
        with open(f_path) as f:
            content = f.read()
            ls = re.findall(param.ELEMENT_BEGIN+'.*?'+param.ELEMENT_END, content)
            return param.SEP_NEWLINE.join(ls)
    except Exception:
        print("read_testcode_elements Exception")
        return ""


def string_to_bool(str):
    if str == 'y':
        return True
    else:
        return False


def get_datetime(b_format):
    now = datetime.now().date()
    if b_format:
        return now.strftime("%Y-%m-%d_%H%M%S")
    else:
        return now.strftime("%Y-%m-%d %H:%M:%S")


def get_email():
    repo = Repo('.', search_parent_directories=True)
    path = repo.working_tree_dir
    path = os.path.normpath(path)
    reader = repo.config_reader()
    email = reader.get_value(param.USER, param.EMAIL)
    return email
