# File_Interceptor


# Whitebeard's File Interceptor 💀⚡

A **real-time file monitoring tool** designed for **offensive and defensive security**. Inspired by **Whitebeard from One Piece**, this interceptor **watches, logs, and reports** all file activities in a specified directory.

---

## 💀 Features
- **Real-time File Monitoring** 🛡️
- **Monitors ALL file events** (create, delete, modify, move, etc.) 🔥
- **Recursive Directory Watching** 📂
- **Auto-Detects New Directories** ⚙️
- **Logs Events with Timestamps** 🕒
- **Dark-Hacker Themed Console Output** 🏴‍☠️

---

## ⚡ Installation
### **1️⃣ Install Dependencies**
```bash
pip install pyinotify
```

### **2️⃣ Run the Interceptor**
```bash
sudo python3 file_interceptor.py
```

### **3️⃣ Monitor File Events in Real-Time**
- Create, delete, modify, or move files in the monitored directory.
- The events will be **logged in real-time**.
- All logs are saved in **file_interceptor.log**.

---

## 🛠️ Configuration
- The default monitored directory is **/home**.
- To change the directory, edit the **start_monitoring()** function:
```python
start_monitoring("/your/directory/path")
```
- Run the script with **sudo** to monitor system-critical directories.

---

## 📜 Log Format
Logs are stored in `file_interceptor.log` with the following format:
```plaintext
[YYYY-MM-DD HH:MM:SS] [EVENT TYPE] File Path
```
Example:
```plaintext
[2025-03-06 12:34:56] [+] File Created: /home/user/Desktop/secret.txt
[2025-03-06 12:35:02] [!] File Modified: /home/user/Desktop/secret.txt
[2025-03-06 12:35:10] [-] File Deleted: /home/user/Desktop/secret.txt
```

---

## 🔥 Why Use Whitebeard's File Interceptor?
✅ **Zero Setup Required** – Just run and it works.
✅ **Handles Everything** – You don’t miss a single file event.
✅ **Recursive & Auto-Update** – Even new directories are covered.
✅ **Fast & Efficient** – Uses `pyinotify` for near-instant alerts.
✅ **Hacker Vibes** – Dark-themed logs & pirate energy. 🏴‍☠️

---

## 💀 ASCII Art (Whitebeard Skull)
```plaintext
        ______
     .-'      `-.
    /            \
   |              |
   |,  .-.  .-.  ,|
   | )(_o/  \o_)( |
   |/     /\     \|
   (_     ^^     _)
    \__|IIIIII|__/
     | \IIIIII/ |
     \          /
      `--------`
   ⚡ Whitebeard’s File Interceptor ⚡
```

---

## 📜 License
This tool is open-source and available for **educational & ethical hacking purposes**. Do not use it for malicious activities.

---

**🏴‍☠️ Now, you’re running a File Interceptor worthy of Whitebeard’s crew!** 💀⚡

