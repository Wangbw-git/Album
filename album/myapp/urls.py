from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),

    #浏览相册（分页浏览）
    url(r'^albums(?P<pIndex>[0-9]+)$',views.albums, name="albums"),

	#添加相片
    url(r'^add$',views.add,name='add'),

	#执行添加相片
    url(r'^upload$',views.upload,name='upload'),

    #编辑相片
    url(r'^edit/(?P<uid>[0-9]+)$',views.edit,name='edit'),

    #执行编辑相片
    url(r'^update$',views.update,name='update'),

    #删除相片
    url(r'^Delete/(?P<uid>[0-9]+)$',views.Delete,name='Delete'),
]