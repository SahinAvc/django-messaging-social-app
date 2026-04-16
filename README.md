# 💬 Django Social Messaging App

A web-based social messaging application built with Django.  
Users can send friend requests, manage friendships, and chat privately with accepted friends.

---

## 🚀 Project Overview

This project simulates a basic social media messaging system similar to Instagram DM or Facebook Messenger.

Users can:
- Create an account and log in
- Send and receive friend requests
- Accept or reject friend requests
- Chat only with accepted friends
- Delete their own messages
- View sent and received messages separately
- Manage everything through a simple admin panel

---

## ✨ Features

### 👤 Authentication System
- User registration (signup)
- Login / Logout system
- Protected pages with login required

---

### 👥 Friend System
- Send friend requests to users
- Accept or reject incoming requests
- Remove existing friends
- Only accepted friends can chat

---

### 💬 Messaging System
- Private messaging between friends only
- Messages stored with sender and receiver info
- Sent and received messages displayed separately
- Message timestamps (created_at)
- Delete own messages

---

### 🛠 Admin Panel
- View all users
- Manage messages
- Manage friend requests
- Delete any data if needed

---

## 🧱 Tech Stack

- Python 3
- Django 6
- SQLite (database)
- Bootstrap 5 (frontend)
- HTML / CSS

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/SahinAvc/django-messaging-social-app.git
cd django-messaging-social-app
