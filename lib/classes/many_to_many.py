class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError('The title must be a string')
        if not (5 <= len(title) <= 50):
            raise ValueError('The title must be between 5 and 50 characters')
        if not isinstance(author, Author):
            raise TypeError('The author must be an instance of Author')
        if not isinstance(magazine, Magazine):
            raise TypeError('The magazine must be an instance of Magazine')
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property   
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError('The title cannot be changed after instantiation')
        self._title = value
        
    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, new_value_author):
        if isinstance(new_value_author, Author):
            self._author = new_value_author
        else:
            raise TypeError('The author must be an instance of Author')

    @property
    def magazine(self):
        return self._magazine
        
    @magazine.setter
    def magazine(self, new_value_magazine):
        if isinstance(new_value_magazine, Magazine):
            self._magazine = new_value_magazine
        else:
            raise TypeError('The magazine must be an instance of Magazine')
            
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('the name must be a string')
        if 0 == len(name):
            raise ValueError('The name must be longer than 0 character')
        
        self._name = name

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'): 
            raise AttributeError('The name cannot be changed after instantiation')
        self._name = value

    def articles(self,):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        return topic_areas if topic_areas else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name 
    @name.setter
    def name (self, value ):
        if not isinstance(value, str):
            raise TypeError('The name must be a string')
        if not (2 <= len(value) <= 16):
            raise ValueError('The name must be between 2 and 16 characters')
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError('The category must be a string')
        if len(value) == 0:
            raise ValueError('The category must be longer than 0 characters')
        self._category = value
    
    def articles(self):
       return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        freq = {}
        for article in self.articles():
            author = article.author
            freq[author] = freq.get(author, 0) + 1
        # Select authors who have more than 2 articles.
        authors = [author for author, count in freq.items() if count > 2]
        return authors if authors else None