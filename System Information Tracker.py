import tkinter as tk
from tkinter import scrolledtext
import psutil
import platform
from datetime import datetime

def get_size(bytes, suffix="B"):
    """
    Verilen bayt cinsinden boyutu daha anlaşılır bir biçimde, uygun birimle döndürür.
    E.g.:
        1253656 bytes => '1.20MB'
        1253656678 bytes => '1.17GB'
    Args:
        bytes (int): Dönüştürülecek bayt miktarı.
        suffix (str): Dönüşen birim sonrası kullanılacak olan birim kısaltması (varsayılan "B").
    Returns:
        str: İnsanlar tarafından daha kolay okunabilir biçimde formatlanmış boyut.
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def system_info():
    """
    Sistem bilgilerini toplayarak tek bir metin stringi olarak döndürür. Toplanan bilgiler arasında işletim sistemi,
    işlemci, bellek ve disk kullanımı bilgileri bulunur.
    Returns:
        str: Sistem bilgilerini içeren detaylı metin.
    """
    info = ""
    uname = platform.uname()
    info += f"System: {uname.system}\n"
    info += f"Node Name: {uname.node}\n"
    info += f"Release: {uname.release}\n"
    info += f"Version: {uname.version}\n"
    info += f"Machine: {uname.machine}\n"
    info += f"Processor: {uname.processor}\n\n"

    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    info += f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n\n"

    # CPU bilgilerini toplar
    info += "CPU Info\n"
    info += f"Physical cores: {psutil.cpu_count(logical=False)}\n"
    info += f"Total cores: {psutil.cpu_count(logical=True)}\n"
    cpu_freq = psutil.cpu_freq()
    info += f"Max Frequency: {cpu_freq.max:.2f}Mhz\n"
    info += f"Min Frequency: {cpu_freq.min:.2f}Mhz\n"
    info += f"Current Frequency: {cpu_freq.current:.2f}Mhz\n"
    info += f"Total CPU Usage: {psutil.cpu_percent()}%\n\n"

    # Bellek kullanım bilgilerini toplar
    svmem = psutil.virtual_memory()
    info += "Memory Information\n"
    info += f"Total: {get_size(svmem.total)}\n"
    info += f"Available: {get_size(svmem.available)}\n"
    info += f"Used: {get_size(svmem.used)}\n"
    info += f"Percentage: {svmem.percent}%\n\n"

    # Disk kullanım bilgilerini toplar
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        info += f"Partition {partition.device}\n"
        info += f"  Total Size: {get_size(partition_usage.total)}\n"
        info += f"  Used: {get_size(partition_usage.used)}\n"
        info += f"  Free: {get_size(partition_usage.free)}\n"
        info += f"  Percentage: {partition_usage.percent}%\n\n"

    return info

def update_text():
    """
    Tkinter GUI'sindeki metin alanını güncel sistem bilgisi ile doldurur. Bu fonksiyon bir butona basıldığında çağrılır.
    """
    info = system_info()
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.INSERT, info)

# GUI başlatılır
root = tk.Tk()
root.title("System Information")

# Ana çerçeve oluşturulur
frame = tk.Frame(root)
frame.pack(pady=20)

# Kaydırılabilir metin alanı eklenir
text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=100, height=25)
text_area.pack(padx=10, pady=10)

# Bilgiyi yenilemek için bir buton eklenir
button = tk.Button(root, text="Refresh Info", command=update_text)
button.pack(pady=20)

# Sistem bilgileri ile GUI metin alanı ilk defa doldurulur
update_text()

# GUI ana döngüsü başlatılır
root.mainloop()
