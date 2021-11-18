from core.log import MyLogger
import json
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re

paths = json.load(open('config/paths.json', 'r'))
config = json.load(open('config/config.json', 'r'))
log_path = paths["log_path"].format(filename=__file__.split('/')[-1])
logger = MyLogger(log_path)


def read_test_amazon(path = "/home/lenovo_e14/Documents/Datasets/amazon_review_polarity_csv/test.csv" ):
    data = pd.read_csv(path)
    data.columns = ["label", "title", "text"]
    return data


def read_dataset_amazon(path="/home/lenovo_e14/Documents/Datasets/amazon_review_polarity_csv/train.csv"):
    if config["mode"] == "test":
        nRows = 10000
    else:
        nRows = None

    logger.info(f"Reading the File {path} with nRows : {nRows}")
    data = pd.read_csv(path, nrows=nRows)
    data.columns = ["label", "title", "text"]
    if config["mode"] != "test":
        test = read_test_amazon()
        data = pd.concat([data, test], ignore_index=True)
    return data


def data_cleaning_amazon(data, column="text"):
    stop_words = stopwords.words("english")
    stemmer = SnowballStemmer("english")
    TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

    def preprocess(text, stem=False, stop_w=False):
        # Remove link,user and special characters
        text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower()).strip()
        if stop_w:
            tokens = []
            for token in text.split():
                if token not in stop_words:
                    if stem:
                        tokens.append(stemmer.stem(token))
                    else:
                        tokens.append(token)
            return " ".join(tokens)
        else:
            return text

    data[column] = data[column].apply(lambda x: preprocess(x))
    return data


