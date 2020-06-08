import os
import datetime
from src import parameters as param
from src.elements import UseElement
from src.elements import UseElement
from src import utilities

def generate_doc():
    path = input("Path of requirements file:")
    requirement = input("Type of requirement:")

    useElement = UseElement.UseElement()
    #useElement.readContent(requirement, path)
    useElement.readContent(requirement, utilities.readFile(path))
    
    useElement.prepareCustomIds(requirement)
    # print(useElement.getContent(requirement))
    useElement.writeContent(requirement, path)