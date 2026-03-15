# AGENTS.md

## Project Overview

This repository contains a **custom UI application for ERPNext** used in a **Law Office Management System**.

The goal of this project is to **customize the ERPNext user interface without modifying the core framework**.
All UI customization must remain inside this application to ensure the system remains **upgrade-safe and maintainable**.

**Tech Stack**

* ERPNext
* Frappe Framework
* Python
* CSS
* JavaScript

---

## Important Rules

1. **Do NOT modify Frappe or ERPNext core code.**
   All modifications must remain inside this repository.

2. **UI customization must only exist inside this app (`erpnext_law_ui`).**

3. **Business logic must NOT be implemented in this repository.**
   Business logic belongs in the separate application:

   ```
   erpnext_law_management
   ```

4. Follow **Frappe coding standards and conventions**.

5. Keep changes **modular, minimal, and maintainable**.

---

## Repository Structure

```
erpnext_law_ui
│
├─ erpnext_law_ui
│   ├─ hooks.py
│   │
│   ├─ templates
│   │   └─ login.html
│   │
│   └─ public
│       ├─ css
│       │   └─ login.css
│       │
│       ├─ js
│       │
│       └─ images
│
├─ README.md
├─ AGENTS.md
└─ .gitignore
```

---

## Responsibilities of This App

This application is responsible for **UI and frontend customization only**.

Examples include:

* Custom login page
* ERPNext branding
* UI styling and theme
* CSS customization
* Frontend JavaScript
* Dashboard layout improvements
* UI components for the desk interface

---

## Responsibilities of Other Apps

The following features **must NOT be implemented here**:

* Legal services logic
* Case management logic
* Client workflows
* Financial calculations
* Backend business rules

These belong in:

```
erpnext_law_management
```

---

## Development Guidelines

When adding or modifying features:

### CSS Files

Place styles in:

```
erpnext_law_ui/public/css
```

Example:

```
login.css
theme.css
dashboard.css
```

---

### JavaScript Files

Place scripts in:

```
erpnext_law_ui/public/js
```

Example:

```
login.js
dashboard.js
```

---

### HTML Templates

Place templates in:

```
erpnext_law_ui/templates
```

Example:

```
login.html
dashboard.html
```

---

### Register Assets

All frontend assets must be registered in:

```
hooks.py
```

Example:

```python
app_include_css = "/assets/erpnext_law_ui/css/login.css"
app_include_js = "/assets/erpnext_law_ui/js/login.js"
```

---

## Design Goals

This project aims to provide a **clean UI layer for ERPNext** while keeping the system:

* Upgrade-safe
* Modular
* Maintainable
* Compatible with future ERPNext updates
* Easy for both developers and AI agents to extend

---

## Summary

* This repository = **UI layer**
* Business logic lives in **erpnext_law_management**
* Never modify **Frappe or ERPNext core**
* Follow **Frappe conventions**
* Keep UI changes organized and modular
