import datetime
import random

from zoulalablog.models import db, User, Tag, Post

user = db.session.query(User).filter_by(id=3).first()
tag_one = Tag('Flask')
tag_two = Tag('Python')
tag_three = Tag('js')
tag_four = Tag('html')
tag_list = [tag_one, tag_two, tag_three, tag_four]

s = "EXAMPLE TEXT,aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

for i in xrange(100):
    new_post = Post("my_post_" + str(i))
    new_post.users = user
    new_post.publish_date = datetime.datetime.now()
    new_post.text = s
    new_post.tags = random.sample(tag_list, random.randint(1, 3))
    db.session.add(new_post)

db.session.commit()