from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler,CommandHandler
import func
import telegram.ext
from telegram.ext import Updater, CommandHandler


user_menu = {}


def is_authorized(user_id):
    authorized_users = [] #permissible user telegram ids
    return user_id in authorized_users


def start(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        button_list = [
            [InlineKeyboardButton("test button", callback_data='test button'),InlineKeyboardButton("Gui test button", callback_data='test button')],
            [InlineKeyboardButton("test button", callback_data='test button'),InlineKeyboardButton("test button", callback_data='test button')],
            [InlineKeyboardButton("test button", callback_data='test button'),InlineKeyboardButton("test button", callback_data='test button')],
            [InlineKeyboardButton("test button", callback_data='test button')],
            [InlineKeyboardButton("test button", callback_data='test button')],
        ]
        reply_markup = InlineKeyboardMarkup(button_list)
        if update.callback_query:
            if query.message.text == "Please select Menu:":
                return

            update.callback_query.edit_message_text(text="Lütfen yapılacak işlem  menüsünü seçin:", reply_markup=reply_markup)
        else:
            update.effective_message.reply_text("Lütfen yapılacak işlem  menüsünü seçin:", reply_markup=reply_markup)
    else:
        update.effective_message.reply_text("Bu komutu kullanma izniniz yok.")
        return "fail"
            

def pcp_process_menu(update, context):
        query = update.callback_query
        user_id = update.effective_user.id

        if is_authorized(user_id):
            button_list = [
                [InlineKeyboardButton("All Visible Start", callback_data='visible_containers_start'),InlineKeyboardButton("All Termal Start", callback_data='termal_containers_start')],
                [InlineKeyboardButton("All Visible Restart", callback_data='visible_containers_restart'),InlineKeyboardButton("All Termal Restart", callback_data='termal_containers_restart')],
                [InlineKeyboardButton("All Visible Stop", callback_data='visible_containers_stop'),InlineKeyboardButton("All Termal Stop", callback_data='termal_containers_stop')],

                [InlineKeyboardButton("Docker PS", callback_data='pcpdockerps')],
                [InlineKeyboardButton("Geri", callback_data='start')],
                
                
            ]
            reply_markup = InlineKeyboardMarkup(button_list)
            user_menu[update.effective_chat.id] = 'pcp_process_menu'  
            update.callback_query.edit_message_text(text="KD Kamera Menüsü.", reply_markup=reply_markup)
        else:
            query.answer("Yetkisiz erişim!")

def gui_process_menu(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        button_list = [
            [InlineKeyboardButton("Gui Start", callback_data='gui_docker_start'), InlineKeyboardButton("Mmh Start", callback_data='mmh_docker_start'), InlineKeyboardButton("Dü Start", callback_data='dü_docker_start'), InlineKeyboardButton("C.Server Start", callback_data='cs_docker_start')],
            [InlineKeyboardButton("Gui Stop", callback_data='gui_docker_stop'), InlineKeyboardButton("Mmh Stop", callback_data='mmh_docker_stop'), InlineKeyboardButton("Dü Stop", callback_data='dü_docker_stop'), InlineKeyboardButton("C.Server Stop", callback_data='cs_docker_stop')],
            [InlineKeyboardButton("Gui Restart", callback_data='gui_docker_restart'), InlineKeyboardButton("Mmh Restart", callback_data='start'), InlineKeyboardButton("Dü Restart", callback_data='dü_docker_restart'), InlineKeyboardButton("C.Server Restart", callback_data='cs_docker_restart')],
            
            [InlineKeyboardButton("Diğer İşlemler", callback_data='gui_other_action'),InlineKeyboardButton("Gui Docker PS", callback_data='guidockerps')],
            [InlineKeyboardButton("Geri", callback_data='start')],
            
        ]
        reply_markup = InlineKeyboardMarkup(button_list)
        user_menu[update.effective_chat.id] = 'gui_process_menu' 
        update.callback_query.edit_message_text(text="Gui Server Process", reply_markup=reply_markup)
    else:
        query.answer("Yetkisiz erişim!")
        

def kgag_log_actions(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        button_list = [
            [InlineKeyboardButton("Gui 24h Logs", callback_data='gui_24h_logs'), InlineKeyboardButton("Mmh 24h Logs", callback_data='mmh_24h_logs'),InlineKeyboardButton("Dü 24h Logs", callback_data='du_24h_logs')],
            [InlineKeyboardButton("Gui --tail 10 F", callback_data='gui_tail_f'), InlineKeyboardButton("Mmh --tail 10 F", callback_data='mmh_tail_f'),InlineKeyboardButton("Dü --tail 10 F", callback_data='du_tail_f')],
            [InlineKeyboardButton("Journal Logs", callback_data='journal_24h_logs'),InlineKeyboardButton("Journal --tail 10 F", callback_data='start'), InlineKeyboardButton("Null Button", callback_data='start')],

            [InlineKeyboardButton("Geri Dön", callback_data='start')],
            
        ]
        reply_markup = InlineKeyboardMarkup(button_list)
        user_menu[update.effective_chat.id] = 'kgag_log_actions'  
        update.callback_query.edit_message_text(text="Logs Menu", reply_markup=reply_markup)
    else:
        query.answer("Yetkisiz erişim!")
# # Menü 4
# def temp_control(update, context):
#     button_list = [
#         [InlineKeyboardButton("Kontrol", callback_data='temp_control')]
#         [InlineKeyboardButton("Geri", callback_data='start')]
#     ]
#     reply_markup = InlineKeyboardMarkup(button_list)
#     user_menu[update.effective_chat.id] = 'temp_control'  # Kullanıcının mevcut menüsünü güncelle
#     update.callback_query.edit_message_text(text="İşlem seçiniz.", reply_markup=reply_markup)

# Diğer İşlem


def gui_other_action(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        button_list = [
            [InlineKeyboardButton("Herşeyi Durdur", callback_data='gui_all_packages_stop'), InlineKeyboardButton("Roudi Start", callback_data='roudi_docker_start'),InlineKeyboardButton("Postgre Start", callback_data='postgre_docker_start')],
            [InlineKeyboardButton("Herşeyi Başlat", callback_data='gui_all_packages_restart'), InlineKeyboardButton("Roudi Stop", callback_data='roudi_docker_stop'),InlineKeyboardButton("Postgre Stop", callback_data='postgre_docker_stop')],
            [InlineKeyboardButton("Gui Packages", callback_data='gui_all_packages_postgre'),InlineKeyboardButton("Roudi Restart", callback_data='roudi_docker_restart'), InlineKeyboardButton("Postgre Restart", callback_data='postgre_docker_restart')],

            [InlineKeyboardButton("Geri Dön", callback_data='gui_process_menu')],
            
        ]
        reply_markup = InlineKeyboardMarkup(button_list)
        user_menu[update.effective_chat.id] = 'gui_other_action'  # Kullanıcının mevcut menüsünü güncelle
        update.callback_query.edit_message_text(text="Diğer Gui İşlemleri", reply_markup=reply_markup)
    else:
        query.answer("Yetkisiz erişim!")

# Callback fonksiyonu
def button_click(update, context):
    query = update.callback_query
    user_id = update.effective_user.id

    if is_authorized(user_id):
        if query.data == 'start':
            start(update, context)
        elif query.data == 'pcp_process_menu':
            pcp_process_menu(update, context)
        elif query.data == 'gui_process_menu':#Gui button menü
            gui_process_menu(update, context)
        elif query.data == 'guidockerps': #Gui Docker PS
            func.guidockerps(update, context)
        elif query.data == 'gui_docker_start':
            func.gui_docker_process(update, context)#GUi Docker Controller
        elif query.data == 'gui_docker_stop':
            func.gui_docker_process(update, context)#GUi Docker Controller
        elif query.data == 'gui_docker_restart':
            func.gui_docker_process(update, context)#GUi Docker Controller
        elif query.data == 'mmh_docker_start':
            func.gui_docker_process(update, context)#Mmh Docker Controller
        elif query.data == 'mmh_docker_stop':
            func.gui_docker_process(update, context)#Mmh Docker Controller
        elif query.data == 'mmh_docker_restart':
            func.gui_docker_process(update, context)#Mmh Docker Controller
        elif query.data == 'dü_docker_start':
            func.gui_docker_process(update, context)#Dü Docker Controller
        elif query.data == 'dü_docker_stop':
            func.gui_docker_process(update, context)#Dü Docker Controller
        elif query.data == 'dü_docker_restart':
            func.gui_docker_process(update, context)#Dü Docker Controller
        elif query.data == 'cs_docker_start':
            func.gui_docker_process(update, context)#Configserver Docker Controller
        elif query.data == 'cs_docker_stop':
            func.gui_docker_process(update, context)#Configserver Docker Controller
        elif query.data == 'cs_docker_restart':
            func.gui_docker_process(update, context)#Configserver Docker Controller
        elif query.data == 'roudi_docker_start':
            func.gui_docker_process(update, context)#Roudi Docker Controller
        elif query.data == 'roudi_docker_stop':
            func.gui_docker_process(update, context)#Roudi Docker Controller
        elif query.data == 'roudi_docker_restart':
            func.gui_docker_process(update, context)#Roudi Docker Controller
        elif query.data == 'postgre_docker_start':
            func.gui_docker_process(update, context)#postgre Docker Controller
        elif query.data == 'postgre_docker_stop':
            func.gui_docker_process(update, context)#Postgre Docker Controller
        elif query.data == 'postgre_docker_restart':
            func.gui_docker_process(update, context)#Postgre Docker Controller
        elif query.data == 'gui_all_packages_stop':
            func.gui_docker_process(update, context)#Gui All Container Restart
        elif query.data == 'gui_all_packages_restart':
            func.scrpt_logs(update,context)
            func.gui_docker_process(update, context)#Gui All Container Restart        
        elif query.data == 'gui_all_packages_postgre':
            func.gui_docker_process(update, context)#Gui All Container Postgre hatası düzelince kaldırılacak.                                 
        elif query.data == 'kgag_log_actions': # logs menü
            kgag_log_actions(update, context)
        elif query.data == 'gui_24h_logs': # logs menü
            func.kgag_logs(update, context)
        elif query.data == 'gui_tail_f': # logs menü -f
            func.kgag_logs(update, context)
        elif query.data == 'mmh_24h_logs': # logs menü -f
            func.kgag_logs(update, context)
        elif query.data == 'mmh_tail_f': # logs menü -f
            func.kgag_logs(update, context)
        elif query.data == 'du_24h_logs': # logs menü -f
            func.kgag_logs(update, context)
        elif query.data == 'du_tail_f': # logs menü -f
            func.kgag_logs(update, context)
        elif query.data == 'journal_24h_logs': # logs menü -f
            func.kgag_logs(update, context)
        # elif query.data == 'temp_control':
        #     temp_control(update, context)
        elif query.data == 'temp_control':
            func.temperature_control(update, context)
        elif query.data == 'weather':
            func.weather(update, context)
        elif query.data == 'go_back_gui_menu':
            gui_process_menu(update, context)
        elif query.data == 'connection_test':  #connection test 
            func.connection_test(update, context)
        elif query.data == 'visible_containers_stop':# Visible Process
            func.visible_containers_stop(update, context)  
        elif query.data == 'visible_containers_start':# Visible Process
            func.visible_containers_start(update, context)
        elif query.data == 'visible_containers_restart':# Visible Process
            func.visible_containers_restart(update, context)
        elif query.data == 'pcpdockerps':# Pcp Docker ps
            func.pcpdockerps(update, context)
        elif query.data == 'termal_containers_start': # Termal Process
            func.termal_containers_start(update, context)  
        elif query.data == 'termal_containers_stop':# Termal Process
            func.termal_containers_stop(update, context)
        elif query.data == 'termal_containers_restart':# Termal Process
            func.termal_containers_restart(update, context)    
        elif query.data == 'gui_other_action':
            gui_other_action(update, context)
        elif query.data == 'screenshot_action':
            func.gui_screenshot(update, context)  
        elif query.data == 'dockerstats':
            func.docker_stats(update, context)
            start(update,context)      
    else:
        query.answer("Yetkisiz erişim!")            


    
def main():
    updater = Updater(token='5872046057:AAFfKqrQNGm895I7Zp7MagMGYo7-Sm37pEM', use_context=True)  # Bot API 
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CallbackQueryHandler(button_click))
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('power', func.power_control))    
    dispatcher.add_handler(CommandHandler('visible1f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible2f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible3f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible4f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible5f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible6f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible7f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible8f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible9f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible10f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible11f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('visible12f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('termal1f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('termal2f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('termal3f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('termal4f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('termal5f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('termal6f', func.logs_monitor))
    dispatcher.add_handler(CommandHandler('dockerstats', func.docker_stats))
    dispatcher.add_handler(CommandHandler('htop', func.kgag_htop))

    updater.start_polling()



        

if __name__ == '__main__':
    main()