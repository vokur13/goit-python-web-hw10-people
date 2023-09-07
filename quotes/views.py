from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Quote, Author, Tag


class QuotesListView(ListView):
    model = Quote
    template_name = "home.html"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"


class TagDetailView(DetailView):
    model = Tag
    template_name = "tag_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quote_list"] = Quote.objects.filter(tags__tag__contains=self.object)
        return context


class QuoteCreateView(CreateView):
    model = Quote
    template_name = "quote_new.html"
    fields = ["tags", "author", "quote"]
    success_url = "/"


class TagCreateView(CreateView):
    model = Tag
    template_name = "tag_new.html"
    fields = [
        "tag",
    ]
    success_url = "/quote/new/"


class AuthorCreateView(CreateView):
    model = Author
    template_name = "author_new.html"
    fields = ["fullname", "born_date", "born_location", "biography"]
    success_url = "/quote/new/"
