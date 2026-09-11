from rest_framework import serializers
from .models import Book , Member , IssueRecord

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['title' , 'author' , 'total_copies' , 'available_copies' , 'id']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields=['name' , 'email' , 'id']

class IssueRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=IssueRecord
        fields=['book' , 'member' , 'issue_date' , 'return_date' , 'returned', 'id']