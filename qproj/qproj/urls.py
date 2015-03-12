from django.conf.urls import patterns, include, url
from django.contrib import admin

from qproj.question.api import QuestionResource

question_resource = QuestionResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/v1/', include(question_resource.urls)),
)
