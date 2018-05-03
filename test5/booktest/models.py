from django.db import models

# Create your models here.
class AreaInfo(models.Model):
    atitle=models.CharField('地区名称', max_length=30)  # 名称
    aParent=models.ForeignKey('self',null=True,blank=True)   # 关系

    def __str__(self):
        return self.atitle

    def parent(self):
        return self.aParent
    parent.admin_order_field = 'atitle'
    parent.short_description = '上级地区'


# 定义图片的模型类
class PicTest(models.Model):
    pic = models.ImageField(upload_to='booktest/')


