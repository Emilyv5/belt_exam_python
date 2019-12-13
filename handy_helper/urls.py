from django.urls import path
from . import views
import login_registration

urlpatterns = [
    path('dashboard', views.dashboard),
    path('jobs/new', views.jobs_new),
    path('jobs/edit/<num>', views.edit_id),
    path('jobs/<num>', views.edit),
    path('edit/<num>', views.edition),
    path('add/<num>', views.add),
    path('giveup/<num>', views.giveup),

    path('addtomyjob/<num>', views.jobadd),
    path('jobgiveup/<num>', views.jobgiveup),
    path('delete/<num>', views.delete),
    path('addjob', views.add_job),
    path('logout', views.logout),
    path('cancel', views.cancel),

    # path('success', views.success),
]