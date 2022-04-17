
import pandas as pd
import re, string, nltk, pickle
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from keras.preprocessing import text,sequence
max_features = 10000
maxlen = 300

def classify(texts):
    d = {'text': [texts]}
    nltk.download('stopwords')
    stop = set(stopwords.words('english'))
    punctuation = list(string.punctuation)
    stop.update(punctuation)
    testing_data = pd.DataFrame(data = d)
    def strip_html(text):
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()

    #Removing the square brackets
    def remove_between_square_brackets(text):
        return re.sub('\[[^]]*\]', '', text)
    # Removing URL's
    def remove_between_square_brackets(text):
        return re.sub(r'http\S+', '', text)
    #Removing the stopwords from text
    def remove_stopwords(text):
        final_text = []
        for i in text.split():
            if i.strip().lower() not in stop:
                final_text.append(i.strip())
        return " ".join(final_text)
    #Removing the noisy text
    def denoise_text(text):
        text = strip_html(text)
        text = remove_between_square_brackets(text)
        text = remove_stopwords(text)
        return text
    #Apply function on review column
    testing_data['text']=testing_data['text'].apply(denoise_text)
    #transform the data
    tokenizer = text.Tokenizer(num_words=max_features)
    tokenized_test = tokenizer.texts_to_sequences(testing_data['text'])
    test_model = sequence.pad_sequences(tokenized_test, maxlen=maxlen)
    # load the model and predict
    loaded_model = pickle.load(open('Best_Model','rb'))
    result = loaded_model.predict(test_model)
    return result