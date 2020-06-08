# T-Reqs: Tooling to enable teams to manage system requirements in large-scale agile system develpment

version 3.0

## Getting Started

Set up the project with the following steps:

### Prerequisites

The following installation should be done.

```
Python 3.x
```

### Installing

Clone Git repository of the project:

```
git clone https://github.com/yujhenchen/treqs.git
```

Change directory to 'treqs', which contains setup.py file. Install the project and its dependencies:

```
pip install -e .
```

## Functions of T-Reqs

### Generate requirement

Change directory to the example project. Input command:
```
generatereq
```

#### Steps:

treqs requires a requirement type. The supporting types of the project are: **US** (user story), **SR** (system requirement), **QR** (quality requirement), and **TC** (test case)
```
Type of requirement:
```

treqs requires a full absolute path of link requirement:
```
Choose XX file path:
```

treqs requires the uid of link requirement:
```
Choose link XX uid:
```

treqs requires a full absolute path of parent requirement in the same requirement document (if there is any):
```
Choose XX file path:
```

treqs requires the uid of parent requirement (if there is any):
```
Choose link XX uid:
```

treqs requires the content of requirement:
```
Input content:
```

Copy the generated text to the target requirement document. The text is presented as:
```
<element id=...></element>
```

### Generate requirements document

Input command:
```
generatereqdoc
```
#### Steps:

treqs requires a full absolute path of a requirements file:
```
Path of requirements file:
```

treqs requires a requirement type. The supporting types of the project are: **US** (user story), **SR** (system requirement), **QR** (quality requirement), and **TC** (test case)
```
Type of requirement:
```

A newly generated .md file can be found in the given directory. This file is a requirements document that contains the numeric ID of each requirement in the requirements document.

### Check consistency

Input command:
```
treqs
```

Select requirement types that intend to check:
```
Check user stories? (y or n):
Check system requirement? (y or n):
Check quality requirement? (y or n):
Check test case? (y or n):
```

treqs requires a full absolute directory of these requirements files:
```
Elements files directory:
```

treqs requires a file pattern for each requirement type:
```
US file pattern:
SR file pattern:
QR file pattern:
TC file pattern:
```

If the test case is chosen, treqs requires full absolute directory of test codes and file pattern of test codes:
```
Test code files directory:
TC file pattern:
```

A newly generated summary_XXX.txt file can be found in the given directory. This file provides results of consistency checking.

## Authors

* **Yu-Jhen Chen** - [yujhenchen](https://github.com/yujhenchen)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Further reading

* [RE for Large-Scale Agile System Development](https://oerich.wordpress.com/2017/06/28/re-for-large-scale-agile-system-development/) 
* [T-Reqs: Tool Support for Managing Requirements in Large-Scale Agile System Development](https://arxiv.org/abs/1805.02769)
* [Requirements Engineering for Large-Scale Agile System Development: A Tooling Perspective](https://odr.chalmers.se/handle/20.500.12380/300667)
