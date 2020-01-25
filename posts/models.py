from django.db import models


class Post(models.Model):
    id = models.IntegerField('ID', primary_key=True)
    title = models.CharField('Title', max_length=1024, db_index=True)
    url = models.URLField('Link', max_length=512, db_index=True)
    created = models.DateTimeField('Created at', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Post [{self.id}, `{self.title}`]"

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
