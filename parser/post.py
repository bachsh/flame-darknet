from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    topic_content = Column(String)
    post_content = Column(String)
    post_author = Column(String)
    url = Column(String)
    flag = Column(Integer, default=-1)
    def __repr__(self):
        return "<Post(topic_content='%s', post_content='%s', post_author='%s', url='%s')>" % (self.topic_content, self.post_content, self.post_author, self.url)

