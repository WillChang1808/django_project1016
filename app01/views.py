from django.shortcuts import render,HttpResponse,redirect
from libs.send_msg import send_msg

# Create your views here.
def index(request):
    return HttpResponse("Hello Django!")

def home(request):
    return render(request,'home.html')

def qiangungun(request):
    return redirect("https://www.qiangungun.com")

def login(request):
    print(request.method)
    return  render(request,'login.html')

def sql(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('sql'):
            return  HttpResponse('SQL执行成功')
        else:
            return HttpResponse('革命未成功，暂时不放松')
        # action = request.POST.getlist('user_select')
        # print(action)
    return  render(request,'sql.html')
def reboot(request):
    task = '200000'
    if request.method == 'POST':
        print('方法是post')
        action = request.POST.get('action')
        print(action)
       # return HttpResponse('后台收到')
        if action == 'send_mgs':
            try:
                send_msg()
            except:
                return render(request, {"content": "短信发送成功"})
                print('短信已发送')
            else:
                return  render(request,{"content":"短信未发送成功"})
                print('短信wei发送')
    return  render(request,'reboot.html')
def ajax(request):
    text = '100'
    return render(request,'ajax.html',{"content":text})


def search_form(request):
    return render(request,'search_form.html')

def search(request):
    request.encoding='utf-8'
    if 'q' in request.POST and request.POST['q']:
        message = '你搜索的内容为:' + request.POST['q']
    else:
        message = '你提交了空表单'
    return render(request,'search.html',{"content":message})
