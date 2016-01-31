from django.db import models

# Create your models here.
class Message(models.Model):
	text = models.CharField(unique=True, max_length=255)

	def __unicode__(self):
		return u'%s: %s' % (self.id, self.text)

	class Meta:
		db_table = u'messages'