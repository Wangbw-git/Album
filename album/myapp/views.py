from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Album

from random import randint
from PIL import Image
from datetime import datetime
import os,time

from django.core.paginator import Paginator

# Create your views here.
def index(request):
	return render(request,"myapp/index.html")

#浏览页面视图
def albums(request,pIndex):
	#将信息存入list中
	list = Album.objects.all()
	#分页
	p = Paginator(list,2)
	if pIndex == '':
		pIndex = '1'
	pIndex =int(pIndex) #强转
	list2 = p.page(pIndex) #用list2接收一页索引界面
	plist = p.page_range
	print(list2)
	context ={"alist":list2,"plist":plist,"pIndex":pIndex} #用context接收数据，并返回给页面
	return render(request,"myapp/albums.html",context)

#添加界面
def add(request):
	return render(request,"myapp/add.html")
#上传方法
def upload(request):
	'''执行图片上传'''
	myfile = request.FILES.get("pic",None)
	print(myfile)
	if not myfile: #未上传文件
		return HttpResponse("没有上传文件信息")
	#上传文件
	#文件名=随机值+.+文件扩展名
	filename = str(randint(1,100000000000))+"."+myfile.name.split('.').pop() #导入randint
	#将资源存放在./static/pics目录下
	destination = open("./static/pics/"+filename,"wb+")
	#分块写入文件
	for chunk in myfile.chunks():
		destination.write(chunk)
	#关闭存放
	destination.close()

	#缩略图
	#执行图片缩放
	image = Image.open("./static/pics/"+filename) #导入Image
	#缩放
	image.thumbnail((200,200))
	#把缩放后的图像用jpeg格式保存
	img = image.save("./static/pics/s_"+filename,None)
	#接收相片信息
	try:
		photo = Album() #从models导入Album()
		photo.title = request.POST['title']
		photo.name = filename
		photo.addtime = datetime.now() #导入datetime
		photo.save()
		context = {"info":"添加信息成功！"}
	except:
		context = {"info": "添加信息失败！"}

	return render(request,"myapp/info.html",context)

#编辑图片
def edit(request,uid):
	try:
		ob = Album.objects.get(id=uid)
		context = {"photo":ob}
		return render(request,"myapp/edit.html",context)
	except:
		context = {"info":"未找到修改信息"}
		return render(request,"myapp/info.html",context)

#执行编辑的上传图片
def update(request):
	'''执行图片上传'''
	myfile = request.FILES.get("pic", None)
	print(myfile)
	if not myfile:  # 未上传文件
		return HttpResponse("没有上传文件信息")
	# 上传文件
	# 文件名=随机值+.+文件扩展名
	filename = str(randint(1, 100000000000)) + "." + myfile.name.split('.').pop()  # 导入randint
	# 将资源存放在./static/pics目录下
	destination = open("./static/pics/" + filename, "wb+")
	# 分块写入文件
	for chunk in myfile.chunks():
		destination.write(chunk)
	# 关闭存放
	destination.close()

	# 缩略图
	# 执行图片缩放
	image = Image.open("./static/pics/" + filename)  # 导入Image
	# 缩放
	image.thumbnail((200, 200))
	# 把缩放后的图像用jpeg格式保存
	img = image.save("./static/pics/s_" + filename, None)
	# 接收相片信息
	try:
		photo = Album.objects.get(id=request.POST['id'])  # 通过models.objects.get(id=POST请求)获取
		photo.title = request.POST['title']
		photo.name = filename
		photo.addtime = datetime.now()  # 导入datetime
		photo.save()
		context = {"info": "修改信息成功！"}
	except:
		context = {"info": "修改信息失败！"}

	return render(request, "myapp/info.html", context)

#删除相片信息
def Delete(request,uid):
	try:
		photo = Album.objects.get(id=uid)
		photo.delete()
		os.remove("./static/pics"+photo.name)
		os.remove("./static/pics/s_"+photo.name)
		context = {"info":"删除信息成功！"}
	except:
		context = {"info":"删除信息失败"}

	return render(request,"myapp/info.html",context)