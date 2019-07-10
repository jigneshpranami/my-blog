from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.opinion_list,name='opinion_list'),
    path('opinion/<int:pk>/',views.opinion_detail,name='opinion_detail'),
    path('opinion/new/',views.opinion_new,name='opinion_new'),
    path('opinion/<int:pk>/edit/', views.opinion_edit, name='opinion_edit'),
    path('drafts/', views.opinion_draft_list, name='opinion_draft_list'),
    path('opinion/<pk>/publish/', views.opinion_publish, name='opinion_publish'),
    path('opinion/<pk>/remove/', views.opinion_remove, name='opinion_remove'),
    path('opinion/<int:pk>/comment/', views.add_comment_to_opinion, name='add_comment_to_opinion'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]