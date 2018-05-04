from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseBadRequest, \
	HttpResponseNotModified, HttpResponseNotFound
from django.shortcuts import render

from hello import response_status_codes


def index(request):
	header = "Personal Data"  # обычная переменная
	langs = ["English", "German", "Spanish"]  # массив
	user = {"name": "Tom", "age": 23}  # словарь
	addr = ("Абрикосовая", 23, 45)  # кортеж

	data = {"header": header, "langs": langs, "user": user, "address": addr}
	return render(request, "index.html", context=data)

def about(request):
	return HttpResponse("<h2>О сайте</h2>")


def contact(request):
	return HttpResponse("<h2>Контакты</h2>")


def products(request, productid=21):
	if productid < 100:
		category = request.GET.get("cat", "")
		output = "<h2>Product № {0}  Category: {1}</h2>".format(productid, category)
		return HttpResponse(output)
	else:
		return HttpResponseNotFound("<h2>Your query is not modified:( Please enter 'productid' < 100</h2>")


def users(request):
	id = request.GET.get("id", 22)
	name = request.GET.get("name", "Tom")
	output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
	return HttpResponse(output)
