from django.db import models
from django.forms import ModelForm


class Leagues(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leagues'


class Pokedex(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pokedex'

    def __str__(self):
        return f'{self.num}: {self.name}'


class PokedexForm(ModelForm):
    class Meta:
        model = Pokedex
        fields = ['num', 'name']


class Rankings(models.Model):
    id = models.IntegerField(primary_key=True)
    position = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    league = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='league', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rankings'

    def __str__(self):
        return self.name

