import nltk
import string

operation = ["AND", "OR", "NOT"]
class Preprocessing:

    @staticmethod
    def Stemming(tokens):
        #  Stemming
        # nltk.download('punkt')
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()
        stemToken = []
        for token in tokens:
            if token not in operation:
                stemToken.append(stemmer.stem(token))
            else:
                stemToken.append(token)
        return stemToken
        # print(f"Stems {stemToken}")

    @staticmethod
    def Lemmatize(tokens):
        # Lemmatization
        # nltk.download('wordnet')
        # nltk.download('averaged_perceptron_tagger')
        from nltk.stem import WordNetLemmatizer
        from nltk.tag import pos_tag
        lemmatizer = WordNetLemmatizer()  # Create the Lemmatizer object
        lemToken = []

        for token, tag in pos_tag(tokens):
            if token not in operation:
                if tag.startswith("NN"):
                    lemToken.append(lemmatizer.lemmatize(token, pos="n"))
                elif tag.startswith("VB"):
                    lemToken.append(lemmatizer.lemmatize(token, pos="v"))
                elif tag.startswith("JJ"):
                    lemToken.append(lemmatizer.lemmatize(token, pos="a"))
            else:
                lemToken.append(token)

        return lemToken
        # print(f"Lems {lemToken}")

    @staticmethod
    def StopWord(tokens):
        # nltk.download('stopwords')
        from nltk.corpus import stopwords
        stop_words = set(stopwords.words('english'))
        new_tokens = []
        for token in tokens:
            if token not in stop_words or token in operation:
                new_tokens.append(token)
        return new_tokens
        # print(f"StopWords removal {new_tokens}")

    @staticmethod
    def tokenize(content=""):
        return [t for t in nltk.word_tokenize(content) if t not in string.punctuation]

    @staticmethod
    def normalization(text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        # print(text)
        return text
