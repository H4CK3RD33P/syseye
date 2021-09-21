import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent, sensors_temperatures, virtual_memory
import smtplib
from email.message import EmailMessage
import mimetypes