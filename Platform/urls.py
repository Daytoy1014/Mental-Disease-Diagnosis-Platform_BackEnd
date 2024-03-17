from django.urls import path

from . import views

urlpatterns = [
    path('PublicRegister/', views.PublicRegister.as_view()),
    path('DoctorRegister/', views.DoctorRegister.as_view()),
    path('ResearcherRegister/', views.ResearcherRegister.as_view()),
    path('PublicLogin/', views.PublicLogin.as_view()),
    path('DoctorLogin/', views.DoctorLogin.as_view()),
    path('ResearcherLogin/', views.ResearcherLogin.as_view()),
    path('getPublicResume/', views.getPublicResume.as_view()),
    path('PublicSaveResume', views.publicSaveResume.as_view()),
    path('getPublicDiagnosisList/', views.getPublicDiagnosisList.as_view()),
    path('PublicEstablishDiagnosis/', views.publicEstablishDiagnosis.as_view()),
    path('PublicLaunchPredict/', views.publicLaunchPridict.as_view()),
    path('getPublicPredictList/', views.getPublicPredictList.as_view()),
    path('getPublicRecommendation/', views.getPublicRecmmendation.as_view()),
    path('getDatasetList/', views.getDatasetList.as_view()),
    path('uploadDataset/', views.uploadDataset.as_view()),
    path('DeleteDataset/', views.DeleteDataset.as_view()),
    path('getModelList/', views.getModelList.as_view()),
    path('getPatientList/', views.getPatientsList.as_view()),
    path('getPatientAssistantTask/', views.getPatientAssistantTask.as_view()),
    path('getBoardList/', views.getBoardsList.as_view()),
]
