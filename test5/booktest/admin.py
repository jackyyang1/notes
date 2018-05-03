from django.contrib import admin
from booktest.models import AreaInfo, PicTest

# 以列表的形式显示下级地区：
# class AreaInfoInline(admin.StackedInline):

# 以表格的形式显示下级地区
class AreaInfoInline(admin.TabularInline):
    model = AreaInfo
    extra = 2

class AreaInfoAdmin(admin.ModelAdmin):

    # 定义表格的字段显示
    list_display = ['id', 'atitle', 'aParent', 'parent']

    # 设置每页显示的条数
    list_per_page = 10

    # 设置操作选项的位置
    actions_on_top = False
    actions_on_bottom = True

    # 定义右侧的过滤器
    list_filter = ['atitle']

    # 增加搜索框
    search_fields = ['id', 'atitle']

    # 设置列表修改页面，子级地区和父级地区显示的上下位置
    # fields = ['aParent', 'atitle']

    # 将子级地区和父级地区分组显示
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )

    # 设置子级地址的显示：
    inlines = [AreaInfoInline]


#  Register your models here.
admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PicTest)