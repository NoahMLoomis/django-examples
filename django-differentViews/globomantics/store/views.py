from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator


def index(req):
    return HttpResponse("Index page")


def detail(req):
    return HttpResponse("This is the details page")


@require_http_methods(["GET"])
@cache_page(900)
@csrf_exempt
def electronics(req):
    items = ("windows", "mac", "iphone", "lenovo")
    if req.method == "GET":
        paginator = Paginator(items, 2)
        pages = req.GET.get("page", 1)
        try:
            items = paginator.page(pages)
        except Exception:
            items = paginator.page(1)
        resp = render(req, "store/list.html", {'items': items})
        print(req.COOKIES['visits'])
        if req.COOKIES.get("visits"):
            val = int(req.COOKIES.get("visits"))
            print("Getting cookie")
            resp.set_cookie('visits', val + 1)
        else:
            print("Initial setting cookie")
            resp.set_cookie('visits', 1)
        return resp
    if req.method == "POST":
        return HttpResponse("POST method not implimented")


class ElectronicsView(View):
    def get(self, req):
        items = ("windows", "mac", "iphone", "lenovo")
        paginator = Paginator(items, 2)
        pages = req.GET.get("page", 1)
        self.process()
        try:
            items = paginator.page(pages)
        except Exception:
            items = paginator.page(1)
        return render(req, "store/list.html", {'items': items})

    def process(self):
        print("We are processing this page")


class ComputersView(ElectronicsView):
    def process(self):
        print("We are processing computers")


class MobileView():
    def process(self):
        print("We are processing Mobile")


class EquipementView(MobileView, ComputersView):
    pass


class ElectronicsView2(TemplateView):
    template_name = "store/list.html"

    def get_context_data(self, **kwargs):
        return {"items": ("windows", "mac", "iphone", "lenovo")}


class ElectronicsView3(ListView):
    template_name = "store/list.html"
    queryset = ("windows", "mac", "iphone", "lenovo")
    context_object_name = 'items'
    paginate_by = 2
