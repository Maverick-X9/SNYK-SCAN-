import os
import pickle
import hashlib
import subprocess
import sqlite3
import requests

# 1. SQL Injection (🚨 Vulnerable)
def sql_injection(user_input):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # 🚨 Vulnerable to SQL Injection
    cursor.execute(query)
    return cursor.fetchall()

# 2. Hardcoded Secret (🚨 Vulnerable)
API_KEY = "123456789abcdef"  # 🚨 Hardcoded API Key

# 3. Command Injection (🚨 Vulnerable)
def command_injection(user_input):
    os.system("echo " + user_input)  # 🚨 User-controlled input in OS command

# 4. Insecure Deserialization (🚨 Vulnerable)
def insecure_deserialization(pickle_data):
    return pickle.loads(pickle_data)  # 🚨 Untrusted deserialization

# 5. Directory Traversal (🚨 Vulnerable)
def directory_traversal(filename):
    with open("/var/www/html/" + filename, "r") as file:  # 🚨 Path traversal risk
        return file.read()

# 6. Cross-Site Scripting (XSS) (🚨 Vulnerable)
def xss(user_input):
    return f"<div>Welcome {user_input}</div>"  # 🚨 User input directly in HTML

# 7. Insecure Hashing (🚨 Vulnerable)
def insecure_hash(password):
    return hashlib.md5(password.encode()).hexdigest()  # 🚨 MD5 is insecure

# 8. Unverified SSL Certificate (🚨 Vulnerable)
def unverified_ssl():
    response = requests.get("https://example.com", verify=False)  # 🚨 SSL verification disabled
    return response.text

# 9. Unrestricted File Upload (🚨 Vulnerable)
def save_file(uploaded_file):
    with open(f"/uploads/{uploaded_file.filename}", "wb") as f:  # 🚨 No validation of file type
        f.write(uploaded_file.read())

# 10. Use of eval() (🚨 Vulnerable)
def dangerous_eval(user_input):
    return eval(user_input)  # 🚨 Allows arbitrary code execution

# 11. Insecure Random Number Generation (🚨 Vulnerable)
import random
def insecure_random():
    return random.random()  # 🚨 Not cryptographically secure

# 12. SSRF (Server-Side Request Forgery) (🚨 Vulnerable)
def ssrf(url):
    response = requests.get(url)  # 🚨 User-controlled request
    return response.text

# 13. Weak JWT Secret (🚨 Vulnerable)
import jwt
def weak_jwt():
    return jwt.encode({"user": "admin"}, "12345", algorithm="HS256")  # 🚨 Weak secret key

# 14. Improper Error Handling (🚨 Vulnerable)
def improper_error_handling():
    try:
        1 / 0
    except Exception as e:
        return str(e)  # 🚨 Leaks exception details

# 15. No Rate Limiting (🚨 Vulnerable)
def no_rate_limiting(user):
    print(f"User {user} accessed the API.")  # 🚨 No limit on API requests
