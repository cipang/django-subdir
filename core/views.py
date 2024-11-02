from pprint import pprint
from io import StringIO

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_one(request):
    output = StringIO()
    print("== META ==", file=output)
    pprint(request.META, stream=output)
    print("\n== GET ==", file=output)
    pprint(request.GET, stream=output)
    print("\n== POST ==", file=output)
    pprint(request.POST, stream=output)
    return render(request, 'default.html',
                  {"title": "Home", "plain_text": output.getvalue()})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_two(request):
    data = request.GET["msg"] if "msg" in request.GET else "No message to show"
    return render(request, 'default.html',
                  {"title": "View 2", "div_content": data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_redir(request):
    return redirect(reverse("view_two") + "?msg=Redirected")
