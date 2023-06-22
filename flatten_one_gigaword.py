import logging
import os
import re
import spacy

from argparse import ArgumentParser
from bs4 import BeautifulSoup

en_nlp = spacy.load("en_core_web_sm")


def flatten_one_gigaword_file(file_path):
    # Parse the text with BeautifulSoup
    soup = BeautifulSoup(open(file_path), "html.parser")

    # Iterate over all <p> items and get the text for each.
    all_paragraphs = []

    for doc in soup("doc"):
        # Turn inter-paragraph newlines into spaces
        paragraph = doc.get_text()
        paragraph = doc.text
        paragraph = re.sub(r"\n+", "\n", paragraph)
        paragraph = paragraph.replace("\n", " ")
        # Tokenize the paragraph into words
        tokens = en_nlp.tokenizer(paragraph)
        words = [str(token) for token in tokens if not
                 str(token).isspace()]
        if len(words) < 3:
            continue
        all_paragraphs.append(words)
    # Return a list of strings, where each string is a
    # space-tokenized paragraph.
    return [" ".join(paragraph) for paragraph in all_paragraphs]
def flatten_one_gigaword_file_return_articles(file_path):
    # Parse the text with BeautifulSoup
    soup = BeautifulSoup(open(file_path), "html.parser")


    all_news_articles_flattened=[]

    # Iterate over all articles/docs items and get the text for each.
    for doc in soup("doc"):
        article = doc.get_text()

        # Turn inter-paragraph newlines into spaces
        article = re.sub(r"\n+", "\n", article)
        article = article.replace("\n", " ")
        # Tokenize the paragraph into words
        tokens = en_nlp.tokenizer(article)
        words = [str(token) for token in tokens if not
                 str(token).isspace()]
        if len(words) < 3:
            continue
        all_news_articles_flattened.append(" ".join(words))
    # Return a list of strings, where each string is a
    # space-tokenized article.
    return all_news_articles_flattened


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger(__name__)

    parser = ArgumentParser(description=("Flatten a gigaword data file for "
                                         "use in language modeling."))
    parser.add_argument("--gigaword-path", required=True,
                        metavar="<gigaword_path>", type=str,
                        help=("Path to Gigaword directory, with "
                              "all .gz files unzipped."))
    parser.add_argument("--output-dir", required=True, metavar="<output_dir>",
                        type=str, help=("Directory to write final flattened "
                                        "Gigaword file."))

    A = parser.parse_args()
    # all_paragraphs = flatten_one_gigaword_file(A.gigaword_path)
    all_articles_this_document = flatten_one_gigaword_file_return_articles(A.gigaword_path)
    for index,article in enumerate(all_articles_this_document):
        output_path = os.path.join(A.output_dir,
                               os.path.basename(A.gigaword_path))
        output_path = str(output_path) +"_"+ str(index+1)+ ".flat"
        with open(output_path, "w") as output_file:
            output_file.write("{}\n".format(article))

