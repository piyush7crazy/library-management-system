from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book , Member , IssueRecord
from .serializer import BookSerializer , MemberSerializer , IssueRecordSerializer

@api_view(['POST'])
def create_book_api(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def list_book_api(request):
    books=Book.objects.all()
    serializer=BookSerializer(books, many=True)
    return Response(serializer.data , status=200)
  

@api_view(['GET'])
def detail_book_api(request,id):
    books=Book.objects.get(id=id)
    serializer=BookSerializer(books)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_book_api(request,id):
    books=Book.objects.get(id=id)
    serializer=BookSerializer(books , data=request.data , partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors ,status=400)


@api_view(['DELETE'])
def delete_book_api(request,id):
    books=Book.objects.get(id=id)
    books.delete()
    return Response(status=204)



@api_view(['POST'])
def create_member_api(request):
    serializer=MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.errors , status=400)


@api_view(['GET'])
def list_member_api(request):
    members=Member.objects.all()
    serializer=MemberSerializer(members,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail_member_api(request,id):
    members=Member.objects.get(id=id)
    serializer=MemberSerializer(members)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_member_api(request,id):
    members=Member.objects.get(id=id)
    serializer=MemberSerializer(members , data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200)
    return Response(serializer.errors,status=400)


@api_view(['DELETE'])
def delete_member_api(request,id):
    members=Member.objects.get(id=id)
    members.delete()
    return Response(status=204)



@api_view(['POST'])
def create_issuerecord_api(request):
    serializer=IssueRecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=400)


@api_view(['GET'])
def list_issuerecord_api(request):
    issue=IssueRecord.objects.all()
    serializer=IssueRecordSerializer(issue , many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def detail_issuerecord_api(request,id):
    issue=IssueRecord.objects.get(id=id)
    serializer=IssueRecordSerializer(issue)
    return Response(serializer.data,status=200)


@api_view(['PATCH'])
def update_issuerecord_api(request,id):
    issue=IssueRecord.objects.get(id=id)
    serializer=IssueRecordSerializer(issue,data=request.data , partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors,status=400)


@api_view(['DELETE'])
def delete_issuerecord_api(request,id):
    issue=IssueRecord.objects.get(id=id)
    issue.delete()
    return Response(status=204)