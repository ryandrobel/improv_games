from django.db import models
from login.models import User

class GameManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['game_name']) < 3 or len(post_data['game_name']) > 25:
            errors['game_name'] = "Game name has to be between 3 and 25 characters!"
        
        if len(post_data['number_of_players']) < 1 or len(post_data['number_of_players']) > 100:
            errors['number_of_players'] = "Number of players name has to be between 1 and 100 characters!"

        if len(post_data['instructions']) < 3 or len(post_data['instructions']) > 500:
            errors['instructions'] = "instructions have to be between 3 and 500 characters!"

        return errors


class Game(models.Model):
    game_name = models.TextField()
    number_of_players = models.TextField()
    instructions = models.TextField()
    creator = models.ForeignKey(User, related_name = 'games', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = GameManager()

class ReviewManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['comment']) < 10 or len(post_data['comment']) > 150:
            errors['comment'] = "Comment has to be between 10 and 150 characters!"
        
        if len(post_data['rating']) < 1 or len(post_data['rating']) > 5:
            errors['rating'] = "Rating should be on a scale of 1 to 5!"

        return errors

class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    user_review = models.ManyToManyField(User, related_name = 'reviews')
    user_comment = models.ManyToManyField(User, related_name = 'comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()

