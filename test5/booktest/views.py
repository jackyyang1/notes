from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.core.urlresolvers import reverse
from booktest.models import PicTest, AreaInfo
from django.core.paginator import Paginator

# 导入settings.py文件
from django.conf import settings



# Create your views here.
def index(request):
    return HttpResponse('hello world!')

# 定义一个视图，返回一个含有链接地址的页面
def fan1(request):
    return render(request, 'booktest/fan1.html')

# 定义视图，作为链接地址的目标视图
def fan2(request):
    return HttpResponse('跳转成功')

# 定义视图，验证重定向中使用反向解析
def red1(request):
    return HttpResponseRedirect(reverse('booktest:fan2'))

# 定义视图，可以接收两个参数
def fan3(request, v1, v2):
    return HttpResponse('%s----%s' % (v1, v2))

# 定义视图，验证重定向中使用反向解析，比较使用参数
def red2(request):
    return HttpResponseRedirect(reverse('booktest:fan3', args=[20, 30]))

# 定义视图，使用图片静态资源
def jingtai(request):
    return render(request, 'booktest/jingtai.html')

# 定义视图，验证中间件的执行
def mid(request):
    # 下面的语句会让中间件中的异常函数执行
    # print('template'+5)
    print('template')
    return render(request, 'booktest/mid.html')


# 定义视图，返回一个上传图片的表单页面
def pic_upload(request):
    return render(request, 'booktest/pic_upload.html')

# 定义视图，接收图片的数据，存储图片，同时将图片的地址写入数据库
def pic_handle(request):

    # 通过request对象的FILES属性拿到图片的数据
    f1 = request.FILES.get('pic')

    # print(f1.name)

    # 拼装图片的存储路径
    fname = settings.MEDIA_ROOT + '/booktest/' + f1.name

    with open(fname, 'wb') as pic:

        # chunks() 方法可以将图片数据进行分块，将分块的内容写入创建的图片文件
        for c in f1.chunks():
            pic.write(c)

    # 将图片的路径写入数据库
    uppic = PicTest()
    uppic.pic = 'booktest/' + f1.name
    uppic.save()

    return HttpResponse('ok')


# 定义视图，显示上传的图片
def pic_show(request):
    pics = PicTest.objects.all()
    return render(request , 'booktest/pic_show.html', {'pics':pics})

# 定义视图，显示省级地区
def pagelist(request, pindex):

    # 获取去省级的数据
    sheng = AreaInfo.objects.filter(aParent__isnull=True)

    # 通过Paginator类对省的列表数据进行分页，每页分10条
    pagenator = Paginator(sheng, 10)

    if pindex == '':
        pindex = 1

    # 拿到某一页的数据
    page = pagenator.page(int(pindex))

    return render(request, 'booktest/pagelist.html', {'page':page})


# 定义视图，返回省市区选择的下拉框页面
def area_select(request):
    return render(request, 'booktest/area_select.html')

# 定义视图，根据parent参数，返回地区的数据
def area(request):
    # 通过request对象的GET属性获取ajax通过get方式传递过来的参数
    get = request.GET
    parent = get.get('parent')

    if parent == 'none':
        area = AreaInfo.objects.filter(aParent__isnull=True)
    else:
        area = AreaInfo.objects.filter(aParent_id=int(parent))

    list = []

    for i in area:
        list.append({'id': i.id, 'atitle': i.atitle})

    return JsonResponse({'list': list})


