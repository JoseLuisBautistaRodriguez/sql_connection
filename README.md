# How to Install and Use MySQLdb (mysqlclient) on WSL with Python in VS Code

> by José Luis Bautista Ridríguez [jlbaur.lat](http://jlbaur.lat/content/posts/Visual_Studio_Entornos_Virtuales_con_WSL.html)

> [!CAUTION]
> Project about a WSL work environment on Visual Studio Code.

Below is a step-by-step guide to install and configure `MySQLdb`—typically installed via the `mysqlclient` package—when working under Windows Subsystem for Linux (WSL) in Visual Studio Code.


## Prerequisites

- **WSL** installed on your Windows system.  
- **VS Code** with the **Remote - WSL** extension (optional but recommended if you want to open and run your project directly in WSL).  
- **Python 3** installed within WSL (e.g., `sudo apt-get install python3 python3-pip`).

## 1. Install Required System Packages

Inside your WSL terminal (Ubuntu or any other distro), run:
```bash
sudo apt-get update
sudo apt-get install python3-dev libmysqlclient-dev
```
- `python3-dev` provides header files needed for building Python modules.
- `libmysqlclient-dev` provides the development files needed for MySQL client libraries.

## 2. Create (Optional) a Virtual Environment

It is a good practice to use a virtual environment for your Python project. In your WSL terminal, navigate to your project folder and run:
```bash
python3 -m venv venv
source venv/bin/activate
```
Your shell prompt should now reflect that you are in a virtual environment (e.g., `(venv)` prefix).

## 3. Install the `mysqlclient` Package

Once you have your environment ready (or even in the global environment, if preferred):
```bash
pip install mysqlclient
```
This package contains the **MySQLdb** module needed to connect to MySQL databases in Python.

## 4. Configure Your MySQL Server

If you are using **XAMPP** on Windows, make sure:
- Your MySQL server is running.
- You know the port (commonly 3306 or 3300) and the host IP that WSL can access (e.g., `172.x.x.x`).
- You have a valid user/password set up in MySQL.

## 5. Update Your Python Script

In your Python script, ensure you import `MySQLdb` and specify the correct connection details:
```python
import MySQLdb

db = MySQLdb.connect(
    host="172.19.224.1",  # Example IP from Windows to WSL
    port=3300,           # Or 3306, depending on your setup
    user="YOUR_USERNAME",
    passwd="YOUR_PASSWORD"
)
```
Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your actual credentials. Also verify the port number matches your MySQL configuration.

## 6. Test Your Connection

Run your script from within the WSL terminal:
```bash
python your_script.py
```
If the connection succeeds, you should see a message indicating successful connection, plus the list of available databases.

## 7. Troubleshooting

- **Connection Refused**: Check if MySQL is running and confirm the port is open and accessible from WSL.  
- **Incorrect Credentials**: Double-check the user/password.  
- **Environment Issues**: Make sure you installed `mysqlclient` inside the same Python environment where you are running the script.

---

### Example Commands Recap

```bash
# 1. Update and install dependencies
sudo apt-get update
sudo apt-get install python3-dev libmysqlclient-dev

# 2. (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install mysqlclient
pip install mysqlclient

# 4. Run your Python script
python your_script.py
```
---

**That’s it!** You now have a fully configured Python environment on WSL, ready to interact with MySQL using `MySQLdb` (via `mysqlclient`).
