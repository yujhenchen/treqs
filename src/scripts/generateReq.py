from src import parameters as param
from src.elements import UseElement
from src import utilities
import uuid


def generate():
    # get user input -> find link US or SR  -> print formated requirement element
    requirement = input("Type of requirement:")
    link_other=""
    link_element=""
    if requirement == param.US_REQ:
        link_element = set_requirement_link(param.US_REQ)
    elif requirement == param.SR_REQ:
        link_other = set_requirement_link(param.US_REQ)
        link_element = set_requirement_link(param.SR_REQ)
    elif requirement == param.QR_REQ:
        link_other = set_requirement_link(param.SR_REQ)
        link_element = set_requirement_link(param.QR_REQ)
    elif requirement == param.TC_REQ:
        link_other = set_requirement_link(param.SR_REQ)
        link_element = set_requirement_link(param.TC_REQ)
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




def form_generated(requirement, content, link_other="", link_element=""):
    uid = generate_uid(requirement)
    dateTime = utilities.get_datetime(False)
    email = utilities.get_email()
    # base on different requirement, generate different format and print on the screen
    useElement = UseElement.UseElement()
    return useElement.create_element(content, uid, requirement, link_other, link_element, email, dateTime)
    

def set_requirement_link(requirement):
    # ask user input target requirement file path
    # read file into dataframe and print
    path = input("Choose "+requirement+" file path:")

    useElement = UseElement.UseElement()
    # useElement.read_content(requirement, path)
    useElement.read_content(requirement, utilities.read_file(path))
    df = useElement.get_content(requirement)
    if len(df.index) > 0:
        print(df)
    else:
        print("requirements of "+requirement+" is empty.")

    link = input("Choose link "+requirement+" uid:")
    return link