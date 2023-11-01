# Cookiecutter ORM

Cookiecutter template for whenever you just want to connect to a database (or two!) and use SQLAlchemy. This project is forked from the fantastic [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/), go check it out!

## But why?

SQLAlchemy can be quite powerful, but most tutorials are focused on integrating it into an application you are developing from the very beginning. However, SQLAlchemy can also help when you just want to explore an _existing_ database! This is not a replacement to a proper DBMS, but leveraging python and the models from SQLAlchemy can still speed up development in projects such as:

- Exploring an existing database and querying basic data
- Migrating data between two databases, applying the relevant transformations and dataa enhancements
- Exporting data to other services

## But _how?_

SQLAlchemy relies on models defined in code. Typically, you'd have to define them yourself, but they can also be grabbed from an existing database using [SQLACodegen](https://github.com/agronholm/sqlacodegen). Furthermore, these models can be used to generate a simple png view of the tables to aid in that first discovery phase!


## Feature roadmap

- [x] Basic project structure and prompts 
- [x] Connection string generator
- [x] Model generator
- [ ] ER model printer
- [ ] Autopopulate a basic jupyter notebook with the models that were created previously
- [ ] Fill requirements.txt with the right dependencies

### Requirements to use the cookiecutter template:
-----------
 - Python 3.8-3.10+ (Python 3.11 and 3.12 can't export the database models)
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/TaruDesigns/cookiecutter-pyorm



### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```


### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
