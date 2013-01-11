from django.views.generic.base import TemplateView

class SummaryCardView(TemplateView):
    template_name = "summary.html"
    def get_context_data(self, **kwargs):
        context = super(SummaryCardView, self).get_context_data(**kwargs)
        return context


class PhotoCardView(TemplateView):
    template_name = "photo.html"
    def get_context_data(self, **kwargs):
        context = super(PhotoCardView, self).get_context_data(**kwargs)
        return context
