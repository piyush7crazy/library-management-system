from django.urls import path
from . import views

urlpatterns=[
    path('api/create_book/',views.create_book_api,name="create_book_api"),
    path('api/list_book/',views.list_book_api,name="list_book_api"),
    path('api/detail_book/<int:id>/',views.detail_book_api,name="detail_book_api"),
    path('api/update_book/<int:id>/',views.update_book_api,name="update_book_api"),
    path('api/delete_book/<int:id>/',views.delete_book_api,name="delete_book_api"),

    path('api/create_member/',views.create_member_api,name="create_member_api"),
    path('api/list_member/',views.list_member_api,name="list_member_api"),
    path('api/detail_member/<int:id>/',views.detail_member_api,name="detail_member_api"),
    path('api/update_member/<int:id>/',views.update_member_api,name="update_member_api"),
    path('api/delete_member/<int:id>/',views.delete_member_api,name="delete_member_api"),

    path('api/create_issuerecord/',views.create_issuerecord_api,name="create_issuerecord_api"),
    path('api/list_issuerecord/',views.list_issuerecord_api,name="list_issuerecord_api"),
    path('api/detail_issuerecord/<int:id>/',views.detail_issuerecord_api,name="detail_issuerecord_api"),
    path('api/update_issuerecord/<int:id>/',views.update_issuerecord_api,name="update_issuerecord_api"),
    path('api/delete_issuerecord/<int:id>/',views.delete_issuerecord_api,name="delete_issuerecord_api"),
]
