""" 向量化 """
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

if __name__ == '__main__':
    with open("segments.pickle", "rb") as f:
        segments = pickle.load(f)

    vectorizer = TfidfVectorizer()
    contents = segments.values()

    # 转换模型
    model = vectorizer.fit(contents)
    print(len(model.vocabulary_))

    # 转化向量
    X = vectorizer.transform(contents)
    with open("dataset.pickle", "wb") as f:
        print("saving dataset.....")
        pickle.dump(X, f)

    # 保存模型
    with open("vectorizer.pickle", "wb") as f:
        print("saving vectorizer model.....")
        pickle.dump(model, f, protocol=4)
