import sys
import random
sys.path.append('./')
import bindqq.getQQName

de_config_file = 'bindqq.json'
gl_ranNum = {}
gl_qqName = {}
gl_qqNum = {}

def on_load(server, prev):
    #加载配置文件
    global gl_config
    gl_config = server.load_config_simple(de_config_file, {})

def on_user_info(server, info):
    if info.content[0:8] == '!!bindqq' :
        if info.content[9:] == 'ok' :
            if info.player in gl_ranNum :
                qqName = bindqq.getQQName.GetQQName(gl_qqNum[info.player])
                if qqName == gl_qqName[info.player] + gl_ranNum[info.player]:
                    server.reply(info,'绑定成功')
                    gl_config[info.player] = gl_qqNum[info.player]
                    server.save_config_simple(gl_config,de_config_file)
                else :
                    server.reply(info,'绑定失败，请修改昵称后再次输入!!bindqq ok')
            else :
                server.reply(info,'请先输入!!bindqq+(空格)+你的QQ号')
        else :
            if info.player not in gl_ranNum :
                gl_qqNum[info.player] = info.content[9:]
                gl_qqName[info.player] = bindqq.getQQName.GetQQName(gl_qqNum[info.player])
                gl_ranNum[info.player] = str(random.randint(1000,9999))
                server.reply(info,"你的QQ名称为" + gl_qqName[info.player] + '，请在昵称后面加上' + gl_ranNum[info.player] + '，然后输入!!bindqq ok')
            else :
                server.reply(info,'你已经输入过，请在修改QQ昵称后输入!!bindqq ok')