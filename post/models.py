from django.db import models

from user.models import User


class Post(models.Model):
    uid = models.IntegerField()
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    @property
    def auth(self):
        if not hasattr(self, '_auth'):
            self._auth = User.objects.get(id=self.uid)
        return self._auth

    def comments(self):
        return Comment.objects.filter(post_id=self.id).order_by('-id')

    def tags(self):
        '''TODO'''
        pass

    def update_tags(self, tag_names):
        '''TODO'''
        pass


class Comment(models.Model):
    uid = models.IntegerField()
    post_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    @property
    def auth(self):
        if not hasattr(self, '_auth'):
            self._auth = User.objects.get(id=self.uid)
        return self._auth

    @property
    def post(self):
        if not hasattr(self, '_post'):
            self._post = Post.objects.get(id=self.post_id)
        return self._post


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)


class PostTagRelation(models.Model):
    '''
    Post 与 Tag 的关系表

        Django部署   django
        Django部署   python
        Django部署   linux
        Linux对比    linux
        Linux对比    python
        nginx       django
        nginx       linux
    '''
    post_id = models.IntegerField()
    tag_id = models.IntegerField()
