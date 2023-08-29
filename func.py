import paramiko
test
import time
import datetime
import socket
import os
import telegram
import requests
import tlgram_zlk_graphicversionv02
import subprocess

def is_authorized(user_id):
    authorized_users = [967187810, 5506418598, 1656936652, 6157504625, 5915921616,6064462151]
    return user_id in authorized_users

#Ssh func
def ssh_info():
    ssh = None
    ssh_info = {
        "host": "xx.xxx.x.x.xx", # your ssh information
        "username": "xxx",
        "password": "xxx"
    }

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_info["host"], username=ssh_info["username"], password=ssh_info["password"])
    return ssh

# Bağlantı durumu
def connection_test(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        
        user_name = update.effective_user.name
        update.effective_message.reply_text("The connection is tested. Please wait." + user_name)
        ssh = None
        
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("xxxxx", username="xxxx", password="xxx")
        except:
            update.effective_message.reply_text("The Gui machine is closed or cannot be reached")
            return ssh
        
        try:
            sshtransport_13_machine = ssh.get_transport()
            dest_addr = ('x.x.x.x', 22)
            local_addr = ('x.x.x.x', 22)
            sshchannel_13_machine = sshtransport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)
        except:
            update.effective_message.reply_text("The xxx  machine is closed or cannot be reached")
            return
        
        try:
            sshtransport_12_machine = ssh.get_transport()
            dest_addr = ('y.y.y.y', 22)
            local_addr = ('y.y.y.y', 22)
            sshchannel_12_machine = sshtransport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)
        except:
            update.effective_message.reply_text("The yyy  machine is closed or cannot be reached")
            return
        
        update.effective_message.reply_text("Connection is successful, servers are open" + user_name)
    


def containers_restart(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        user_name = update.effective_user.name
        update.effective_message.reply_text("your message!" + user_name)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("x.x.xx.x", username="xx", password="x")

        ssh_transport_12_machine = ssh.get_transport()
        dest_addr = ('x.x.x.x', 22)
        local_addr = ('x.x.x.x', 22)
        ssh_channel_12_machine = ssh_transport_12_machine.open_channel("direct-tcpip", dest_addr, local_addr)

        x_machine_host = paramiko.SSHClient()
        x_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        x_machine_host.connect('xx.xx.x.xx', username='x', password='xx', sock=ssh_channel_12_machine)
        
        sshtransport_13_machine = ssh.get_transport()
        dest_addr = ('y.y.y.y', 22)
        local_addr = ('x.x.x.x', 22) 
        sshchannel_13_machine = sshtransport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)

                            
        y_machine_host = paramiko.SSHClient()
        y_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        y_machine_host.connect('y.y.y.y', username='username', password='username1', sock=sshchannel_13_machine)

        x_server_container = [
            'x-machine-container-container',
            'x-machine-container-2-container',
            'x-machine-container-3-container',
            'x-machine-container-4-container',
            'x-machine-container-5-container',
            'x-machine-container-6-container'
        ]

        y_server_container = [
            'x-machine-container-7-container',
            'x-machine-container-8-container',
            'x-machine-container-9-container',
            'x-machine-container-10-container',
            'x-machine-container-11-container',
            'x-machine-container-12-container'
        ]
        
        xxx_command = f'docker restart {" ".join(x_server_container)}'
        # output = ssh_stdout.read().decode('utf-8')
        # update.effective_message.reply_text(chat_id=update.message.chat_id, text=output)
        xxx1_command = f'docker restart {" ".join(y_server_container)}'
        ssh_stdin, ssh_stdout, ssh_stderr = x_machine_host.exec_command(xxx_command)
        ssh_stdin, ssh_stdout, ssh_stderr = y_machine_host.exec_command(xxx1_command)
        print()
        time.sleep(10)
        update.effective_message.reply_text("Your Message")

        x_machine_host.close()
        y_machine_host.close()
        ssh.close() 
    else:
        query.answer("Unauthorized access!")

def _containers_stop(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        user_name = update.effective_user.name
        update.effective_message.reply_text("Görünür kameralar durduruldu.Lütfen Bekleyiniz. " + user_name)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("x.xx.x.x.xxx", username="username", password="username1")

        ssh_transport_12_machine = ssh.get_transport()
        dest_addr = ('x.xx.x.x.xxx', 22)
        local_addr = ('x.xx.x.x.xxx', 22)
        ssh_channel_12_machine = ssh_transport_12_machine.open_channel("direct-tcpip", dest_addr, local_addr)

        x_machine_host = paramiko.SSHClient()
        x_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        x_machine_host.connect('x.xx.x.x.xxx', username='username', password='username1', sock=ssh_channel_12_machine)
        
        sshtransport_13_machine = ssh.get_transport()
        dest_addr = ('y.yy.y.y.yy', 22)
        local_addr = ('x.xx.x.x.xxx', 22) 
        sshchannel_13_machine = sshtransport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)

                            
        y_machine_host = paramiko.SSHClient()
        y_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        y_machine_host.connect('y.yy.y.y.yy', username='username', password='username1', sock=sshchannel_13_machine)

        x_server_container = [
            'x-machine-container-container',
            'x-machine-container-2-container',
            'x-machine-container-3-container',
            'x-machine-container-4-container',
            'x-machine-container-5-container',
            'x-machine-container-6-container'
        ]

        y_server_container = [
            'y-machine-container-7-container',
            'y-machine-container-8-container',
            'y-machine-container-9-container',
            'y-machine-container-10-container',
            'y-machine-container-11-container',
            'y-machine-container-12-container'
        ]
        
        x_server_command = f'docker stop {" ".join(x_server_container)}'
        # output = ssh_stdout.read().decode('utf-8')
        # update.effective_message.reply_text(chat_id=update.message.chat_id, text=output)
        xxx1_command = f'docker stop {" ".join(y_server_container)}'
        ssh_stdin, ssh_stdout, ssh_stderr = x_machine_host.exec_command(xxx_command)
        ssh_stdin, ssh_stdout, ssh_stderr = y_machine_host.exec_command(xxx1_command)
        time.sleep(10)
        update.effective_message.reply_text("Başarılı Görünür Kameralar durduruldu.")

        x_machine_host.close()
        y_machine_host.close()
        ssh.close()
    else:
        # Kullanıcı yetkilendirilmemişse hata mesajı gönder
        query.answer("Unauthorized access!")
        
def containers_start(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
    
        user_name = update.effective_user.name
        update.effective_message.reply_text("Your Message ! " + user_name)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("x.xx.x.x.xxx", username="username", password="username1")

        ssh_transport_12_machine = ssh.get_transport()
        dest_addr = ('x.xx.x.x.xxx', 22)
        local_addr = ('x.xx.x.x.xxx', 22)
        ssh_channel_12_machine = ssh_transport_12_machine.open_channel("direct-tcpip", dest_addr, local_addr)

        x_machine_host = paramiko.SSHClient()
        x_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        x_machine_host.connect('x.xx.x.x.xxx', username='username', password='username1', sock=ssh_channel_12_machine)
        
        sshtransport_13_machine = ssh.get_transport()
        dest_addr = ('y.yy.y.y.yy', 22)
        local_addr = ('x.xx.x.x.xxx', 22) 
        sshchannel_13_machine = sshtransport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)

                            
        y_machine_host = paramiko.SSHClient()
        y_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        y_machine_host.connect('y.yy.y.y.yy', username='username', password='username1', sock=sshchannel_13_machine)

        x_server_container = [
            'x-machine-container-container',
            'x-machine-container-2-container',
            'x-machine-container-3-container',
            'x-machine-container-4-container',
            'x-machine-container-5-container',
            'x-machine-container-6-container'
        ]

        y_server_container = [
            'x-machine-container-7-container',
            'x-machine-container-8-container',
            'x-machine-container-9-container',
            'x-machine-container-10-container',
            'x-machine-container-11-container',
            'x-machine-container-12-container'
        ]
        
        xxx_command = f'docker start {" ".join(x_server_container)}'
        # output = ssh_stdout.read().decode('utf-8')
        # update.effective_message.reply_text(chat_id=update.message.chat_id, text=output)
        xxx1_command = f'docker start {" ".join(y_server_container)}'
        ssh_stdin, ssh_stdout, ssh_stderr = x_machine_host.exec_command(xxx_command)
        ssh_stdin, ssh_stdout, ssh_stderr = y_machine_host.exec_command(xxx1_command)
        time.sleep(10)
        update.effective_message.reply_text("YOur Messageee !")

        x_machine_host.close()
        y_machine_host.close()
        ssh.close()
    else:
        # Kullanıcı yetkilendirilmemişse hata mesajı gönder
        query.answer("Unauthorized access!")

#22ff START Containers
def 22ff_containers_start(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
    
        user_name = update.effective_user.name
        update.effective_message.reply_text("your messageeeeee" + user_name)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("x.xx.x.x.xxx", username="username", password="username1")

        ssh_transport_12_machine = ssh.get_transport()
        dest_addr = ('x.xx.x.x.xxx', 22)
        local_addr = ('x.xx.x.x.xxx', 22)
        ssh_channel_12_machine = ssh_transport_12_machine.open_channel("direct-tcpip", dest_addr, local_addr)

        x_machine_host = paramiko.SSHClient()
        x_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        x_machine_host.connect('x.xx.x.x.xxx', username='username', password='username1', sock=ssh_channel_12_machine)
        
        sshtransport_13_machine = ssh.get_transport()
        dest_addr = ('y.yy.y.y.yy', 22)
        local_addr = ('x.xx.x.x.xxx', 22) 
        sshchannel_13_machine = sshtransport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)

                            
        y_machine_host = paramiko.SSHClient()
        y_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        y_machine_host.connect('y.yy.y.y.yy', username='username', password='username1', sock=sshchannel_13_machine)

        x_server_container = [
            'xxx-xxx-container',
            'xxx-xxx-2-container',
            'xxx-xxx-3-container',
        ]

        y_server_container = [
            'xxx-xxx-4-container',
            'xxx-xxx-5-container',
            'xxx-xxx-6-container',
        ]
        
        xxx_command = f'docker start {" ".join(x_server_container)}'
        # output = ssh_stdout.read().decode('utf-8')
        # update.effective_message.reply_text(chat_id=update.message.chat_id, text=output)
        xxx1_command = f'docker start {" ".join(y_server_container)}'
        ssh_stdin, ssh_stdout, ssh_stderr = x_machine_host.exec_command(xxx_command)
        time.sleep(5)
        ssh_stdin, ssh_stdout, ssh_stderr = y_machine_host.exec_command(xxx1_command)

        update.effective_message.reply_text("BYour Message")

        x_machine_host.close()
        y_machine_host.close()
        ssh.close()
        
    else:
        # Kullanıcı yetkilendirilmemişse hata mesajı gönder
        query.answer("Unauthorized access!")
 
#22ff STOP Containers
def 22ff_containers_stop(update, context):
    
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        user_name = update.effective_user.name
        update.effective_message.reply_text("Your messageeeeeeeeee" + user_name)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("x.xx.x.x.xxx", username="username", password="username1")

        ssh_transport_12_machine = ssh.get_transport()
        dest_addr = ('x.xx.x.x.xxx', 22)
        local_addr = ('x.xx.x.x.xxx', 22)
        ssh_channel_12_machine = ssh_transport_12_machine.open_channel("direct-tcpip", dest_addr, local_addr)

        x_machine_host = paramiko.SSHClient()
        x_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        x_machine_host.connect('x.xx.x.x.xxx', username='username', password='username1', sock=ssh_channel_12_machine)
        
        sshtransport_13_machine = ssh.get_transport()
        dest_addr = ('y.yy.y.y.yy', 22)
        local_addr = ('x.xx.x.x.xxx', 22) 
        sshchannel_13_machine = sshtransport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)

                            
        y_machine_host = paramiko.SSHClient()
        y_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        y_machine_host.connect('y.yy.y.y.yy', username='username', password='username1', sock=sshchannel_13_machine)

        x_server_container = [
            'xxx-xxx-container',
            'xxx-xxx-2-container',
            'xxx-xxx-3-container',
        ]

        y_server_container = [
            'xxx-xxx-4-container',
            'xxx-xxx-5-container',
            'xxx-xxx-6-container',
        ]
        
        xxx_command = f'docker stop {" ".join(x_server_container)}'
        # output = ssh_stdout.read().decode('utf-8')
        # update.effective_message.reply_text(chat_id=update.message.chat_id, text=output)
        xxx1_command = f'docker stop {" ".join(y_server_container)}'
        ssh_stdin, ssh_stdout, ssh_stderr = x_machine_host.exec_command(xxx_command)
        time.sleep(5)
        ssh_stdin, ssh_stdout, ssh_stderr = y_machine_host.exec_command(xxx1_command)
        time.sleep(5)
        update.effective_message.reply_text("YOur Messageeeeeeeeeeeeeeeee")

        x_machine_host.close()
        y_machine_host.close()
        ssh.close()
    else:
        # Kullanıcı yetkilendirilmemişse hata mesajı gönder
        query.answer("Unauthorized access!")
 
#22ff RESTART Containers
def 22ff_containers_restart(update, context):
    
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
            
        user_name = update.effective_user.name
        update.effective_message.reply_text("YOur MEssageeeeeeeeeeeeeeeeeeeee" + user_name)
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("x.xx.x.x.xxx", username="username", password="username1")
            
            try:
                ssh_transport_12_machine = ssh.get_transport()
                dest_addr = ('x.xx.x.x.xxx', 22)
                local_addr = ('x.xx.x.x.xxx', 22)
                ssh_channel_12_machine = ssh_transport_12_machine.open_channel("direct-tcpip", dest_addr, local_addr)
                
                x_machine_host = paramiko.SSHClient()
                x_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                x_machine_host.connect('x.xx.x.x.xxx', username='username', password='username1', sock=ssh_channel_12_machine)
                
                try:
                    ssh_transport_13_machine = ssh.get_transport()
                    dest_addr = ('y.yy.y.y.yy', 22)
                    local_addr = ('x.xx.x.x.xxx', 22) 
                    ssh_channel_13_machine = ssh_transport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)
                    
                    y_machine_host = paramiko.SSHClient()
                    y_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    y_machine_host.connect('y.yy.y.y.yy', username='username', password='username1', sock=ssh_channel_13_machine)
                    
                    x_server_container = [
                        'xxx-xxx-container',
                        'xxx-xxx-2-container',
                        'xxx-xxx-3-container',
                    ]

                    y_server_container = [
                        'xxx-xxx-4-container',
                        'xxx-xxx-5-container',
                        'xxx-xxx-6-container',
                    ]

                    xxx_command = f'docker restart {" ".join(x_server_container)}'
                    xxx1_command = f'docker restart {" ".join(y_server_container)}'

                    ssh_stdin, ssh_stdout, ssh_stderr = x_machine_host.exec_command(xxx_command)
                    time.sleep(5)
                    ssh_stdin, ssh_stdout, ssh_stderr = y_machine_host.exec_command(xxx1_command)
                    time.sleep(5)
                    
                    update.effective_message.reply_text("Your MEssage ")
                    
                    y_machine_host.close()
                    ssh_channel_13_machine.close()
                    x_machine_host.close()
                    ssh_channel_12_machine.close()
                    
                except Exception as e:
                    update.effective_message.reply_text("errorr")
                    x_machine_host.close()
                    ssh_channel_12_machine.close()
                    
            except Exception as e:
                update.effective_message.reply_text("errorrrr")
            
        except Exception as e:
            update.effective_message.reply_text("Errorrrr")
    else:
        # Kullanıcı yetkilendirilmemişse hata mesajı gönder
        query.answer("Unauthorized access!")    
        
#xxx Docker ps
def xxxdockerps(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
    
        
        user_name = update.effective_user.name
        update.effective_message.reply_text("Containers working in the machine are checked. Please wait. " + user_name)
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("x.xx.x.x.xxx", username="username", password="username1")

            ssh_transport_12_machine = ssh.get_transport()
            dest_addr = ('x.xx.x.x.xxx', 22)
            local_addr = ('x.xx.x.x.xxx', 22)
            ssh_channel_12_machine = ssh_transport_12_machine.open_channel("direct-tcpip", dest_addr, local_addr)

            x_machine_host = paramiko.SSHClient()
            x_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                x_machine_host.connect('x.xx.x.x.xxx', username='username', password='username1', sock=ssh_channel_12_machine)
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                error_message = "Failed to connect to Server 1. Error: {}".format(str(e))
                update.effective_message.reply_text(text=error_message)
                return

            ssh_transport_13_machine = ssh.get_transport()
            dest_addr = ('y.yy.y.y.yy', 22)
            local_addr = ('x.xx.x.x.xxx', 22) 
            ssh_channel_13_machine = ssh_transport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)

            y_machine_host = paramiko.SSHClient()
            y_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                y_machine_host.connect('y.yy.y.y.yy', username='username', password='username1', sock=ssh_channel_13_machine)
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                error_message = "Failed to connect to Server 2. Error: {}".format(str(e))
                update.effective_message.reply_text(text=error_message)
                x_machine_host.close()
                return

            command = "docker ps --format 'table {{.Names}}\t{{.Status}}'"
            ssh_stdin, ssh_stdout, ssh_stderr = x_machine_host.exec_command(command)
            output = ssh_stdout.read().decode()
            update.effective_message.reply_text(text=output)

            command = "docker ps --format 'table {{.Names}}\t{{.Status}}'"
            ssh_stdin, ssh_stdout, ssh_stderr = y_machine_host.exec_command(command)
            output = ssh_stdout.read().decode()
            update.effective_message.reply_text(text=output)

            y_machine_host.close()
            x_machine_host.close()

        except (paramiko.SSHException, paramiko.AuthenticationException) as e:
            # Handle SSH connection errors for the main server
            error_message = "error: {}".format(str(e))
            update.effective_message.reply_text(text=error_message)
    else:
        # Kullanıcı yetkilendirilmemişse hata mesajı gönder
        query.answer("Unauthorized access!") 
                          
    #Gui Docker ps

#Gui Docker ps 
def guidockerps(update, context):
    query = update.callback_query
    user_id = update.effective_user.id
    
    if is_authorized(user_id):
        user_name = update.effective_user.name
        update.effective_message.reply_text("Containers working in the machine are checked. Please wait." + user_name)
        try:
            ssh = ssh_info()
            command = "docker ps --format 'table {{.Names}}\t{{.Status}}'"
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            output = ssh_stdout.read().decode()
            update.effective_message.reply_text(text=output)


        except (paramiko.SSHException, paramiko.AuthenticationException) as e:
            # Handle SSH connection errors for the main server
            error_message = "ERror: {}".format(str(e))
            update.effective_message.reply_text(text=error_message)
        ssh.close()
    else:
        # Kullanıcı yetkilendirilmemişse hata mesajı gönder
        query.answer("Unauthorized access!")       
        
#Gui Docker Process
def gui_docker_process(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        query = update.callback_query
        query.answer()  

        callback_data = query.data
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time, query.data)
        ssh = ssh_info()

        if callback_data =='gui_docker_start':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Gui Container Başlatılıyor.Lütfen Bekleyiniz. " + user_name)
            try:
                    command = "docker start xxx-xxxxxxx-gui-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text=output + " Başlatıldı.")
                    ssh.close()
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()
        elif callback_data =='gui_docker_stop':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Gui Container Durduruluyor.Lütfen Bekleyiniz. " + user_name)
            try:
                    command = "docker stop xxx-xxxxxxx-gui-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text=output + " Durduruldu.")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()
        elif callback_data =='gui_docker_restart':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Gui Container yeniden başlatılıyor.Lütfen Bekleyiniz. " + user_name)
            try:
                    command = "docker restart xxx-xxxxxxx-gui-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text=output + " Restarted")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()
        elif callback_data =='mmh_docker_start':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Mmh Container Başlatılıyor. Lütfen Bekleyiniz. " + user_name)
            try:
                    command = "docker start xxx-xxxxxxx-mmh-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " Başlatıldı.")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()
        elif callback_data =='mmh_docker_stop':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Mmh Container Durduruluyor. Lütfen Bekleyiniz. " + user_name)
            try:
                    command = "docker stop xxx-xxxxxxx-mmh-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " Durduruldu.")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()
        elif callback_data =='mmh_docker_restart':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Mmh Container yeniden başlatılıyor. Lütfen Bekleyiniz. " + user_name)
            try:
                    command = "docker restart xxx-xxxxxxx-mmh-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " Durduruldu.")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()
        elif callback_data =='dü_docker_start':
            user_name = update.effective_user.name
            update.effective_message.reply_text("beeee" + user_name)
            try:
                    command = "docker start xxx-xxxxxxx-test-unit-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " Başlatıldı.")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()
        elif callback_data =='dü_docker_stop':
            user_name = update.effective_user.name
            update.effective_message.reply_text("beeee" + user_name)
            try:
                    command = "docker stop xxx-xxxxxxx-test-unit-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " beeee.")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()       
        elif callback_data =='dü_docker_restart':
            user_name = update.effective_user.name
            update.effective_message.reply_text("teasdasdasd " + user_name)
            try:
                    command = "docker restart xxx-xxxxxxx-test-unit-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " Restarted")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()     
        elif callback_data =='cs_docker_start':
            user_name = update.effective_user.name
            update.effective_message.reply_text("aetaetaet. " + user_name)
            try:
                    command = "docker start xxx-xxxxxxx-testserver-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + "Başlatıldı.")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()     
        elif callback_data =='cs_docker_stop':
            user_name = update.effective_user.name
            update.effective_message.reply_text("aetaetgaeaaet" + user_name)
            try:
                    command = "docker stop xxx-xxxxxxx-testserver-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " Durduruldu.")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()          
        elif callback_data =='cs_docker_restart':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Cteasdasdasd " + user_name)
            try:
                    command = "docker restart xxx-xxxxxxx-testserver-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " Restarted")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()
        elif callback_data =='gui_all_packages_restart':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Bütün Containerler Yeniden başlatılıyor.. Lütfen Bekleyiniz. " + user_name)
            try:
                    command = "docker restart xxx-xxxxxxx-testserver-container xxx-xxxxxxx--container xxx-xxxxxxx-mmh-container xxx-xxxxxxx-gui-container xxx-xxxxxxx-test-unit-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " Restarted")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()    
        elif callback_data =='gui_all_packages_stop':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Bütün Containerler durduruluyor.. Lütfen Bekleyiniz. " + user_name)
            try:
                    command = "docker stop xxx-xxxxxxx-container xxx-xxxxxxx-container xxx-xxxxxxx-container xxx-xxxxxxx-gui-container xxx-xxxxx-container"
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                    output = ssh_stdout.read().decode()
                    update.effective_message.reply_text(text= output + " Durduruldu.")
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:
                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()                    
        elif callback_data =='gui_all_packages_postgre':
            user_name = update.effective_user.name
            update.effective_message.reply_text("waittt " + user_name)
            try:
                    # ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('docker restart xx-postgres')
                    # output = ssh_stdout.read().decode('utf-8')  # 
                    # update.effective_message.reply_text(text=output + 'Your MEssage') 
                    # time.sleep(2)
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('docker restart xxx-xxxxxxx-gui-container')
                    output = ssh_stdout.read().decode('utf-8')  # 
                    update.effective_message.reply_text(text=output + 'Your MEssage') 
                    time.sleep(2)
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('docker restart xxx-xxxxxxx--unit-container')
                    output = ssh_stdout.read().decode('utf-8')  # 
                    update.effective_message.reply_text(text=output + 'Your MEssage')     
                    time.sleep(2)  
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:

                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()  
        elif callback_data =='_docker_start':
            user_name = update.effective_user.name
            update.effective_message.reply_text(" " + user_name)
            try:
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('docker start xxx-xxxxxxx--container')
                    output = ssh_stdout.read().decode('utf-8')  # 
                    update.effective_message.reply_text(text=output + 'restarted.') 
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:

                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()  
        elif callback_data =='_docker_stop':
            user_name = update.effective_user.name
            update.effective_message.reply_text("  " + user_name)
            try:
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('docker stop xxx-xxxxxxx--container')
                    output = ssh_stdout.read().decode('utf-8')  # 
                    update.effective_message.reply_text(text=output + 'stopped.') 
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:

                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()  
        elif callback_data =='_docker_restart':
            user_name = update.effective_user.name
            update.effective_message.reply_text(" " + user_name)
            try:
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('docker restart xxx-xxxxxxx--container')
                    output = ssh_stdout.read().decode('utf-8')  # 
                    update.effective_message.reply_text(text=output + 'restarted') 
            except (paramiko.SSHException, paramiko.AuthenticationException) as e:

                    error_message = "Error: {}".format(str(e))
                    update.effective_message.reply_text(text=error_message)
                    ssh.close()    
    else:

        query.answer("Unauthorized access!")       
        
               
def logs_logs(update, context):
    
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        if update.effective_message is None:
            chat_id = update.effective_chat.id
        else:
            chat_id = update.effective_message.chat_id

        query = update.callback_query
        query.answer()

        callback_data = query.data
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time, query.data)

        ssh = ssh_info()
        
        
        if callback_data == 'gui_24h_logs':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Sending last 24 used log of Gui Container..This process may take a few minutes.")
            now = datetime.datetime.now()
            one_day_ago = now - datetime.timedelta(days=1)
            since_date = one_day_ago.strftime('%Y-%m-%dT%H:%M:%S')

        
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"docker logs --timestamps xxx-xxxxxxx-gui-container --since {since_date} > guilog.txt")
            time.sleep(30)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"tar -czvf guilog.tar.gz guilog.txt")
            time.sleep(30)

            sftp = ssh.open_sftp()
            sftp.get('guilog.tar.gz', 'guilog.tar.gz')


            with open('guilog.tar.gz', 'rb') as f:
                context.bot.send_document(chat_id=chat_id, document=f)
            
        elif callback_data == 'gui_tail_f':
            ssh_stin,ssh_stdout,ssh_stderr = ssh.exec_command("docker logs --tail=25 xxx-xxxxxxx-gui-container")
            output = ssh_stdout.read().decode('utf-8')
            update.effective_message.reply_text(text=output)
                
        elif callback_data =='mmh_24h_logs':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Sending last 48 used log of MMH Container..This process may take a few minutes." + user_name)
            now = datetime.datetime.now()
            one_day_ago = now - datetime.timedelta(days=1)
            since_date = one_day_ago.strftime('%Y-%m-%dT%H:%M:%S')
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"docker logs --timestamps xxx-xxxxxxx-mmh-container --since {since_date} > mmhlog.txt")
            time.sleep(30)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"tar -czvf mmhlog.tar.gz mmhlog.txt")
            time.sleep(30)

            sftp = ssh.open_sftp()
            sftp.get('mmhlog.tar.gz', 'mmhlog.tar.gz')
            
            with open('mmhlog.tar.gz', 'rb') as f:
                context.bot.send_document(chat_id=chat_id, document=f)
                
        elif callback_data == 'mmh_tail_f':
            ssh_stin,ssh_stdout,ssh_stderr = ssh.exec_command("docker logs --tail=25 xxx-xxxxxxx-mmh-container")
            output = ssh_stdout.read().decode('utf-8')
            update.effective_message.reply_text(text=output)
                
        elif callback_data =='du_24h_logs':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Sending last 48 used log of test  Container..This process may take a few minutes." + user_name)
            now = datetime.datetime.now()
            one_day_ago = now - datetime.timedelta(days=1)
            since_date = one_day_ago.strftime('%Y-%m-%dT%H:%M:%S')
            print(since_date)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"docker logs --timestamps xxx-xxxxxxx-test-unit-container --since {since_date} > dulogs.txt")
            time.sleep(30)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"tar -czvf dulogs.tar.gz dulogs.txt")
            time.sleep(30)
            

            sftp = ssh.open_sftp()
            sftp.get('dulogs.tar.gz', 'dulogs.tar.gz')
            
            with open('dulogs.tar.gz', 'rb') as f:
                context.bot.send_document(chat_id=chat_id, document=f)
                
        elif callback_data == 'du_tail_f':
            ssh_stin,ssh_stdout,ssh_stderr = ssh.exec_command("docker logs --tail=20 xxx-xxxxxxx-test-unit-container")
            output = ssh_stdout.read().decode('utf-8')
            update.effective_message.reply_text(text=output)

        elif callback_data =='journal_24h_logs':
            user_name = update.effective_user.name
            update.effective_message.reply_text("Sending last 48 used log of Journal..This process may take a few minutes." + user_name)
            
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"journalctl --since '1 days ago' > journallogs.txt")
            time.sleep(30)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"tar -czvf journallogs.tar.gz journallogs.txt")
            time.sleep(30)

            sftp = ssh.open_sftp()
            sftp.get('journallogs.tar.gz', 'journallogs.tar.gz')

            with open('journallogs.tar.gz', 'rb') as f:
                context.bot.send_document(chat_id = chat_id, document=f)

            os.remove('journallogs.tar.gz')
    else:
        query.answer("Unauthorized access!")       
        

def temperature_control(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
    
        if update.message is None:
            chat_id = update.effective_chat.id
        else:
            chat_id = update.message.chat_id
        query = update.callback_query
        query.answer()

        callback_data = query.data
        ssh = ssh_info()
        
        if callback_data == 'temp_control':
            user_name = update.effective_user.name
            update.effective_message.reply_text("The heat status is checked." + user_name)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('/home/username/Desktop/yourpc/yourdirectory/xxx.sh')
    else:

        query.answer("Unauthorized access!")
        
#power control check server
def check_server(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((host, port))
        sock.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False


def system_power(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
    
        user_name = update.effective_user.name
        update.effective_message.reply_text("Bekleyiniz." + user_name)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("x.xx.x.x.xxx", username="username", password="username1")

        sshtransport_13_machine = ssh.get_transport()
        dest_addr = ('y.yy.y.y.yy', 22)
        local_addr = ('x.xx.x.x.xxx', 22)
        sshchannel_13_machine = sshtransport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)

                            
        y_machine_host = paramiko.SSHClient()
        y_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        y_machine_host.connect('y.yy.y.y.yy', username='username', password='username1', sock=sshchannel_13_machine)

        sshtransport_12_machine = ssh.get_transport()
        dest_addr = ('x.xx.x.x.xxx', 22)
        local_addr = ('y.yy.y.y.yy', 22)
        sshchannel_12_machine = sshtransport_12_machine.open_channel("direct-tcpip", dest_addr, local_addr)

                            
        x_machine_host = paramiko.SSHClient()
        x_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        x_machine_host.connect('x.xx.x.x.xxx', username='username', password='username1', sock=sshchannel_12_machine)

        y_machine_host = update.message.text
        if y_machine_host == '/rebootxxx':

            ssh_stdin, ssh_stdout, ssh_stderr = x_machine_host.exec_command('sudo reboot now') 
            time.sleep(5)
            xxx12_machine_status = check_server('x.xx.x.x.xxx', 22)
            context.bot.send_message(chat_id=update.message.chat_id, text='')

        elif y_machine_host == '/rebootxxx1':
            ssh_stdin, ssh_stdout, ssh_stderr = y_machine_host.exec_command('sudo reboot now')
            time.sleep(5)
            xxx13_machine_status = check_server('y.yy.y.y.yy', 22)
            context.bot.send_message(chat_id=update.message.chat_id, text='.')

        elif y_machine_host == '/rebootgui':
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('sudo reboot now')
            print(ssh_stdout.read().decode())
            time.sleep(3)
            gui_machine_status = check_server('x.xx.x.x.xxx', 22)
            context.bot.send_message(chat_id=update.message.chat_id, text='')

        elif y_machine_host == '/shutdownxxx':

            ssh_stdin, ssh_stdout, ssh_stderr = x_machine_host.exec_command('sudo shutdown now') 
            time.sleep(5)
            xxx12_machine_status = check_server('x.xx.x.x.xxx', 22)
            context.bot.send_message(chat_id=update.message.chat_id, text='')

        elif y_machine_host == '/shutdownxxx1':
            ssh_stdin, ssh_stdout, ssh_stderr = y_machine_host.exec_command('sudo shutdown now')
            time.sleep(5)
            xxx13_machine_status = check_server('y.yy.y.y.yy', 22)
            context.bot.send_message(chat_id=update.message.chat_id, text='')

        elif y_machine_host == '/shutdowngui':
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('sudo shutdown now')
            print(ssh_stdout.read().decode())
            time.sleep(3)
            gui_machine_status = check_server('x.xx.x.x.xxx', 22)
            context.bot.send_message(chat_id=update.message.chat_id, text='.')

        else:
            pass
    else:

        query.answer("Unauthorized access!")
        
#Power Control Menü
def power_control(update, context):
    user_name = update.effective_message.from_user.name
    update.effective_message.reply_text("Bekleyiniz." + user_name)
    authorized_users = [967187810]

    user_id = update.effective_message.from_user.id

    if user_id in authorized_users:
        message =  """

        *Power Control* :    
        
        *#* /rebootxxx
        *#* /rebootyyy
        *#* /rebootgui
        *#* /shutdownxxx
        *#* /shutdownxxx1
        *#* /shutdowngui
        """
        context.bot.send_message(chat_id=update.message.chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        update.message.reply_text("Bu komutu kullanma izniniz yok.")

def logs_monitor(update,context):
        authorized_users = [967187810]
        user_id = update.effective_message.from_user.id
        if user_id not in authorized_users:
            update.effective_message.reply_text("Bu komutu kullanma izniniz yok.")
            return
        try:

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("x.xx.x.x.xxx", username="username", password="username1")
        except:
            update.effective_message.reply_text("Gui Server Kapalı ya da Ulaşılamıyor")
        else:  

            sshtransport_12_machine = ssh.get_transport()
            dest_addr = ('x.xx.x.x.xxx', 22) #edited#
            local_addr = ('x.xx.x.x.xxx', 22) #edited#
            sshchannel_12_machine = sshtransport_12_machine.open_channel("direct-tcpip", dest_addr, local_addr)

                            
            x_machine_host = paramiko.SSHClient()
            x_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            x_machine_host.connect('x.xx.x.x.xxx', username='username', password='username1', sock=sshchannel_12_machine)



            sshtransport_13_machine = ssh.get_transport()
            dest_addr = ('y.yy.y.y.yy', 22) #edited#
            local_addr = ('x.xx.x.x.xxx', 22) #edited#
            sshchannel_13_machine = sshtransport_13_machine.open_channel("direct-tcpip", dest_addr, local_addr)

                            
            y_machine_host = paramiko.SSHClient()
            y_machine_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            y_machine_host.connect('y.yy.y.y.yy', username='username', password='username1', sock=sshchannel_13_machine)
        logs_command = update.message.text 
        if logs_command == '/goilogsf' : 
            try: 
                ssh_stin,ssh_stdout,ssh_stderr = ssh.exec_command("docker logs --tail=15 xxx-xxxxxxx-gui-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output) 
            except paramiko.SSHException:
                update.message.reply_text("There was an error when buying the logs.")
        elif logs_command == '/mkhlogsf':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = ssh.exec_command("docker logs --tail=15 xxx-xxxxxxx-mmh-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                update.message.reply_text("There was an error when buying the logs.")
        elif logs_command == '/logsf':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = ssh.exec_command("docker logs --tail=15 xxx-xxxxxxx-test-unit-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                update.message.reply_text("There was an error when buying the logs.")
        elif logs_command == '/postgreslogsf':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = ssh.exec_command("docker logs --tail=15 xx-postgres")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                update.message.reply_text("There was an error when buying the logs.")
        elif logs_command == '/cerverlogsf':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = ssh.exec_command("docker logs --tail=15 xxx-xxxxxxx--container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                update.message.reply_text("There was an error when buying the logs.")
        elif logs_command == '/11f1f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = x_machine_host.exec_command("docker logs --tail=5 x-machine-container-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/11f2f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = x_machine_host.exec_command("docker logs --tail=5 x-machine-container-2-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/11f3f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = x_machine_host.exec_command("docker logs --tail=5 x-machine-container-3-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/11f4f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = x_machine_host.exec_command("docker logs --tail=5 x-machine-container-4-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/11f5f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = x_machine_host.exec_command("docker logs --tail=5 x-machine-container-5-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/11f6f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = x_machine_host.exec_command("docker logs --tail=5 x-machine-container-6-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/11f7f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = y_machine_host.exec_command("docker logs --tail=5 x-machine-container-7-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/11f8f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = y_machine_host.exec_command("docker logs --tail=5 x-machine-container-8-container")
                output = ssh_stdout.read().decode('utf-8')11f
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")          
        elif logs_command == '/11f9f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = y_machine_host.exec_command("docker logs --tail=5 x-machine-container-9-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")      
        elif logs_command == '/11f10f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = y_machine_host.exec_command("docker logs --tail=5 x-machine-container-10-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")  
        elif logs_command == '/11f11f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = y_machine_host.exec_command("docker logs --tail=5 x-machine-container-11-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/11f12f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = y_machine_host.exec_command("docker logs --tail=5 x-machine-container-12-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")            
        elif logs_command == '/22ff1f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = x_machine_host.exec_command("docker logs --tail=5 xxx-xxx-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/22ff2f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = x_machine_host.exec_command("docker logs --tail=5 xxx-xxx-2-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/22ff3f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = x_machine_host.exec_command("docker logs --tail=5 xxx-xxx-3-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/22ff4f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = y_machine_host.exec_command("docker logs --tail=5 xxx-xxx-4-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/22ff5f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = y_machine_host.exec_command("docker logs --tail=5 xxx-xxx-5-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        elif logs_command == '/22ff6f':
            try:
                ssh_stin,ssh_stdout,ssh_stderr = y_machine_host.exec_command("docker logs --tail=5 xxx-xxx-6-container")
                output = ssh_stdout.read().decode('utf-8')
                context.bot.send_message(chat_id=update.message.chat_id, text=output)
            except paramiko.SSHException:
                context.bot.send_message("There was an error when buying the logs.")
        ssh.close()

# weather
weather_dict = {
    "Clear": "Açık",
    "Clouds": "Bulutlu",
    "Rain": "Yağmurlu",
    "Snow": "Karlı",
    # ...
}        
# weather       
def weather(update, context):
        LATITUDE = xx.xxx 
        LONGITUDE = xx.xxx
        #openweather
        API_KEY = 'your weather apı key'
        user_name = update.effective_user.name
        update.effective_message.reply_text("waiting" + user_name)
        # API'ye istek 
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric&lang=tr')
        data = response.json()

        # API'den dönen hava durumu 
        weather_description = data['weather'][0]['description']
        custom_description = weather_dict.get(weather_description, weather_description)
        message = f" {data['main']['temp']} °C\nHava durumu: {custom_description}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        now = datetime.datetime.now()
        five_hours_later = now + datetime.timedelta(hours=2)
        timestamp = str(int(five_hours_later.timestamp()))
        response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric&lang=tr&dt={timestamp}')
        data = response.json()
        weather_description = data['list'][0]['weather'][0]['description']
        custom_description = weather_dict.get(weather_description, weather_description)
        message = f"EXPECTED AFTER 2 HOURS: {custom_description}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return "fail"
    
#screenshot
def gui_screenshot(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        user_name = update.effective_user.name
        update.effective_message.reply_text("Gui screenshot is taken .. Please wait. " + user_name)
        try:
            ssh = ssh_info()
            command = "export DISPLAY=:1 && scrot screenshot.png"
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            time.sleep(5)
            
            sftp = ssh.open_sftp()
            remote_path = "/home/username/screenshot.png"
            local_path = os.path.join(os.getcwd(), "screenshot.png")
            sftp.get(remote_path, local_path)
            sftp.close()
            ssh.close()

            with open(local_path, 'rb') as f:
                update.effective_message.reply_document(document=f)

            os.remove(local_path)

        except (paramiko.SSHException, paramiko.AuthenticationException) as e:
            error_message = "your messageHata: {}".format(str(e))
            update.effective_message.reply_text(text=error_message)
    else:
        query.answer("Unauthorized access!")    
        

def scrpt_logs(update, context): # burası , olası bir komut öncesi containerlerin durumunu almak için log üretilecek yer . 
    
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        if update.effective_message is None:
            chat_id = update.effective_chat.id
        else:
            chat_id = update.effective_message.chat_id

        query = update.callback_query
        query.answer()

        callback_data = query.data
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time, query.data)

        ssh = ssh_info()

        if callback_data == 'gui_all_packages_restart':
            # Extract file name and directory path from the callback data
                 
            current_date = datetime.datetime.now().strftime("%m%d")
            file_name = f"guilogs{current_date}.txt"
            file_path = f"~/Desktop/yourpc/yourdirectory/logs/{file_name}"

            # Execute SSH command to generate log file
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"docker logs --timestamps --tail 200 xxx-xxxxxxx-gui-container > {file_path}")
            time.sleep(5)
                        # Extract file name and directory path from the callback data
            current_date = datetime.datetime.now().strftime("%m%d")
            file_name = f"postgrelog{current_date}.txt"
            file_path = f"~/Desktop/yourpc/yourdirectory/logs/{file_name}"

            # Execute SSH command to generate log file
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"docker logs --timestamps --tail 200 xx-postgres > {file_path}")
            time.sleep(5)

            current_date = datetime.datetime.now().strftime("%m%d")
            file_name = f"Dü{current_date}.txt"
            file_path = f"~/Desktop/yourpc/yourdirectory/logs/{file_name}"

            # Execute SSH command to generate log file
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"docker logs --timestamps --tail 200 xxx-xxxxxxx-test-unit-container > {file_path}")
            time.sleep(5)

            current_date = datetime.datetime.now().strftime("%m%d")
            file_name = f"mmh{current_date}.txt"
            file_path = f"~/Desktop/yourpc/yourdirectory/logs/{file_name}"

            # Execute SSH command to generate log file
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"docker logs --timestamps --tail 200 xxx-xxxxxxx-mmh-container > {file_path}")
            time.sleep(5)
            
# docker stats         
def docker_stats(update, context):
    
    query = update.callback_query
    user_id = update.effective_user.id
    
    if is_authorized(user_id):
        user_name = update.effective_user.name
        update.effective_message.reply_text("waiting  " + user_name)
        try:
            ssh = ssh_info()
            command = "docker stats --no-stream --format 'table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}'"
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            output = ssh_stdout.read().decode()
            update.effective_message.reply_text(text=output)
            tlgram_zlk_graphicversionv02.start(update,context)
        except (paramiko.SSHException, paramiko.AuthenticationException) as e:
            error_message = "error,: {}".format(str(e))
            update.effective_message.reply_text(text=error_message)
    else:
        query.answer("Unauthorized access!")
 
# def xx_htop(update,context):
#     query = update.callback_query
#     user_id = update.effective_user.id
    
#     if is_authorized(user_id):
#         user_name = update.effective_user.name
#         update.effective_message.reply_text("waiting " + user_name)
#         try:
#             ssh = ssh_info()
#             command = "htop"
#             ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
#             output = ssh_stdout.read().decode()
#             update.effective_message.reply_text(text=output)


#         except (paramiko.SSHException, paramiko.AuthenticationException) as e:

#             error_message = "error: {}".format(str(e))
#             update.effective_message.reply_text(text=error_message)
#         ssh.close()
#     else:
#         query.answer("Unauthorized access!")    