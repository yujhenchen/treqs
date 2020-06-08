from src import parameters as param
from src.elements import UseElement
from src import utilities

def generate_doc():
    path = input("Path of requirements file:")
    requirement = input("Type of requirement:")

    useElement = UseElement.UseElement()
    #useElement.read_content(requirement, path)
    useElement.read_content(requirement, utilities.read_file(path))
    
    useElement.prepare_customids(requirement)
    # print(useElement.get_content(requirement))
    useElement.write_content(requirement, path)