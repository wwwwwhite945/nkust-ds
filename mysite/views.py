from django.shortcuts import render #回傳複雜的網站或模板
from django.http import HttpResponse #回傳簡單的資料
from mysite import models

def index(request):

	return render(request, "index.html",locals())

def page(request, pno):
	authors = [
		'梁小菁',
		'黃小倩',
		'盧小璇',
		'黃小婷'
	]
	if pno >=0 and pno<len(authors):
		author = authors[pno]
	else:
		author = "未知成員"
	return HttpResponse("成員簡介：{}".format(author))

def db(request, sno):
	stories = models.Story.objects.filter(sno = sno) #all 取得全部資料 get 取得單一資料 filter 取得符合條件資料
	if len(stories) >= 1:
		story = stories[0]
	else:
		story = "找不到!"
	return HttpResponse(story)