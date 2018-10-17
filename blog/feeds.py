from django.contrib.syndication.views import Feed
from .models import Post

class AllPostsRssFeed(Feed):
    title = "无此人的博客"
    link = "/"
    description = "无此人的博客文章"

    def items(self):
        return Post.objects.all()

    def item_title(self,item):
        return '[%s] %s' % (item.category,item.title)

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return '127.0.0.1:8000/all/rss/'+str(item.id)+'/'