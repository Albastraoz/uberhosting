from django.db import models

# Packages model
class Package(models.Model):
    name = models.CharField(max_length=50, default='Package name')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    domains = models.IntegerField(default=1)
    mail_space = models.IntegerField(default=0)
    mail_address = models.IntegerField(default=0)
    hosting_space = models.IntegerField(default=0)
    hosting_databases = models.IntegerField(default=0)
    apps = models.BooleanField(default=False)
    highlight = models.BooleanField(default=False)
    sftp = models.IntegerField(default=0)

    def __str__(self):
        return self.name