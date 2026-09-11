from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    total_copies=models.IntegerField()
    available_copies=models.IntegerField()


class Member(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()


class IssueRecord(models.Model):
    book=models.ForeignKey(Book ,on_delete=models.CASCADE)
    member=models.ForeignKey(Member , on_delete=models.CASCADE)
    issue_date=models.DateField()
    return_date=models.DateField(null=True,blank=True)
    returned=models.BooleanField(default=False)

