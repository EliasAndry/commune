from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
# regex to filter valid phone numbers
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number format: '+999999999'")


class User(AbstractUser):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class Chore(models.Model):
    # Commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    assign = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)

    @staticmethod
    def get_chore_by_title(title):
        try:
            chore = Chore.objects.filter(title=title).order_by('date').first()
        except Chore.DoesNotExist:
            return None
        return chore
