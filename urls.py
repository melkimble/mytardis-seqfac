import django
from django.conf import settings
from django.conf.urls import url
from .views import view_fastqc_html_report
from .custom_api import get_version_json, trash_experiment, \
    _delete_all_trashed, stats_ingestion_timeline

# urlpatterns = patterns('')

urlpatterns = [
    # url(r'^results/(?P<path>.*)$', 'django.views.static.serve', {
    #     'document_root': settings.WEBCACHE_FILE_PATH,
    # }),

    # url(r'^results/(?P<dataset_id>\d+)/(?P<filename>.*)$',
    #     'sequencing_facility.views.view_html_result_file'),

    url(r'^report/(?P<dataset_id>\d+)/(?P<filename>.*)$',view_fastqc_html_report,
        name='tardis.apps.sequencing_facility.views.view_fastqc_html_report'),

    # custom (non-tastypie) API endpoints
    url(r'^api/version$',get_version_json,
        name='tardis.apps.sequencing_facility.custom_api.get_version_json'),

    url(r'^api/trash_experiment/(?P<experiment_id>\d+)$',trash_experiment,
        name='tardis.apps.sequencing_facility.custom_api.trash_experiment'),

    url(r'^api/_delete_all_trashed/$',_delete_all_trashed,
        name='tardis.apps.sequencing_facility.custom_api._delete_all_trashed'),

    url(r'^api/_stats/$',stats_ingestion_timeline,
        name='tardis.apps.sequencing_facility.custom_api.stats_ingestion_timeline'),
]
