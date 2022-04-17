import pandas as pd
import os, re, string, nltk, pickle
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from keras.preprocessing import text,sequence
import tensorflow as tf
max_features = 10000
maxlen = 300

def classifyInput(texts):
    d = {'text': [texts]}
    nltk.download('stopwords')
    stop = set(stopwords.words('english'))
    punctuation = list(string.punctuation)
    stop.update(punctuation)
    testing_data = pd.DataFrame(data = d)
    testing_data = pd.DataFrame(data = d)

    def clean(text):
        soup = BeautifulSoup(text, "html.parser")
        text = soup.get_text()
        text = re.sub('\[[^]]*\]', '', text)
        text = re.sub(r'http\S+', '', text)
        final_text = []
        for i in text.split():
            if i.strip().lower() not in stop:
                final_text.append(i.strip())
        return " ".join(final_text)
    #Apply function on review column
    testing_data['text']=testing_data['text'].apply(clean)
    tokenizer = text.Tokenizer(num_words = max_features)
    tokenized_test = tokenizer.texts_to_sequences(testing_data['text'])
    test_model = sequence.pad_sequences(tokenized_test, maxlen=maxlen)
    # load the model and predict'
    loaded_model = pickle.load(open(os.path.join(os.getcwd(),"./api/api/routes/classif/model/Best_model.pkl"),'rb'))
    result = loaded_model.predict(test_model)
    return result