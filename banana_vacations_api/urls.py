from django.urls import path, include

from rest_framework.routers import DefaultRouter

from banana_vacations_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet),
router.register('planner-notes', views.PlannerNotesApiViewSet),
router.register('diary', views.DiaryApiViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]