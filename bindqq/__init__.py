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
    #注册帮助信息
    server.register_help_message('!!bindqq','绑定QQ')

def on_user_info(server, info):
    if info.content[0:8] == '!!bindqq' :
        if info.content[9:] == '' :
        #提示
            server.reply(info, '§6!!bindqq §7显示帮助信息\n' +
            '§6!!bindqq bind §7绑定QQ\n' +
            '§6!!bindqq unbind §7验证绑定')

        elif info.content[9:13] == 'bind':
        #绑定
            if info.player not in gl_config :
            #未绑定
                if info.content[14:] == 'ok' :
                #验证绑定
                    if info.player in gl_ranNum :
                    #已执行绑定
                        qqName = bindqq.getQQName.GetQQName(gl_qqNum[info.player])
                        if qqName == gl_qqName[info.player] + gl_ranNum[info.player]:
                        #正确修改QQ昵称
                            server.reply(info,'绑定成功')
                            gl_config[info.player] = gl_qqNum[info.player]
                            server.save_config_simple(gl_config,de_config_file)
                        else :
                        #未修改/错误修改QQ昵称
                            server.reply(info,'绑定失败，请正确修改昵称后再次输入!!bindqq bind ok')
                    else :
                    #未执行绑定
                        server.reply(info,'请先输入 !!bindqq bind 你的QQ号 执行绑定')
                else :
                #执行绑定
                    if info.player not in gl_ranNum :
                    #未执行绑定
                        gl_qqNum[info.player] = info.content[14:]
                        gl_qqName[info.player] = bindqq.getQQName.GetQQName(gl_qqNum[info.player])
                        gl_ranNum[info.player] = str(random.randint(1000,9999))
                        server.reply(info,"你的QQ名称为" + gl_qqName[info.player] + '，请在昵称后面加上' + gl_ranNum[info.player] + '，然后输入!!bindqq bind ok')
                    else :
                    #已执行绑定
                        server.reply(info,'你已经输入过，请在修改QQ昵称后输入!!bindqq bind ok')
            else :
            #已绑定
                server.reply(info, '已经绑定了哦')

        elif info.content[9:] == 'unbind':
        #解绑
            server.reply(info,'此功能暂未实现')