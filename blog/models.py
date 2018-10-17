from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(verbose_name='类别名称',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '类别名称'
        verbose_name_plural = '分类列表'

class Tag(models.Model):
    name = models.CharField(verbose_name='标签',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签名称'
        verbose_name_plural = '标签列表'

class Post(models.Model):
    title = models.CharField(verbose_name='标题',max_length=70)
    body = models.TextField(verbose_name='正文',blank=True,null=True)
    created_time = models.DateTimeField(verbose_name='创建时间',blank=True,null=True)
    modified_time = models.DateTimeField(verbose_name='修改时间',blank=True,null=True)
    excerpt = models.CharField(verbose_name='文章摘要',max_length=200,blank=True,null=True)
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE,blank=False,null=False)
    tags = models.ManyToManyField(Tag,verbose_name='标签集合',blank=True)
    author = models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = '文章列表'
        get_latest_by = 'created_time'

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])