from django.shortcuts import render, redirect
from web.models import RTDays, Category


def home(request):
    return render(request, 'home.html')

# def reverse(request):
#     usertext = request.GET['usertext']
#     reversedtext = usertext[::1]
#     word_counter = len(usertext.split())
#     context = {
#         'usertext': usertext,
#         'reversedtext': reversedtext,
#         'word_counter': word_counter
#     }
#     return render(request, 'web/reverse.html', context=context)

def base(request):
    return render(request, 'base.html')


def RTD(request):
    rtdays = RTDays.objects.all()  # запрашиваем все объекты rtday через менеджер объектов
    categories = Category.objects.all()  # так же получаем все Категории
    if request.method == "POST":  # проверяем то что метод именно POST
        if "Add" in request.POST:  # проверяем метод добавления rtday
            title = request.POST["description"]  # сам текст
            date = str(request.POST["date"])  # дата, до которой должно быть закончено дело
        category = request.POST["category_select"]  # категория, которой может выбрать или создать пользователь.
        content = title + " -- " + date + " " + category  # полный склеенный контент
        RTDay = RTDays(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
        RTDay.save()  # сохранение нашего дела
    return redirect("/RTDay")  # перегрузка страницы (ну вот так у нас будет устроено очищение формы)


    if "Delete" in request.POST:  # если пользователь собирается удалить одно дело
        checkedlist = request.POST.getlist('checkedbox')  # берем список выделенные дел, которые мы собираемся удалить
        for i in range(len(checkedlist)):  # мне почему-то не нравится эта конструкция
            RTDay = RTDays().objects.filter(id=int(checkedlist[i]))
            RTDay.delete()  # удаление дела
    return render(request, "home.html", {"rtdays": rtdays, "categories": categories})


def category(request):
    categories = Category.objects.all()  # запрашиваем все объекты Категорий
    if request.method == "POST":  # проверяем что это метод POST
        if "Add" in request.POST:  # если собираемся добавить
            name = request.POST["name"]  # имя нашей категории
            category = Category(name=name)  # у нашей категории есть только имя
    category.save()  # сохранение нашей категории
    return redirect("/category")


    if "Delete" in request.POST:  # проверяем есть ли удаление
        check = request.POST.getlist(
            'check')  # немного изменил название массива в отличии от rtd, что бы было меньше путаницы в коде
        for i in range(len(check)):
            try:
                categ = Category.objects.filter(id=int(check[i]))
                categ.delete()  # удаление категории
            except BaseException:  # вне сомнения тут нужно нормально переписать обработку ошибок, но на первое время хватит и этого
                return HttpResponse('<h1>Сначала удалите карточки с этими категориями)</h1>')
    return render(request, "category.html", {"categories": categories})


def redirect_view(request):
    return redirect("/category")  # редирект с главной на категории
