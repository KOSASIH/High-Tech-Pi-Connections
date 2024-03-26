# Loading and cleaning datasets sample
df = pd.read_csv("path/to/dataset.csv")
df = df.dropna()
df.drop_duplicates(inplace=True)
df = preprocess_data(df)
