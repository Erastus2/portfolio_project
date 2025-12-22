from django.shortcuts import render
from .models import TechGroup

def skills_page(request):
    groups = TechGroup.objects.prefetch_related(
        "categories__items"
    ).all()

    return render(request, "skills/skill.html", {
        "groups": groups
    })
