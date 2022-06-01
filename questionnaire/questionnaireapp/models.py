from django.db import models

# Create your models here.
class Explanationlist(models.Model):
    explnataion = models.ForeignKey('Explanations', models.DO_NOTHING)
    list = models.ForeignKey('List', models.DO_NOTHING)
    rank = models.IntegerField()

    class Meta:
        db_table = 'explanationList'
        unique_together = (('explnataion', 'list'),)


class Explanationusers(models.Model):
    explanation = models.ForeignKey('Explanations', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    answer_id = models.IntegerField()

    class Meta:
        db_table = 'explanationUsers'


class Explanations(models.Model):
    text = models.TextField()
    tweet_id = models.CharField(max_length=200)

    class Meta:
        db_table = 'explanations'
        unique_together = (('id', 'text'),)
    def __str__(self) -> str:
        return self.tweet_id

class List(models.Model):
    list_id = models.CharField(unique=True, max_length=200)
    list_name = models.TextField(unique=True)

    class Meta:
        db_table = 'list'


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'users'