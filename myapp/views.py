import os

from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, HttpResponse, redirect
from dwebsocket.decorators import accept_websocket

from myapp import models
from myapp.models import Driver
from myapp.my_utils import *


def index(request):
    return render(request, 'index.html')


def charts(request):
    return render(request, 'charts.html')


def charts2(request):
    return render(request, 'charts2.html')


def charts3(request):
    return render(request, 'charts3.html')


def notifications(request):
    return render(request, 'notifications.html')


def tables(request):
    return render(request, 'tables.html')


def typography(request):
    return render(request, 'typography.html')


def page_profile(request):
    return render(request, 'page_profile.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.USER.objects.filter(username=username, password=password).first()
        if user_obj:
            return redirect('index.html')
        else:
            data = 1
            return render(request, 'login.html', locals())


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_pwd = request.POST.get('re_pwd')
        if username and password and re_pwd:
            if password == re_pwd:
                user_obj = models.USER.objects.filter(username=username).first()
                if user_obj:
                    data = 1
                    return render(request, 'register.html', locals())
                else:
                    models.USER.objects.create(username=username, password=password).save()
                    return redirect('/login.html')
            else:
                data = 2
                return render(request, 'register.html', locals())
        else:
            data = 3
            return render(request, 'register.html', locals())


def showAll(request):
    global current_num
    if request.method == 'GET':
        drivers = Driver.objects.all()
        paginator = Paginator(drivers, 5)  # 设置每一页显示几条  创建一个panginator对象
        try:
            current_num = int(request.GET.get('page', 1))  # 当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
            drivers = paginator.page(current_num)
        except EmptyPage:
            drivers = paginator.page(4)  # 当你输入的page是不存在的时候就会报错

        if paginator.num_pages > 5:  # 如果分页的数目大于5
            if current_num - 5 < 1:  # 你输入的值
                pageRange = list(range(1, 5))  # 按钮数
            elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
                pageRange = list(range(current_num - 5, current_num + 1))  # 显示的按钮数
            else:
                pageRange = list(range(current_num - 5, current_num + 6))  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
        else:
            pageRange = paginator.page_range  # 正常分配
        return render(request, 'notifications.html', locals())
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            name = request.POST.get('name')
            num = request.POST.get('num')
            sex = request.POST.get('sex')
            type = request.POST.get('type')
            carNum = request.POST.get('carNum')
            models.Driver.objects.create(id=id, name=name, num=num, sex=sex, type=type, carNum=carNum).save()
    except:
        print("主键重复")
        data = 1
        return render(request, 'notifications.html', locals())
    else:
        print("正确")
        drivers = models.Driver.objects.all()
        return redirect('notifications.html')


def delete(request):
    if request.method == 'GET':
        id = request.GET.get('delete_id')
        models.Driver.objects.filter(id=id).delete()
        # drivers = models.Driver.objects.all()
        return redirect('notifications.html')


def tousu(request):
    if request.method == 'GET':
        tousus = models.Tousu.objects.all()
        return render(request, 'tables.html', locals())
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            sex = request.POST.get('sex')
            num = request.POST.get('num')
            id = request.POST.get('id')
            reason = request.POST.get('reason')
            models.Tousu.objects.create(id=id, name=name, num=num, sex=sex, reason=reason).save()
    except:
            tousus = models.Tousu.objects.all()
            return render(request, 'tables.html',locals())
    else:
        return redirect('tables.html')


def delete1(request):
    if request.method == 'GET':
        name = request.GET.get('delete_id')
        models.Tousu.objects.filter(name=name).delete()
        # drivers = models.Tousu.objects.all()
        return redirect('tables.html')


def update_msg(request):
    if request.method == "GET":
        data = {
            'icon': 'static/uploadefiles/icons/hehe.jpg'  # 拿头像文件路径
        }
        return render(request, 'page_profile.html', data)

    else:
        icon = request.FILES['u_icon']  # 拿文件数据
        file_name = 'icons/' + get_random_str() + '.jpg'  # 获取图片的随机名
        image_path = os.path.join('static/uploadefiles/', file_name)  # 拼接一个自己的文件路径
        with open(image_path, 'wb')as fp:  # 打开拼接的文件路径
            for i in icon.chunks():  # 遍历图片的块数据（切块的传图片）
                fp.write(i)  # 将图片数据写入自己的那个文件
        data = {  # 拼接返回数据
            'icon': '/static/uploadefiles/' + file_name  # 拿头像文件路径
        }
        # print(user.icon)
        return render(request, 'page_profile.html', data)


@accept_websocket
def echo(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        try:  # 如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'index.html')
    else:
        for message in request.websocket:
            request.websocket.send(message)  # 发送消息到客户端
