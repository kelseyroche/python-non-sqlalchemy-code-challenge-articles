class Article:
    all = []

    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self.author = author
        else:
            print("Author must be of type Author")
        if isinstance(magazine, Magazine):
            self.magazine = magazine
        else:
            print("Magazine must be of type magazine")
        if isinstance(title, str) and (5 <= len(title) <= 50):
            self._title = title
        else:
            print("Title must be a string between 5 and 50 characters")
        
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title (self, title):
        if isinstance(title, str) and (5<=len(title) <= 50):
            self._title = title
        else:
            print("Title must be a string between 5 and 50 characters")
        
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name=name
        else:
            print("Name must be a string longer than 0 characters")

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles())) 

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set(magazine.category for magazine in self.magazines()))
        return categories if categories else None

class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str) and (2<= len(name) <= 16):
            self._name = name
        else:
            print("Name must be a string between 2 and 16 characters")
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            print("Category must me a string longer than 0 characters")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (2<= len(name) <= 16):
            self._name = name
        else:
            print("Name must be a string between 2 and 16 characters")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            print("Category must me a string longer than 0 characters")

    def articles(self):
        return [article for article in Article.all if article.magazine ==self]

    def contributors(self):
        return list (set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}

        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] +=1
            else:
                author_counts[author] =1

        result = [author for author, count in author_counts.items() if count >2]
        return result if result else None
    