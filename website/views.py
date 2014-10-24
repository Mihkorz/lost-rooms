# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView

class IndexPage(TemplateView):
    template_name = 'website/index.html'
    
    
    def dispatch(self, request, *args, **kwargs):
        return super(IndexPage, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
              
        context = super(IndexPage, self).get_context_data(**kwargs)
        
        
        context['test'] = "TEst"
        
        return context