# ERPNext Law UI

Custom UI layer for ERPNext Law Office Management System.

This app customizes the ERPNext interface for legal offices while keeping core ERPNext/Frappe code untouched.

## Implemented (Issue 1)

- Branded custom login template
- Login page styling for law office identity
- Lightweight login JavaScript enhancements
- Frontend asset registration in `hooks.py`

## Project Structure

```text
erpnext_law_ui/
├─ erpnext_law_ui/
│  ├─ __init__.py
│  ├─ hooks.py
│  ├─ templates/
│  │  └─ login.html
│  └─ public/
│     ├─ css/
│     │  └─ login.css
│     ├─ js/
│     │  └─ login.js
│     └─ images/
├─ AGENTS.md
└─ README.md
```

## Installation

```bash
bench get-app https://github.com/alhaditraining/erpnext_law_ui
bench --site yoursite install-app erpnext_law_ui
```
