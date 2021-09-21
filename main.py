import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent, sensors_temperatures, virtual_memory
import smtplib
from email.message import EmailMessage
import mimetypes
import os

def create_and_send_email(recipient,subject,content,attachment=None):
    sender = 'putyouremail@gmail.com'
    password = 'putyourpassword'
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.login(sender,password)

    email = EmailMessage()
    email['To'] = recipient
    email['From'] = sender
    email['Subject'] = subject
    email.set_content(content)

    if attachment is not None:
        filename = os.path.basename(attachment)
        mime_full_type,_ = mimetypes.guess_type(attachment)
        mime_type,sub_type = mime_full_type.split('/')
        with open(attachment,'rb') as attached_file:
            email.add_attachment(attached_file.read(),
                                maintype=mime_type,
                                subtype= sub_type,
                                filename=filename)

    mail_server.send_message(email)
    mail_server.quit()

cpuy = []
tempy = []
virty = []

def cpu_usage(i):
    percent = cpu_percent()
    cpuy.append(percent)
    plt.plot(cpuy, 'r', label='hello')
    ax = plt.gca()
    ax.set_xticklabels([])
    plt.tight_layout()

red = FuncAnimation( plt.gcf(), cpu_usage, interval = 100)

def cpu_temperature(i):
    percent = sensors_temperatures()['coretemp'][1][1]
    tempy.append(percent)
    plt.plot(tempy, 'b', label='hello')
    ax = plt.gca()
    ax.set_xticklabels([])
    plt.tight_layout()

blue = FuncAnimation( plt.gcf(), cpu_temperature, interval = 100)

def ram_usage(i):
    percent = list(virtual_memory())[2]
    virty.append(percent)
    plt.plot(virty, 'y', label='hello')
    ax = plt.gca()
    ax.set_xticklabels([])
    plt.tight_layout()

yellow = FuncAnimation( plt.gcf(), ram_usage, interval = 100)

plt.title("BLUE -> CPU Temperature \n RED -> CPU Usage \n YELLOW ->  RAM Usage")
plt.show()