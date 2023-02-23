Install project dependencies:

    $ conda env create -f environment.yml

Install dependencies for jyupter notebook:

    $ conda install --name tf -c anaconda ipykernel

Add the kernel to jupyter:

    $ python -m ipykernel install --user --name tf --display-name "Python (tf)"


To download the data, run the following command:

    $ mkdir data
    $ cd data
    $ kaggle competitions download -c godaddy-microbusiness-density-forecasting
