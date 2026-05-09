# ☕ Canelinha Cafe — Self-Service Ordering System

Interactive coffee ordering project with two interfaces:

- **Python CLI app** (`cafe.py`) for terminal-based ordering.
- **Web kiosk UI** (`index.html`) inspired by the same flow.

---

## 📋 Project Overview

**Canelinha Cafe** simulates a self-service kiosk where customers can:

- Browse the coffee menu and stock
- Add or remove items from a cart
- Register/login to activate a discount
- Validate CPF during registration
- Finish an order with a final summary

---

## ✨ Current Features

### CLI (`cafe.py`)

- Customer greeting and interactive menu loop
- Product catalog with **price + stock control**
- Cart management (add, view, remove)
- User registration/login with CPF validation
- 10% discount for authenticated customers
- Admin login with stock/price management tools

### Web UI (`index.html`)

- Responsive digital kiosk layout
- Visual menu cards with quantity inputs
- Real-time cart summary and totals
- Registration/login forms with discount state
- English and Portuguese (Brazil) language toggle

---

## 🧩 Repository Structure

```text
.
├── cafe.py      # Terminal application
├── index.html   # Web kiosk interface
└── README.md
```

---

## 🚀 How to Run

### 1) Terminal version

**Requirements:** Python 3

```bash
python cafe.py
```

### 2) Web version

Open `index.html` in any modern browser.

If you prefer a local server:

```bash
python -m http.server 8000
```

Then visit: `http://localhost:8000`

---

## 🔐 Discount and CPF Logic

- Registration requires a valid CPF (check digits are validated).
- Successful registration enables the 10% discount.
- Returning users can log in to reactivate discount mode.

---

## 🛠️ Tech Stack

- **Python 3** (CLI logic)
- **HTML/CSS/JavaScript** (web interface)

---

## 🤝 Contributing

Contributions are welcome via issues and pull requests.

Suggested improvements:

- Persist users/orders in a database
- Add automated tests
- Separate CLI logic into reusable modules
- Add a backend API for the web UI

---

> “The best coffee shop in town since 1980.” — Canelinha Cafe ☕
