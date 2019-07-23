from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):     # 使用__str__方法帮助人性化显示对象信息   用到这个方法类设置返回的参数。 参数要加入self
        return self.name   # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

    class Meta:    # 首先class Meta做为嵌套类，主要目的是给上级类添加一些功能，或者指定一些标准。
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"