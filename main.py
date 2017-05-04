import sys
import mailbox
from multiprocessing import Pool
import easygui
import sys




# path = easygui.fileopenbox()

# FIX
# if ubuntu && wayland && ImportError: No module named '_tkinter'
# sudo apt-get install tk-dev tk tcl-dev tcl python3-tk


# put your filename path here
try:
    filename = easygui.fileopenbox()
    mbox = mailbox.mbox(filename)
except AttributeError as e:
    easygui.msgbox("No File Specified - Click 'Exit' To Close App",'No File Specified','Exit')
    sys.exit()


def get_sender(message):
    return message['sender']
"""
with Pool as p:
    senders = p.map(get_sender,mbox)
"""

senders = []

for message in mbox:
    senders.append(get_sender(message))

def write_list_to_file(list:list,filepath):
    with open(filepath, 'a+') as to_write:
        list = map(lambda x: x + "\n", list)
        to_write.writelines(list)
    return True

senders = list(set(senders))

print(senders)
write_list_to_file(senders,'senders.list')