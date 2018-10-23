from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Comment

# Create your views here.

def play(request):
    return render(request, 'play.html')

count = 0

def play2(request):
    #회원정보등 불러옴
    abc = '제형민'
    age = 20


    num = 1
    num = num + 1

    global count
    count = count + 1

    if age >19:
        status = '성인'
    else:
        status = '청소년'

    diary = ['오늘은','무엇을','했나','재미있었나요']

    return render(request, 'play2.html', {'name': abc, 'count': count, 'age' : status, 'diary' : diary, 'num': num})

def profile(request):
    return render(request, 'profile.html')

def event(request):
    abc = '제형민'
    age = 20

    global count
    count = count + 1

    #if count is 7 // 7일떄만

    if count <= 6:
        aaa = "꽝 입니다."
    elif count == 7:
        aaa = "당첨입니다."
    else :
        aaa = "역시 꽝 입니다."

    if age >19:
        status = '성인'
    else:
        status = '청소년'

    return render(request, 'event.html',{'name': abc, 'count': count, 'age' : status, 'aaa': aaa})

def newsfeed(request):
    #누스피드 불러오기
    #DB 에서 가져오기(모델링)
    articles = Article.objects.all()
    return render(request, 'newsfeed.html',{'articles': articles})

#한개의 글만 부를때
def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    #코멘트 저장하라
    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author = request.POST['nickname'],
            text = request.POST['reply'],
            password = request.POST['password']
        )
        return redirect(f'/feed/{pk}')
    # return redirect(f'/feed/{article.pk}')
    # return redirect(f'/feed/' + str(pk))
    # return redirect(f'/feed/'+ str(article.pk)) 즁 택일

    return render(request, 'detail_feed.html', {'feed': article})

def new_feed(request):
    #데이터베이스 저장

    #사용자가 제시 버튼을 눌럿는가?
    if request.method == 'POST':
    #글저장
        new_article = Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['content'] + '--추신 : 감사합니다.',
            password=request.POST['password']
        )

    return render(request,'new_feed.html')

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    #실제로 수정하는 로직
    if request.method == 'POST':#수정버튼을 눌럿다

        if redirect.POST['password'] == article.password:

            article.title = request.POST['title']
            article.author = request.POST['author']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{pk}')
            # return redirect(f'/feed/' + str(pk))
            # return redirect(f'/feed/{article.pk}')
        else:# 틀렸을때
            return redirect(f'/feed/{pk}')

    return render(request, 'edit_feed.html', {'feed': article})

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    #삭제 로직
    if request.method == 'POST':  # 수정버튼을 눌럿다
        # request.POST['password'] <---사용자가 입력한 비번
        # 진짜 비번 ---> article.password
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/')

    return render(request, 'remove_feed.html', {'feed': article})