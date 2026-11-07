# 📈 Stock Portfolio Tracker

A robust, command-line Python application designed to simulate stock market investments. Users can build a custom portfolio, calculate real-time investment values, and export their financial data to a clean, Excel-compatible CSV file.

This project demonstrates strong fundamentals in Python programming, modular software architecture, and data handling.

## ✨ Key Features

- **Modular Architecture:** Code is strictly separated into Data, Input, Logic, and Output layers for high maintainability.
- **Robust Input Validation:** Gracefully handles invalid stock symbols, negative quantities, and non-integer inputs without crashing.
- **Clean Data Export:** Utilizes Python's built-in `csv` module to generate perfectly formatted, cross-platform compatible CSV files.
- **Interactive CLI:** Provides a clean, user-friendly terminal interface with real-time feedback.

## 🛠️ Tech Stack & Concepts

- **Language:** Python 3.x
- **Libraries:** Built-in `csv` module (No external dependencies required)
- **Core Concepts:** 
  - Modular Programming (Function-based architecture)
  - Data Structures (Dictionaries, Lists of Dictionaries)
  - File I/O Operations (Read/Write CSV)
  - Exception Handling (`try/except` blocks)

## 🏗️ Project Architecture

To ensure clean and scalable code, the application follows a **Separation of Concerns** design pattern:

| Module / Function | Responsibility |
| :--- | :--- |
| `get_stock_prices()` | **Data Layer:** Manages the hardcoded market data. |
| `get_user_input()` | **UI Layer:** Handles user interaction and input validation. |
| `calculate_totals()` | **Logic Layer:** Processes business logic and arithmetic. |
| `display_and_save()` | **Output Layer:** Manages terminal UI and file I/O operations. |

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher installed on your machine.

### Installation & Execution
1. Clone this repository or download the `stock_tracker.py` file.
2. Open your terminal or command prompt.
3. Navigate to the project directory.
4. Run the script:
   ```bash
   python stock_tracker.py






   