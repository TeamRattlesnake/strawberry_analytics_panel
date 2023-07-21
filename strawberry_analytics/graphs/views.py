from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

from .daily import generate_daily_analytics
from .daily_graph import generate_daily_graph
from .monthly import generate_monthly_analytics
from .monthly_graph import generate_monthly_graph
from .service_rating import generate_service_rating
from .service_rating_graph import (
    generate_service_rating_graph,
    generate_service_published_graph,
)


# Create your views here.
def index(request):
    print(request)
    return render(request, "graphs/index.html")


def last_day(request):
    print(request)
    generate_daily_analytics()
    image = generate_daily_graph()
    try:
        with open(image, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new("RGBA", (1, 1), (255, 0, 0, 0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response


def last_month(request):
    print(request)
    generate_monthly_analytics()
    image = generate_monthly_graph()
    try:
        with open(image, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new("RGBA", (1, 1), (255, 0, 0, 0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response


def service_rating(request):
    print(request)
    generate_service_rating()
    image = generate_service_rating_graph()
    try:
        with open(image, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new("RGBA", (1, 1), (255, 0, 0, 0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response


def service_published_rating(request):
    print(request)
    generate_service_rating()
    image = generate_service_published_graph()
    try:
        with open(image, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new("RGBA", (1, 1), (255, 0, 0, 0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response
