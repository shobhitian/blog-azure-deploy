from django.shortcuts import render
from .models import Post, News, Keywords
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    # Retrieve all Post objects
    keywords = Keywords.objects.all()
    news_list = News.objects.all()
    posts = Post.objects.all()
    
    
    return render(request, 'tech-index.html', {'posts': posts, 'news_list': news_list, 'keywords': keywords})


def author(request):
    return render(request, 'tech-author.html')

def category1(request):
    return render(request, 'tech-category-01.html')

def category2(request):
    return render(request, 'tech-category-02.html')

def category3(request):
    return render(request, 'tech-category-03.html')

def contact(request):
    return render(request, 'tech-contact.html')

def single(request):
   
    
    post = Post.objects.get(pk=2)
    paragraphs = post.content.split('\n')


    return render(request, 'tech-single.html', {'post': post, 'paragraphs': paragraphs})


def single_post(request, post_id):
    # Retrieve the specific Post object based on the post_id
    post = Post.objects.get(pk=post_id)
    paragraphs = post.content.split('\n')
    keywords = Keywords.objects.get(post_id=post_id)
    print(keywords.keywords)

    return render(request, 'tech-single.html', {'post': post, 'paragraphs': paragraphs, 'keywords': keywords})

def single_news(request, news_id):
    # Retrieve the specific Post object based on the post_id
    news = News.objects.get(pk=news_id)
    keywords = Keywords.objects.get(news_id=news_id)
    print(keywords.keywords)


    return render(request, 'tech-single.html', {'news': news, 'keywords': keywords})





def contact_form(request):
    if request.method == 'POST':
        # Assuming you have added the 'name' attribute to your form fields
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(message)

        # Do something with the form data, such as sending an email
        send_mail(
            f"Subject: {subject}",
            f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}",
            'eehappy69@gmail.com',  # Replace with your email address
            ['eehappy69@gmail.com'],  # Replace with the recipient's email address
            fail_silently=False,
        )
        print(send_mail)

    # Render the form template for GET requests
    return render(request, 'tech-contact.html')