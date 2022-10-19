from django.urls import path
from django.conf.urls import url 
from backend import views

app_name = 'backend'

urlpatterns =[
        path('login/', views.login_view, name='login_view'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('logout_view/', views.logout_view, name='logout_view'),
        path('add_blog/', views.add_blog, name='add_blog'),
        path('blog/', views.blog, name='blog'),
        path('view_blog/<int:view_id>', views.view_blog, name='view_blog'),
        path('blog/<int:post_id>', views.edit_blog, name='edit_blog'),
        path('services/', views.services, name='services'),
        path('add_services/', views.add_services, name='add_services'),
        path('services/<int:post_id>', views.edit_services, name='edit_services'),
        path('view_services/<int:view_id>', views.view_services, name='view_services'), 
        path('delete-blog/<int:delete_id>', views.delete_blog, name='delete_blog'),
        path('delete-services/<int:delete_id>', views.delete_services, name='delete_services'),
        path('team/', views.team, name='team'),
        path('add_team/', views.add_team, name='add_team'),
        path('team/<int:team_id>', views.edit_team, name='edit_team'),
        path('view_team/<int:view_id>', views.view_team, name='view_team'),
        path('delete-team/<int:delete_id>', views.delete_team, name='delete_team'),
        path('newsletter/', views.newsletter, name='newsletter'),
        path('change_password/', views.change_password, name='change_password'),
        path('password_reset/', views.password_reset_request, name='password_reset_request'),
    
]