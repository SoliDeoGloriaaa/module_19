from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=14)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=25)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')


# Запросы:

# Buyer.objects.create(name='Artur', balance='1200', age=20)
# Buyer.objects.create(name='Alina', balance='12300', age=21)
# Buyer.objects.create(name='Maxim', balance='3200', age=17)

# Game.objects.create(title='Pay Day 2', cost=2100, size=5, description='Первая игра', age_limited=True) 
# Game.objects.create(title='PUBG', cost=1100, size=2, description='Вторая игра', age_limited=True)
# Game.objects.create(title='CS2', cost=7400, size=6, description='Третья игра', age_limited=False)

# Game.objects.get(id=1).buyer.set((Buyer.objects.get(id=1), Buyer.objects.get(id=2)))
# Game.objects.get(id=2).buyer.set((Buyer.objects.get(id=1), Buyer.objects.get(id=2), Buyer.objects.get(id=3)))
# Game.objects.get(id=3).buyer.set((Buyer.objects.get(id=1), Buyer.objects.get(id=3)))