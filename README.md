# KeyPhantom 👻

**KeyPhantom** is an educational keylogger and clipboard logger written in Python — intended strictly for learning and controlled lab testing. This repository contains a small HTTP server (`server.py`) and the main logger (`KeyPhantom.py`). The project appends logs locally to `credentials.log` by default.

> ⚠️ **Important:** Do not run this software on anyone else's machine without explicit written permission. Use only in a controlled lab environment for educational purposes.

---

## 🔍 Project Overview

* **Purpose:** Demonstrate keystroke and clipboard capture for educational and lab testing only.
* **Language:** Python (3.8+ recommended)
* **Interfaces:** Command-line execution; optional local HTTP server to receive logs.
* **Logs:** `credentials.log` (local file created/appended automatically)

---

## 🚀 Features

* Keystroke capture (educational/demo)
* Clipboard capture
* Optional: Send captured data to a local `server.py` if configured
* Local log storage to `credentials.log`
* Safety & ethics reminder

---


> **Important:** Do NOT commit `credentials.log` to version control. Add it to `.gitignore`.

---

## ⚙️ Prerequisites

* Python 3.8 or newer
* (Optional) `virtualenv` for an isolated environment

---

## 🛠️ Quick Setup

  Clone the repository:

```bash
git clone https://github.com/Uhani007/KeyPhantom.git
cd KeyPhantom
```

---

## 🧰 Usage Notes

* `server.py` is a simple local HTTP receiver; if you configure `KeyPhantom.py` to POST captured data, it can forward logs to the running server.
* For purely local testing, run `KeyPhantom.py` and inspect `credentials.log`.

---

## 🔒 Safety & Ethics

This project is for **educational** and **lab** use only. Unauthorized use on other peoples' devices is illegal and unethical.

If you are using this code for research or demonstrations:

* Always obtain explicit written permission from the device owner.
* Store logs securely and never publish real sensitive data.
* Follow responsible disclosure and ethical guidelines.

---

## 🧹 Suggested `.gitignore
