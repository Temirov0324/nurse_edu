from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News

def news_list(request):
    news_list = News.objects.filter(is_published=True)
    paginator = Paginator(news_list, 6)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'news': news,
    }
    return render(request, 'news/list.html', context)

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk, is_published=True)
    context = {
        'news': news,
    }
    return render(request, 'news/detail.html', context)