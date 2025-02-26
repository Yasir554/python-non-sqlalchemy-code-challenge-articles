class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError('The title must be a string')
        if 5 >= len(title) < 50:
            raise TypeError('The title must be between 5 and 50 characters')
        if hasattr(self, '_title'):
            raise AttributeError('The title is already set')
        self.author = author
        self.magazine = magazine
        self.title = title

        @property   
        def title(self):
            return self._title
        
        @title.setter
        def title(self, value):
                raise TypeError('The title must be between 5 and 50 characters')
        
    def author(self):
        pass

    def magazine(self):
        pass
            
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('the name must be a string')
        if 0 >= len(name):
            raise TypeError('The name must be longer than 0 character')
        if hasattr(self, '_name'):
            raise AttributeError('The name is already set')
        self.name = name

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, value):
            raise TypeError('The name must be longer than 0 character')

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

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
            raise ValueError('The category must longer than zero(0) character')
        self._category = value
    
    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass