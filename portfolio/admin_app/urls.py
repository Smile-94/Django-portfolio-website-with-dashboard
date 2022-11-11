from django.urls import path

from admin_app import views

app_name='admin_app'

urlpatterns = [
    path('admin/',views.AdminView.as_view(),name='admin'),
    path('message/<pk>/',views.MessageDetail.as_view(),name='message'),
    path('delete_message/<pk>/',views.DeleteMessage.as_view(),name='delete_message'),
    path('skills/',views.AddSkills.as_view(),name='skills'),
    path('update_skills/<pk>/',views.EditSkills.as_view(),name='edit_skills'),
    path('delete_skills/<pk>/',views.DeleteSkills.as_view(),name='delete_skills'),
    path('eduction/',views.AddEducation.as_view(),name='educations'),
    path('update_eduction/<pk>/',views.UpdateEducation.as_view(),name='update_education'),
    path('delete_education/<pk>/',views.DeleteEducation.as_view(),name='delete_education'),
    path('add_expriences/',views.AddExprience.as_view(),name='expriences'),
    path('update_expriences/',views.UpdateExprience.as_view(),name='update_exprience'),
    path('update_expriences/<pk>/',views.UpdateExprience.as_view(),name='update_exprience'),
    path('delete_expriences/<pk>/',views.DeleteExprience.as_view(),name='delete_exprience'),
    path('profile_info/',views.AddPersonalInfo.as_view(),name='profile'),
    path('update_profile/<pk>/',views.EditInfo.as_view(),name='edit_profile'),
]
