from django.db import models

Employment_CHOICES = (
    ("Complete", "Complete"),
    ("Partial", "Partial"),
    ("Internship", "Internship"),
)


class Post(models.Model):
    image = models.ImageField()
    Job_title = models.CharField(max_length=100)
    Specialization = models.CharField(max_length=100)
    Employment_type = models.CharField(max_length=100, choices=Employment_CHOICES)
    Salary = models.PositiveIntegerField(default=0)
    Requirement = models.TextField()
    Description = models.TextField()


    def __str__(self):
        return self.Job_title