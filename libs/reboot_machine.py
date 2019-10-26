import winrm

def reboot():
    win_session = winrm.Session('http://192.168.11.83:5985/wsman',auth=('Administrator','justdoit'))
    try:
        res = win_session.run_cmd('cd .. & dir')
    except:
        return '重启失败'
    else:
        return res.std_out

