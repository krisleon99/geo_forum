# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from material.frontend import urls as frontend_urls

admin.autodiscover()

js_info_dict = {
    'packages': ('doc_forum',),
}

urlpatterns = [

                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       # url(r'^avatar/', include('avatar.urls')),

                       url(r'^$', include('doc_forum.manager.urls')),

                       url(r'^proposal/', include('doc_forum.proposal.urls')),

                       url(r'^manager/', include('doc_forum.manager.urls')),

                       url(r'^agreement/', include('doc_forum.agreement.urls')),

                       url(r'^agreementgesp/', include('doc_forum.agreementgesp.urls')),

                       url(r'^doctos/', include('doc_forum.doctos.urls')),

                       url(r'^institution/', include('doc_forum.institution.urls')),

                       url(r'^forum/', include('doc_forum.forum.urls')),

                       url(r'^event/', include('doc_forum.appointment.urls')),

                        url(r'^fmail/', include('doc_forum.fmail.urls')),

                       # Accounts
                       url(r'^accounts/', include('doc_forum.accounts.urls')),

                       url(r'', include(frontend_urls)),

                       ]

# Serve static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
