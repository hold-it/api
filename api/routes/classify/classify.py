from model.model import classifyInput
from newspaper import Article


url = "https://en.wikipedia.org/wiki/Jimmy_Neutron"
article = Article(url)
article.download()
article.parse()
classifyInput(article.text)