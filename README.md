# Python Learning Journey

A structured collection of Python exercises and projects developed during my progression from basic Python programming to object-oriented programming, data handling and small application development.

This repository documents my learning path through practical exercises, final projects and applied programming challenges.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Project Overview

This repository contains practical Python work developed across different learning stages.

The main goal is to show progression in:

- Python fundamentals
- Functions and modules
- File handling
- CSV processing
- Object-oriented programming
- Abstract classes
- Package organization
- Unit testing
- Jupyter Notebook workflows
- Small application development

---

## Repository Structure

```text
python-learning-journey/
│
├── a1-notebook/
│   └── Python_A1_Miguel_Angel_de_Alba_y_Perez.ipynb
│
├── b1-text-processing/
│   ├── ejb1_x1_main.py
│   ├── ejb1_x1_test.py
│   └── util_package/
│       ├── __init__.py
│       └── text_manager.py
│
├── b1-fast-food-order-system/
│   ├── prepare_order.py
│   ├── data/
│   │   ├── cashiers.csv
│   │   ├── customers.csv
│   │   ├── drinks.csv
│   │   ├── hamburgers.csv
│   │   ├── happyMeal.csv
│   │   └── sodas.csv
│   │
│   ├── orders/
│   │   ├── __init__.py
│   │   └── order.py
│   │
│   ├── products/
│   │   ├── __init__.py
│   │   ├── food_package.py
│   │   └── product.py
│   │
│   ├── users/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   └── util/
│       ├── __init__.py
│       ├── converter.py
│       └── file_manager.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Included Projects

### A1 Notebook

Introductory Python notebook focused on basic programming concepts.

Main topics:

- Variables
- Data types
- Basic operations
- Conditional logic
- Loops
- Functions
- Notebook-based workflow

### B1 Text Processing

Text processing exercise focused on string manipulation and algorithmic thinking.

Main topics:

- Custom text processing functions
- Word analysis
- Palindrome detection
- Punctuation handling
- Function decomposition
- Unit testing with Pytest

Skills demonstrated:

- Writing reusable functions
- Processing strings without relying only on built-in shortcuts
- Testing Python functions
- Working with helper modules

### B1 Fast Food Order System

Object-oriented Python application that simulates a basic fast food order management system.

The application loads CSV data for cashiers, customers and products, converts the records into Python objects and allows the creation of customer orders.

Main features:

- CSV data loading
- Product management
- Cashier and customer entities
- Order creation
- Total price calculation
- Object-oriented design
- Abstract classes
- Package-based project structure

---

## Fast Food Order System Architecture

```text
CSV Files
   |
   v
CSVFileManager
   |
   v
Converters
   |
   +-- ProductConverter
   +-- CashierConverter
   +-- CustomerConverter
   |
   v
Domain Objects
   |
   +-- Products
   +-- Users
   +-- Orders
   |
   v
Order Processing
```

---

## Main Concepts Practiced

### Python Fundamentals

- Variables
- Functions
- Loops
- Conditionals
- Lists
- Dictionaries
- String handling

### Object-Oriented Programming

- Classes
- Inheritance
- Abstract classes
- Encapsulation
- Composition
- Method overriding

### File Handling

- CSV reading
- Data conversion
- Data mapping
- Simple persistence logic

### Testing

- Pytest
- Test-driven correction
- Function validation

### Project Organization

- Python packages
- Modules
- Imports
- Separation of responsibilities
- Reusable components

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/miguelangeldealba/python-learning-journey.git
cd python-learning-journey
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Run the A1 notebook

```bash
jupyter notebook a1-notebook/Python_A1_Miguel_Angel_de_Alba_y_Perez.ipynb
```

### Run the text processing tests

```bash
cd b1-text-processing
pytest
```

### Run the fast food order system

```bash
cd b1-fast-food-order-system
python prepare_order.py
```

---

## Main Skills Demonstrated

- Python programming fundamentals
- Object-oriented programming
- Abstract classes
- CSV data handling
- Modular code organization
- Unit testing
- Data conversion
- Basic application logic
- Jupyter Notebook usage
- Progressive learning documentation

---

## Project Status

This repository is a learning portfolio.

It is intended to show progression, practice and applied programming knowledge rather than a production-ready application.

Completed:

- Basic Python notebook
- Text processing exercise
- Unit testing practice
- Object-oriented fast food order system
- CSV-based data loading
- Modular package structure

---

## Future Improvements

- Improve folder naming consistency
- Add more intermediate Python exercises
- Add advanced automation scripts
- Add more tests to the fast food order system
- Add type hints across all modules
- Add docstrings to all public functions and classes
- Add CI workflow with GitHub Actions
- Add a dedicated `src/` structure
- Add more real-world mini projects

---

## Author

**Miguel Ángel de Alba y Pérez**

- GitHub: [miguelangeldealba](https://github.com/miguelangeldealba)
- LinkedIn: [Miguel Ángel de Alba](https://www.linkedin.com/in/miguel-angel-de-alba-y-p%C3%A9rez)

---

## License

This project is licensed under the MIT License.
