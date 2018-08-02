from django.db import models


class User(models.Model):
    SEX = (
        ('M', '男性'),
        ('F', '女性'),
        ('U', '保密'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)
    icon = models.ImageField()
    plt_icon = models.CharField(max_length=256, default='')
    age = models.IntegerField(default=18)
    sex = models.CharField(max_length=8, choices=SEX)

    @property
    def avatar(self):
        if self.icon:
            return self.icon.url
        else:
            return self.plt_icon

    def has_perm(self, perm_name):
        pass


class UserRoleRelation(models.Model):
    uid = models.IntegerField()
    role_id = models.IntegerField()

    @classmethod
    def add_role_to_user(cls, uid, role_id):
        pass

    @classmethod
    def del_role_from_user(cls, uid, role_id):
        pass


class Role(models.Model):
    '''
    角色表
        admin   管理员
        manager 版主
        user    普通用户
    '''
    name = models.CharField(max_length=16, unique=True)


class RolePermRelation(models.Model):
    role_id = models.IntegerField()
    perm_id = models.IntegerField()

    @classmethod
    def add_perm_to_role(cls, role_id, perm_id):
        pass

    @classmethod
    def del_perm_from_role(cls, role_id, perm_id):
        pass

class Permission(models.Model):
    '''
    权限表
        add_post    添加帖子权限
        del_post    删除帖子权限
        add_comment 添加评论权限
        del_comment 删除评论权限
        del_user    删除用户权限
    '''
    name = models.CharField(max_length=16, unique=True)
