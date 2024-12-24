# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import path 

from .views import FormSubmission

urlpatterns = [
    path('forms/submit/', FormSubmission.as_view(), name='djangocms_forms_submissions'),
]
