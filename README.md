# Project Title

Talent Engine 2.0 

## Description

Project contains code created during Talent Engine.  

## Getting Started

### Dependencies

Before installing repository you have to instal PIP - package installer for python
```
pip install pip
```

### Installing
Install the mandatory modules using 
```
pip install -r requirements.txt
```

### Executing program

To execute tests type 
```
pytest
```
To execute tests in specific browser use ```--browser``` flag
 ```
pytest -- browser=firefox
```
Available browsers:
- chrome
- firefox
- edge

If browser flag not added, tests will be executed in Chrome

## Before commit
Sort and format your code using 
```
black .
isort .
```

## Authors

Kamil Roslan
kamil.roslan@globallogic.com
