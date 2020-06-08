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

## Running the tests

A test script test.py is under '/tests' directory.

### Example of using test script

Execute treqs funstions by uncomment the following line in test.py:

```
checkConsistency.check()
```

## Functions of T-Reqs

Change directory to the example project.

### Generate requirement

input command:

```
generatereq
```
workflow:

@startuml
actor Developer
participant Treqs
participant Project

'generate requirement
group Generate requirement

Developer->Treqs: generatereq
Developer->Treqs: select requirement type
Developer->Treqs: choose requirements document
Developer->Treqs: choose link requirement
Developer->Treqs: choose parent requirement in document (if any)
Developer->Treqs: input requirement content
Treqs->Developer: generate requirement tag
Developer->Project: copy requirement tag into requirements document
end

@enduml


### Generate requirements document

input command:

```
generatereqdoc
```

### Check consistency

input command:

```
treqs
```

## Authors

* **Yu-Jhen Chen** - *Initial work* - [yujhenchen](https://github.com/yujhenchen)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Further reading

* [RE for Large-Scale Agile System Development](https://oerich.wordpress.com/2017/06/28/re-for-large-scale-agile-system-development/) 
* [T-Reqs: Tool Support for Managing Requirements in Large-Scale Agile System Development](https://arxiv.org/abs/1805.02769)
* [Requirements Engineering for Large-Scale Agile System Development: A Tooling Perspective](https://odr.chalmers.se/handle/20.500.12380/300667)
