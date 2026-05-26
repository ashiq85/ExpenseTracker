# Personal Expense Tracker

A modern, premium personal expense tracking web application built with Python Django. It helps individuals keep a clear, organized record of daily spending, analyze monthly habits, and visualize category breakdowns.

## Project Overview

This is a **self‑contained Django web app** that provides full CRUD (Create, Read, Update, Delete) functionality for expense entries. Users can:

* **Add** an expense with title, amount (in Indian Rupees), category, date, and optional note.
* **View** a sortable list of all expenses, automatically ordered by the most recent date and entry.
* **Filter** the list by category, custom date range, or title keyword.
* **Edit / Delete** any entry.
* **See a monthly summary** that shows total spending and a Chart.js doughnut chart breaking down expenses by category.

All of this runs locally with a lightweight SQLite database and requires **no authentication** or external services – ideal for personal use or as a teaching demo.

## Why This Stack?

* **Django** – Batteries‑included framework that handles data modeling, form validation, and routing out‑of‑the‑box, giving us solid code hygiene and rapid development.
* **SQLite** – Zero‑configuration, file‑based DB perfect for a single‑user desktop‑like app.
* **Vanilla HTML/CSS/JS** – Complete control over the premium UI (dark mode, glassmorphism, micro‑animations) without the overhead of a heavyweight front‑end framework.
* **Chart.js** – Simple CDN‑loaded library for interactive charts, giving visual insight into spending patterns.

## Tech Stack
* **Backend:** Python Django
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Chart.js
* **Database:** SQLite (Django default)

## What Was Built & Why (Data Model & Code Hygiene)

This project was built to be a robust, end‑to‑end functional web application focusing on code hygiene and a sensible, scalable data model.

* **The Data Model:** The `Expense` model is designed with strict data integrity in mind.
  * `amount` utilizes a `DecimalField` (instead of a FloatField) to prevent floating‑point arithmetic errors commonly associated with currency. It also strictly validates that values must be 0.01 or greater (no negative expenses).
  * `date` utilizes a custom validator to ensure no future dates can be logged, keeping data historically accurate.
  * `category` uses choices enforced at the database level to prevent invalid data entry.
* **Code Hygiene & Architecture:**
  * The application heavily leverages Django's **Class‑Based Views (CBVs)** (`ListView`, `CreateView`, `UpdateView`, `DeleteView`). This minimizes boilerplate code, keeps the `views.py` file extremely clean (DRY principle), and relies on battle‑tested framework code for routing and database interactions.
  * Form rendering and logic are neatly abstracted away into `forms.py` using `ModelForm`, ensuring that frontend validation matches database constraints exactly without messy HTML hardcoding.
  * Separation of concerns is strictly maintained: styling is entirely isolated in `style.css`, and business logic lives firmly in the backend.

## Stack Choices and Tradeoffs
* **Django:** Chosen for its batteries‑included approach, which makes setting up the database models, forms, and routing extremely fast and secure. Tradeoff: It might be slightly heavy for a very simple app compared to Flask or FastAPI, but the built‑in ORM and Form validation save significant development time.
* **SQLite:** Chosen because it requires zero configuration and is perfectly suitable for a personal, single‑user desktop‑like application. Tradeoff: Not suitable for high‑concurrency production deployments, but deployment is explicitly out of scope for this project.
* **Vanilla CSS/JS:** Chosen to create a custom, premium design with glassmorphism and dynamic dark mode aesthetics without the overhead or learning curve of a heavy frontend framework or utility‑first library like Tailwind (unless explicitly requested). Tradeoff: CSS files can grow large, but it gives maximum control over the exact aesthetic requested.
* **Chart.js:** Included via CDN to provide a visually appealing, interactive doughnut chart for the category breakdown in the summary view.

## Features
* **Add Expense:** Title, Amount, Category (Food, Transport, Shopping, Bills, Entertainment, Other), Date, Note.
* **View Expenses:** Dashboard showing all expenses in a clean table format.
* **Edit/Delete:** Update details or remove incorrect entries.
* **Filtering:** Filter expenses by category, date range, or partial title match.
* **Monthly Summary:** View total spending and a beautiful chart breakdown by category for a selected month.
* **Premium Design:** A dynamic dark mode interface with glassmorphism effects, rich colors, and micro‑animations on load and hover.

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
