POSTS = [
    {'id': 1, 'title': 'My First Blog Post', 'content': 'This is the content of my first blog post.'},
    {'id': 2, 'title': 'Another Blog Post', 'content': 'This is another content of blog post.'},
]

from posts.models import Item

POSTS = Item.objects.all()