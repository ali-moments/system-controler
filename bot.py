from telegram.ext import Updater,CommandHandler
import subprocess

updater = Updater("TOKEN",use_context = True)

def start_method(update,context):
    context.bot.sendMessage(update.message.chat_id,"Connected !")

def run_command(update,context):
    command = ""
    for i in context.args:
        command += i+" "
    print(str(update.message.chat_id)+" : "+command)
    proc = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    command_result = proc.stdout.read() + proc.stderr.read()
    context.bot.sendMessage(update.message.chat_id,command_result.decode())

updater.dispatcher.add_handler(CommandHandler("start",start_method))
updater.dispatcher.add_handler(CommandHandler("run",run_command))

updater.start_polling()
