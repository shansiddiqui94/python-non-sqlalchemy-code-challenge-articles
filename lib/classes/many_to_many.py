import ipdb
# Many to Many structure cc
class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50 and not hasattr(self, "_title"):
            self._title = new_title
        else:
            print("Sorry, invalid title")

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            print("invalid Author")

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            print("invalid Magazine")
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, "_name"):
            self._name = new_name
        else:
            print("invalid name")

    def articles(self):
        article_list = []
        for article_obj in Article.all: #article_obj is an object, and Article.all has many objects in it
            # the for loop is checking for each object and passes each of them in article_obj
            # Article.all is referring to the list of all the object articles being stored in the (Article) class, in the list (all)
            if article_obj.author is self: # this line is accessing the value of the key author (.author)
                #it checks if the value of author matches this author which is self
                #(.author) key is referred to the author instance attribute that's initialized in the class of Article's constructor i.e init method
                article_list.append(article_obj) # this line adds whichever author that matches this author (self) to the list article_list
                #That's how this method keeps track of articles written by this author
        return article_list

    def magazines(self):
        mag_list = []
        for article_obj in Article.all:
            if article_obj.author is self:
                mag_list.append(article_obj.magazine)
        return list(set(mag_list)) 

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine):
            article = Article(self, magazine, title)
            return article
        else:
            print("invaalid magazine")


    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        topic_list = []
        for topic in self.magazines():
            topic_list.append(topic.category)
        return list(set(topic_list))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            print("Mags name is invalid, try again")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            print("invalid category")

    def articles(self):
        article_list = []
        for article_obj in Article.all:
            if article_obj.magazine is self and isinstance(article_obj, Article):
                article_list.append(article_obj)
        return article_list

    def contributors(self):
        author_list = []
        for author_obj in Article.all:
            if author_obj.magazine is self and isinstance(author_obj.author, Author):
                author_list.append(author_obj.author)
        return list(set(author_list))
        

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        title_list = []
        for mag_title in self.articles():
            title_list.append(mag_title.title)
        return title_list

    def contributing_authors(self):
        if len(self.articles()) <= 2:
            return None
        author_dictionary = {}
        for article in self.articles():
            if article.author in author_dictionary:
                author_dictionary[article.author] += 1
            else:
                author_dictionary[article.author] = 1

        contributor_list = []
        for author in author_dictionary:
            article_count = author_dictionary[author]
            if article_count > 2:
                contributor_list.append(author)
        return contributor_list