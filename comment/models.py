from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(verbose_name='名字',max_length=100)
    email = models.EmailField(verbose_name='邮箱',max_length=255)
    url = models.URLField(verbose_name='个人网站',blank=True)
    text = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(verbose_name='评论时间',auto_now_add=True)

    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)

    def __str__(self):
        return  self.text[:20]

    class Meta:
        ordering = ['-created_time']
        verbose_name = '评论'
        verbose_name_plural = '评论列表'
        get_latest_by = 'created_time'