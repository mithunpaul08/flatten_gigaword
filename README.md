This is the same code as [this](https://github.com/nelson-liu/flatten_gigaword) with the exception that each news article will be written as plain text in a separate file. This is useful if you
are doing information retrieval for example using bm25


# Flattening the Gigaword Datset

The scripts in this repository dump the text of the Gigaword dataset into a single file, for use 
with language modeling (and other!) toolkits.

See my [blog post on flattening the Gigaword corpus](https://blog.nelsonliu.me/2017/09/23/flattening-the-gigaword-corpus/) for 
more information about how the code in this repo works.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation


This project was developed in Python 3.6, but should work with Python 3.x and 2.x.
Please raise an issue if you find that this is not the case.

[Conda](https://conda.io/) will set up a virtual environment with the exact
version of Python used for development along with all the dependencies
needed to run the code in this package.

1.  [Download and install conda](https://conda.io/docs/download.html).

2.  Create a conda environment with Python 3.6.

    ```
    conda create -n flat python=3.6
    ```

3.  Now activate the conda environment.

    ```
    source activate flat
    ```

4.  Install the required dependencies with `pip`.

    ```
    pip install -r requirements.txt
    ```

5.  Install the required SpaCy data pack.
    ```
    python -m spacy download en
    ```
6. ate: if you have a conda environment you can run `mamba install parallel`


Extra info: for whatever reason you choose to run Parallel in codna    To run this code, you must have **GNU Parallel**. This can be installed on Ubuntu with:

```
sudo apt-get install parallel
```
more details about GNU Parallel is kept [here](./flatten_all_gigaword.sh /home/jovyan/data-store/home/mithunpaul08/lestat/data/gigaword/only_one_input_file/ /home/jovyan/data-store/home/mithunpaul08/lestat/data/flattened_gigaword_2009_2010/articles_from_only_one_gigaword_input_file/ 2)


upd
## Usage

[`flatten_one_gigaword.py`](./flatten_one_gigaword.py) takes in the path of a Gigaword data file
and an output directory to write a flattened version to. The bash script at 
[`flatten_all_gigaword.sh`](./flatten_all_gigaword.sh) is a thin wrapper that feeds the paths of all the
Gigaword data files to [`flatten_one_gigaword.py`](./flatten_one_gigaword.py) and combines the final output.

[`flatten_all_gigaword.sh`](./flatten_all_gigaword.sh) takes in three positional arguments:

- The path to the Gigaword directory, with all of the data files unzipped.
- You can use this command from the root dir (the one which has data folder) to recursively unzip all the files
  - `find . -name "*.gz" | xargs -P 5 -I fileName sh -c 'gzip -d "$(dirname "fileName")/$(basename -s .zip "fileName")" "fileName"'`
- A directory to write the flattened files to and the final combined output. 
    It will be created if it does not exist.

- The number of files to process at once.

For example, you can run:

```
./flatten_all_gigaword.sh /Users/mitch/research/lestat/GIGAWORD/only_2010_html_data/ /Users/mitch/research/lestat/GIGAWORD/only_2010_data_flattened_one_article_per_document/ 24
```

Or if you want to run just the python file on a sample data

`python flatten_one_gigaword.py --gigaword-path /Users/mitch/research/lestat/GIGAWORD/small_gigaword_eng_html --output-dir data/output/`

to extract data (in parallel, processing 24 files at a time) from the Gigaword corpus 
at `./data/gigaword_eng_5/` and write the flattened files + combined output to `tmp/`. 
