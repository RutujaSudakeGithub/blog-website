from .models import Category
from about.models import SocailLinks


def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_links(request):
    social_links = SocailLinks.objects.all()
    return dict(social_links=social_links)
