import pandas as pd

from simsity.service import Service
from simsity.indexer import PyNNDescentIndexer
from simsity.preprocessing import ColumnLister
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv("tests/data/clinc-data.csv").head(100)


encoder = make_pipeline(ColumnLister(column="text"), CountVectorizer())


service = Service(indexer=PyNNDescentIndexer(metric="euclidean"), encoder=encoder)

service.train_from_dataf(df, features=["text"])
service.query(text="where is my phone", n_neighbors=3, out="dataframe")
