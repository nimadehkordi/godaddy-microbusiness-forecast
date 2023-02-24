# Project Title

## Introduction

This is a project for the [Godaddy Microbusiness Density Forecasting](https://www.kaggle.com/c/godaddy-microbusiness-density-forecasting) competition on Kaggle. The objective of this competition is to predict the density of microbusinesses in US counties, which are often not reflected in traditional economic data sources due to their small size or recent establishment. Since historical economic data is readily accessible, the competition focuses on forecasting. The competition will have a public leaderboard and a final private leaderboard, both of which will be based on data gathered after the submission deadline. Contestants must make static predictions that can only incorporate information available before the end of the submission period. While submissions will be rescored during the forecasting phase, notebooks will not be re-executed.

## Table of Contents

- [Project Title](#project-title)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Dataset](#dataset)
  - [Methodology](#methodology)
  - [Code Structure](#code-structure)
  - [Results](#results)
  - [Future Work](#future-work)
  - [Authors](#authors)
  - [License](#license)

## Getting Started

Install miniconda3 and create a new environment with the name tf:

    $ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    $ bash Miniconda3-latest-Linux-x86_64.sh
    $ conda env create -f environment.yml -n tf

Install dependencies for jyupter notebook and add the kernel:

    $ conda install --name tf -c anaconda ipykernel
    $ python -m ipykernel install --user --name tf --display-name "Python (tf)"


To download the data, run the following command:

    $ mkdir data
    $ cd data
    $ kaggle competitions download -c godaddy-microbusiness-density-forecasting

## Dataset

The objective of this competition is to predict the density of microbusinesses in US counties, which are often not reflected in traditional economic data sources due to their small size or recent establishment. Since historical economic data is readily accessible, the competition focuses on forecasting. The competition will have a public leaderboard and a final private leaderboard, both of which will be based on data gathered after the submission deadline. Contestants must make static predictions that can only incorporate information available before the end of the submission period. While submissions will be rescored during the forecasting phase, notebooks will not be re-executed.

## Methodology



## Code Structure

```
├── README.md
├── environment.yml
├── data
│   ├── sample_submission.csv
│   ├── test.csv
│   └── train.csv
├── notebooks
│   ├── eda.ipynb
├── src
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── make_dataset.py
│   │   └── preprocess.py
│   ├── features
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── model.py
│   │   ├── predict_model.py
│   │   └── train_model.py
│   └── visualization
│       ├── __init__.py
│       └── visualize.py
└── tests
    ├── __init__.py
    └── test_make_dataset.py
```

## Results


## Future Work


## Authors

Nima Riahi Dehkordi - [GitHub](https://github.com/nimadehkordi) - [LinkedIn](https://www.linkedin.com/in/nimariahidehkordi/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

