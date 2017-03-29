from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(unique=False, max_length=255)
    player1 = models.CharField(unique=False, max_length=255)
    player2 = models.CharField(unique=False, max_length=255)
    players = models.IntegerField(unique=False)
    gamestate = models.CharField(unique=False, max_length=1000)
    turn = models.CharField(unique=False, max_length=1)
    leaver = models.BooleanField(unique=False, default=False)
    winner = models.CharField(unique=False, max_length=1, default="")
    draw = models.BooleanField(unique=False, default=False)

    def __unicode__(self):
        return u'%s: %s' % (self.id, self.name)

    class Meta:
        db_table = u'games'

