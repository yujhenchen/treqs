# TReqs requirements

<treqs-element id="35590bca-960f-11ea-bb37-0242ac130002" type="requirement" >

## List TReqs Elements
TReqs shall be able to list treqs-elements within a specified gitlab project.

> Example:

    treqs list

<treqs-element id="437f09c6-9613-11ea-bb37-0242ac130002" type="requirement" >

### Filter by type 
TReqs shall allow to list treqs-elements within a specified gitlab project that have a specific type (e.g. requirement, test, quality requirement).
<treqs-link type="parent" target="35590bca-960f-11ea-bb37-0242ac130002" />

> Example:

    treqs list --type=requirement

</treqs-element>

<treqs-element id="a0820b4a-9614-11ea-bb37-0242ac130002" type="requirement" >

### Filter by ID 
TReqs shall allow to list treqs-elements within a specified gitlab project that have a specific ID.
<treqs-link type="parent" target="35590bca-960f-11ea-bb37-0242ac130002" />

> Example:

    treqs list --id="35590bca-960f-11ea-bb37-0242ac130002"

</treqs-element>

<treqs-element id="a0820e06-9614-11ea-bb37-0242ac130002" type="requirement" >

### Default output 
When listing treqs-elements, treqs by default returns a map that contains the id as key and the first line of the content (in this example, usually a heading) as element. 
<treqs-link type="parent" target="35590bca-960f-11ea-bb37-0242ac130002" />
</treqs-element>

</treqs-element>

<treqs-element id="97a8fb92-9613-11ea-bb37-0242ac130002" type="requirement" >

> Examples:
> Minimal example (returns a treqs-element with a newy generated id of the specified type and prints it on commandline)

    treqs create --type=requirement

> Specify a file to append the new element automatically (may be useful if called from within a tool)    

    treqs create --type=requirement --targetfile="requirements/SR_requirements.md" --content="text of new requirement\n may have several lines"


## Create TReqs Elements
TReqs shall be able to create treqs-elements within a specified gitlab project.

Suggestion:

- Have a function that returns text to the terminal/console, which then can be copied and pasted into a markdown file or header of an automated test
- Allow to specify a file to which the new element should be appended
- Such a function could take optional paramenters, such as type and test. If those are missing, just an empty treqs-element structure is returned.

</treqs-element>


# A few more rough thoughts (EK)

## consistency aspects
- The functions specfied above would create a common infrastructure. In addition, it should be possible to get all tracelinks to and from a treqs-element.
- In addition, it should be possible to store within a gitlab project 
   - a requirements information model (i.e. which treqs-elements are allowed in this gitlab-project) and 
   - a traceability information model (i.e. which types of links are allowed/required between treqs-elements)
- since that might be difficult, we might go for a different approach
   - since the convenience functions above provide good infrastructure, the gitlab project could store instead consistency rules
   - such consistency rules are written in python and executed by the treqs command
   - a rule can _fire_, i.e. add a line to a log consisting of criticality, location, message, description (including suggestions for fixing)
   - rules could for example check whether mandatory tracelinks exist. 
   - they could also check certain conventions or writing rules (e.g. avoiding weakwords, passive voice, ...)
   
It should be a good practice to check consistency before pushing, thus, these rules resemble unit tests.
   
## Replacement rules

In addition to consistency, we have a lot of things where treqs should add automatically generated stuff to a markdown file.

- Mebrahtom's approach to modeling, where a script generates a line that calls the plantuml webservice for generating a picture of each plantuml diagram
- One could generate some markdown text with links to elements

Those should, of course, be marked somehow, since the next execution should overwrite them. 

It is conceivable to automatically execute those on commit or push.



## test requirement tag
1<treqs-element id="437f09c6-9613-11ea-bb37-0242ac130002" type="requirement"  linked_us="b860686e-9b6f-11ea-bb37-0242ac130002" parent_sr="b8606b20-9b6f-11ea-bb37-0242ac130002"> this is the content of requirement</treqs-element>


<b>1.1</b><treqs-element id="437f09c6-9613-11ea-bb37-0242ac130002" type="requirement"  linked_us="b860686e-9b6f-11ea-bb37-0242ac130002" parent_sr="b8606b20-9b6f-11ea-bb37-0242ac130002"> this is the content of requirement2</treqs-element>

<b>SR1</b><element id="3552adb8-9b99-11ea-bb37-0242ac130002" type="SR" link_us="3552b1be-9b99-11ea-bb37-0242ac130002" link_element="root" email="person1" date="20200101 00:00:00">SR 1</element>

SR1.1 <treqs-element id="3552b0ec-9b99-11ea-b837-0242ac130002" type="SR" link_us="3552b286-9b99-11ea-bb37-0242ac130002" link_element="3552adb8-9b99-11ea-bb37-0242ac130002" email="XXXXX" date="20200000 00:00:00">This shoud be 1.1</element>

SR2 <element id="3552affc-9b99-11ea-bb37-0242ac130002" type="SR" link_us="3552b286-9b99-11ea-bb37-0242ac130002" link_element="root" email="person1" date="20200101 00:00:00">SR 2</element>

SR2.1 <element id="3552b0ec-9b99-11ea-bb37-0242ac130002" type="SR" link_us="3552b286-9b99-11ea-bb37-0242ac130002" link_element="3552affc-9b99-11ea-bb37-0242ac130002" email="person1" date="20200101 00:00:00">SR 2.1</element>


