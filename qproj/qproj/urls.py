from django.conf.urls import patterns, include, url
from django.contrib import admin
from qproj.question.api import PostResource
from qproj.question.api import CommentResource

post_resource = PostResource()
comment_resource = CommentResource()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/v1/', include(post_resource.urls)),
    (r'^api/v1/', include(comment_resource.urls)),
)