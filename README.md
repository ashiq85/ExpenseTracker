# Personal Expense Tracker

A modern, premium personal expense tracking web application built with Python Django.

## Tech Stack
* **Backend:** Python Django
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Chart.js
* **Database:** SQLite (Django default)

## Stack Choices and Tradeoffs
* **Django:** Chosen for its batteries-included approach, which makes setting up the database models, forms, and routing extremely fast and secure. Tradeoff: It might be slightly heavy for a very simple app compared to Flask or FastAPI, but the built-in ORM and Form validation save significant development time.
* **SQLite:** Chosen because it requires zero configuration and is perfectly suitable for a personal, single-user desktop-like application. Tradeoff: Not suitable for high-concurrency production deployments, but deployment is explicitly out of scope for this project.
* **Vanilla CSS/JS:** Chosen to create a custom, premium design with glassmorphism and dynamic dark mode aesthetics without the overhead or learning curve of a heavy frontend framework or utility-first library like Tailwind (unless explicitly requested). Tradeoff: CSS files can grow large, but it gives maximum control over the exact aesthetic requested.
* **Chart.js:** Included via CDN to provide a visually appealing, interactive doughnut chart for the category breakdown in the summary view.

## Features
* **Add Expense:** Title, Amount, Category (Food, Transport, Shopping, Bills, Entertainment, Other), Date, Note.
* **View Expenses:** Dashboard showing all expenses in a clean table format.
* **Edit/Delete:** Update details or remove incorrect entries.
* **Filtering:** Filter expenses by category, date range, or partial title match.
* **Monthly Summary:** View total spending and a beautiful chart breakdown by category for a selected month.
* **Premium Design:** A dynamic dark mode interface with glassmorphism effects, rich colors, and micro-animations on load and hover.

## Done vs Skipped
* **Done:** All core CRUD operations for expenses, filtering by multiple criteria, monthly summary with Chart.js visualization, and a premium styling system.
* **Skipped:** Authentication and deployment were explicitly requested to be skipped. 

## Known Rough Edges
* **Date Filtering:** The HTML5 date input might render differently across various browsers.
* **Summary Month Selector:** The month selector relies on the browser's native `type="month"` input, which is widely supported but might have limited fallback styling on very old browsers.

## Complete Setup & Run Commands

Ensure you have Python installed.

1. **Install Django:**
   ```bash
   python -m pip install django
   ```

2. **Navigate to the project directory:**
   ```bash
   cd expense
   ```

3. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.
