from django.db import models
status_choice = [("active", "Активно"), ("blocked", "Заблокировано")]
# Create your models here.


class Guestbook(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    text = models.TextField(max_length=1000, null=False, blank=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    status = models.CharField(max_length=30, choices=status_choice, null=False, default="active")

    class Meta:
        db_table = "guests"
        verbose_name = "Гость"
        verbose_name_plural = "Гости"


    def __str__(self):
        return f'{self.id}. {self.name}. {self.text}. {self.status}: {self.create_time} {self.update_time}'
