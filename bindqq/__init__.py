import sys
import random
sys.path.append('./')
import bindqq.getQQName

de_config_file = 'config.json'
de_default_config = {
    '每个QQ账号绑定的玩家最大数量': 1,
    'database':{}
}
gl_ranNum = {}
gl_qqName = {}
gl_qqNum = {}

def searchDB(qqNum: str, server):
    count = 0
    for key in gl_config['database']:
        if gl_config['database'][key] == qqNum:
            count += 1
    return(count)

def bind(server, info):
    if info.player not in gl_config['database'] :
    #未绑定
        if info.content[11:] == '':
            server.reply(info, '§6!!bindqq b QQ号 §7绑定QQ\n' + 
            '§6!!bindqq b ok §7验证绑定')
        if info.content[11:] == 'ok' :
        #验证绑定
            if info.player in gl_ranNum :
            #已执行绑定
                qqName = bindqq.getQQName.GetQQName(gl_qqNum[info.player])
                if qqName == gl_qqName[info.player] + gl_ranNum[info.player]:
                #正确修改QQ昵称
                    server.reply(info,'绑定成功')
                    gl_config['database'][info.player] = gl_qqNum[info.player]
                    server.save_config_simple(gl_config,de_config_file)
                else :
                #未修改/错误修改QQ昵称
                    server.reply(info,'绑定失败，请正确修改昵称后再次输入!!bindqq b ok')
            else :
            #未执行绑定
                server.reply(info,'请先输入 !!bindqq b 你的QQ号 执行绑定')
        else :
        #执行绑定
            if info.player not in gl_ranNum :
            #未执行绑定
                qqNum = info.content[11:]
                if searchDB(qqNum, server) < gl_config['每个QQ账号绑定的玩家最大数量']:
                #<QQ绑定数量上限
                    gl_qqNum[info.player] = qqNum
                    gl_qqName[info.player] = bindqq.getQQName.GetQQName(qqNum)
                    gl_ranNum[info.player] = str(random.randint(1000,9999))
                    server.reply(info,'你的QQ名称为' + gl_qqName[info.player] + '，请在昵称后面加上' + gl_ranNum[info.player] + '，然后输入!!bindqq b ok(绑定成功后可以改回原来的昵称)')
                else :
                #=QQ绑定数量上限
                    server.reply(info,'此QQ账号已经被绑定到' + str(gl_config['每个QQ账号绑定的玩家最大数量']) + '个玩家了，请先解绑后再绑定')
            else :
            #已执行绑定
                server.reply(info,'你已经输入过，请在修改QQ昵称后输入!!bindqq b ok')
    else :
    #已绑定
        server.reply(info, '已经绑定了哦')

def unbind(server, info):
    server.reply(info,'此功能暂未实现')

def on_load(server, prev):
    #加载配置文件
    global gl_config
    gl_config = server.load_config_simple(de_config_file, de_default_config)
    #注册帮助信息
    server.register_help_message('!!bindqq','绑定QQ')

def on_user_info(server, info):
    if info.content[0:8] == '!!bindqq' :
        if info.content[9:] == '' :
        #帮助信息
            server.reply(info, '§6!!bindqq §7显示帮助信息\n' +
            '§6!!bindqq b §7绑定QQ\n' +
            '§6!!bindqq ub §7解除绑定')

        elif info.content[9:10] == 'b':
        #绑定
            bind(server, info)

        elif info.content[9:] == 'ub':
        #解绑
            unbind(server, info)