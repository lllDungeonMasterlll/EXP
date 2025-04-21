from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Block(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    block_number = models.BigIntegerField()
    created_at = models.DateTimeField(null=True, blank=True)
    stored_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('currency', 'block_number')
