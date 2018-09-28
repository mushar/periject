from django.db import models

# Create your models here.


class ContactDetails(models.Model):
    project_manager = models.CharField(max_length=200)

class Department(models.Model):
    Information_Technology = 'IT'
    Finance = 'FR'
    Human_Resources = 'HR'
    Membership = 'MR'
    Consultancy = 'CS'
    Marketing = 'MK'
    DEPARTMENT_CHOICES = (
    (Information_Technology, 'IT'),
    (Finance, 'Finance'),
    (Human_Resources, 'HR'),
    (Membership, 'Membership'),
    (Consultancy, 'Conultancy'),
    (Marketing, 'Marketing'),
    )
    chosen_department = models.CharField(max_length=2,
                                      choices=DEPARTMENT_CHOICES,
                                      default=Information_Technology)

       ##def is_upperclass(self):
       ## return self.chosen_department in (self.JUNIOR, self.SENIOR)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)