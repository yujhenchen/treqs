import os
import datetime
from _treqs import parameters as param
from _treqs.elements import UseRequirement
from _treqs.elements import UseRequirement
from _treqs import commonFuns

def generate_doc():
    path = input("Path of requirements file:")
    requirement = input("Type of requirement:")

    useRequirement = UseRequirement.UseRequirement()
    #useRequirement.readContent(requirement, path)
    useRequirement.readContent(requirement, commonFuns.readFile(path))
    
    useRequirement.prepareCustomIds(requirement)
    # print(useRequirement.getContent(requirement))
    useRequirement.writeContent(requirement, path)