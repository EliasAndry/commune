from django.db import models


class Vote(models.Model):
    user = models.ForeignKey('commune_app.User', on_delete=models.CASCADE)
    chore = models.ForeignKey('commune_app.Chore', on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    # creates a new vote while checking if the related Chore can be passed or not
    @staticmethod
    def create_new_vote(voting_user, voted_chore, vote_bool):
        user_vote = Vote(user=voting_user, chore=voted_chore, approve=vote_bool)
        user_vote.save()
        # temporarily compared the number of votes to 3 until we get a method in commune model
        # that returns the number of members in the commune
        if len(Vote.objects.filter(chore=voted_chore)) == 3:
            num_of_yes_votes = len(Vote.objects.filter(chore=voted_chore, approve=True))
            num_of_no_votes = len(Vote.objects.filter(chore=voted_chore, approve=False))
            if num_of_yes_votes > num_of_no_votes:
                voted_chore.passed = True
                voted_chore.save()
        return user_vote
