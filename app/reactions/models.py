from django.db import models
from common.models import CommonModel


# User: FK
# Video: FK
# reaction(like, dislike, cancel) => 실제 youtube rest api

# User : Reaction => 1:N(FK)
# Video : Reaction => 1:N(FK)

class Reaction(CommonModel):
    # user = models.ForeignKey(User) # Circular Import Error
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'DisLike'),
        (NO_REACTION, 'No Reaction'),
    )


    # LIKE(1), DISLIKE(-1), NO_REACTION(0)
    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION,
    )
