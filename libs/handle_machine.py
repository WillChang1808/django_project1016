import winrm

def reboot20453():
    win_session = winrm.Session('http://172.16.204.53:5985/wsman',auth=('Administrator','Qgg12#45'))
    try:
        res = win_session.run_cmd('ipconfig')
    except:
        return '重启失败'
    else:
        return res.std_out

def reboot203112():
    win_session = winrm.Session('http://172.16.203.112:5985/wsman',auth=('Administrator','Qgg12#45'))
    try:
        res = win_session.run_cmd('ipconfig')
    except:
        return '重启失败'
    else:
        return res.std_out
def clean_tab_logs():
    win_session = winrm.Session('http://172.16.154.105:5985/wsman',auth=('Administrator','Qgg12#45'))
    try:
        res = win_session.run_cmd('ipconfig')
    except:
        return '清理失败'
    else:
        return res.std_out