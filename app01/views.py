from django.shortcuts import render,HttpResponse,redirect
from libs.send_msg import send_msg
from libs import handle_machine

# Create your views here.
# def index(request):
#     return HttpResponse("Hello Django!")

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

def index(request):
    if request.method == 'POST':
        print((request.POST))
        if request.POST.get('select1'):
            action = request.POST.get('select1')
            print(action)
            if action == 'reboot20453':
                res1 = handle_machine.reboot20453()
                if res1 == "重启失败":
                    return HttpResponse("重启失败，请选择短信通知管理员")
                else:
                    return HttpResponse(res1)
            elif action == 'send_sms':
                res1 = send_msg(content="重启204.53遇到问题")
                return HttpResponse(res1)

        if request.POST.get('select2'):
            action = request.POST.get('select2')
            print(action)
            if action == 'reboot203112':
                res2 = handle_machine.reboot203112()
                if res2 == "重启失败":
                    return HttpResponse("重启失败，请选择短信通知管理员")
                else:
                    return HttpResponse(res2)
            elif action == 'send_sms':
                res2 = send_msg(content="重启203.112遇到问题")
                return HttpResponse(res2)
        if request.POST.get('select3'):
            action = request.POST.get('select3')
            if action == 'clean_logs':
                res3 = handle_machine.clean_tab_logs()
                if res3 == "清理失败":
                    return HttpResponse("清理失败，请选择短信通知管理员")
                else:
                    return HttpResponse(res3)
            elif action == 'send_sms':
                res3 = send_msg(content="清理tableau日志遇到问题")
                return HttpResponse(res3)
            return  HttpResponse(action)
        if request.POST.get('select4'):
            res = request.POST.get('select4')
            print("demo前端返回")
            return HttpResponse("后端返回:%s" % res)
        return HttpResponse('请先选择')
    return  render(request,'index.html')
