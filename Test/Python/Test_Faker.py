import requests
import tkinter as tk
from tkinter import messagebox

URL = 'https://jsonplaceholder.typicode.com/users'

def fetch_users(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        users = response.json()
        return users
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return []

def show_user_info(users):
    for user in users:
        message = f"Name: {user['name']}\nEmail: {user['email']}\nAddress: {user['address']['street']}, {user['address']['suite']}, {user['address']['city']}, {user['address']['zipcode']}"
        messagebox.showinfo("User Info", message)

def main():
    users = fetch_users(URL)
    if users:
        show_user_info(users)
    else:
        print("No users found or an error occurred.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  
    main()
