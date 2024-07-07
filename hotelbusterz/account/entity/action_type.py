from django.db import models


class ActionType(models.TextChoices):
    LOGIN = 'LOGIN'
    VIEW_HOME = 'VIEW_HOME'
    VIEW_BOARD_LIST = 'VIEW_BOARD_LIST'
    VIEW_FAVORITE_READ = 'VIEW_FAVORITE_READ'
    VIEW_PRODUCT_LIST = 'VIEW_PRODUCT_LIST'
    BUTTON_BOOKNOW = 'BUTTON_BOOKNOW'
    BUTTON_REFERRAL = 'BUTTON_REFERRAL'