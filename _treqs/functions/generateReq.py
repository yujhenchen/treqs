import os
from git import Repo
from datetime import datetime
from _treqs import parameters as param
from _treqs.elements import UseRequirement
from _treqs import commonFuns
import uuid


def generate():
    # get user input -> find link US or SR  -> print formated requirement element
    requirement = input("Type of requirement:")
    link_other=""
    link_element=""
    if requirement == param.usReq:
        link_element = set_requirement_link(param.usReq)
    elif requirement == param.srReq:
        link_other = set_requirement_link(param.usReq)
        link_element = set_requirement_link(param.srReq)
    elif requirement == param.qrReq:
        link_other = set_requirement_link(param.srReq)
        link_element = set_requirement_link(param.qrReq)
    elif requirement == param.tcReq:
        link_other = set_requirement_link(param.srReq)
        link_element = set_requirement_link(param.tcReq)
    else:
        print("Unknown requirement type!")
        generate()

    content = input("Input content:")
    generated_req = form_generated(requirement, content, link_other, link_element)
    # print formated result of genrated requirement
    print("Copy the text below into requirement document:")
    print(generated_req)


def generate_uid(requirement):
    # return requirement+'_'+str(uuid.uuid1().hex)
    return requirement+'_'+str(uuid.uuid1().hex)


def getDateTime():
    now = datetime.now().date()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def getEmail():
    repo = Repo('.', search_parent_directories=True)
    path = repo.working_tree_dir
    path = os.path.normpath(path)
    reader = repo.config_reader()
    email = reader.get_value(param.user, param.email)
    return email


def form_generated(requirement, content, link_other="", link_element=""):
    uid = generate_uid(requirement)
    dateTime = getDateTime()
    email = getEmail()
    # base on different requirement, generate different format and print on the screen
    useRequirement = UseRequirement.UseRequirement()
    return useRequirement.createElement(content, uid, requirement, link_other, link_element, email, dateTime)
    

def set_requirement_link(requirement):
    # ask user input target requirement file path
    # read file into dataframe and print
    path = input("Choose "+requirement+" file path:")

    useRequirement = UseRequirement.UseRequirement()
    # useRequirement.readContent(requirement, path)
    useRequirement.readContent(requirement, commonFuns.readFile(path))
    df = useRequirement.getContent(requirement)
    if len(df.index) > 0:
        print(df)
    else:
        print("requirements of "+requirement+" is empty.")

    link = input("Choose link "+requirement+" uid:")
    return link