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
