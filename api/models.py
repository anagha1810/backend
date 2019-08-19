from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


class course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


    def no_of_ratings(self):
        ratings = rating.objects.filter(Course=self)
        return len(ratings)

    def avg_ratings(self):
        sum = 0
        ratings = rating.objects.filter(Course=self)
        for rate in ratings :
            sum += rate.stars

        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0


class rating(models.Model):
    Course = models.ForeignKey(course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'Course'),)
        index_together = (('user', 'Course'),)