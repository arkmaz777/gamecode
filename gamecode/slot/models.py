from django.db import models
from django.contrib.auth.models import User

class Result(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_auth_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='id_auth_user',
        related_name='results'
    )
    reels_combination = models.JSONField()
    game_result = models.PositiveSmallIntegerField()


