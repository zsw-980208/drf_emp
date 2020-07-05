from django.db import models
class User(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
    )

    username = models.CharField(max_length=80)
    real_name = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    status = models.SmallIntegerField(default=False)
    register_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bz_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Employee(models.Model):
    emp_name = models.CharField(max_length=80)
    img = models.ImageField(upload_to="pic", default="pic/1.jpg")
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.IntegerField()

    @property
    def cate_age(self):
        if self.age <30:
            return "青年"
        elif 30<=self.age<=50:
            return "中年"
        elif self.age>50:
            return "老年"

    class Meta:
        db_table = "bz_employee"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_name