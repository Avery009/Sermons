from django.urls import path

from . import views

urlpatterns = [
	path('',views.sermons, name='sermons'),
	path('enter/',views.entersermon, name='enter_sermon'),
	path('view/<int:sermon_id>', views.viewsermon, name='view_sermon'),
	path('edit/<int:sermon_id>', views.editsermon, name='edit_sermon'),
	path('remove/<int:sermon_id>', views.givethanks, name='remove_sermon'),
]
