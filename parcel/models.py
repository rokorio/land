from django.db import models

# Create your models here.
class ParcelDetail(models.Model):
    reg_no=models.CharField(max_length=10)

class UserDetail(models.Model):
    pass

class Payments(models.Model):
    pass
class planingApplication(models.Model):
    pass


class Green_card(models.Model):
    pass

class Owner(models.Model):
    pass

class LandCaution(models.Model):
    pass