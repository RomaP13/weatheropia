from django.shortcuts import render


def index(request):
    columns = range(1, 3)
    buttons = range(1, 6)
    return render(
        request,
        'index.html',
        {'columns': columns, 'buttons': buttons}
    )
