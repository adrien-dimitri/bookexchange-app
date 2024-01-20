Book exchange app
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
=====

The book exchange app is a web platform that allows users to buy, sell, and trade textbooks with other students, providing a convenient and cost-effective solution for acquiring course materials.

## Table of Contents
* [Overview](#overview)
* [Features](#features)
* [Technologies](#technologies)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)

## Overview
The Book Exchange Web App is a Django-based platform designed to facilitate the buying, selling, and trading of textbooks among university students. 

It provides a user-friendly interface and essential features to streamline the textbook exchange process and help students find the resources they need for their courses efficiently.

## Features
- **User Registration**: Create an account and set up a personalized profile.
- **Textbook Listings**: Users can list their textbooks for sale or trade.
- **Textbook Search**: Search for textbooks by title, author, or other criteria.
- **Messaging System**: Communicate with other users to negotiate textbook transactions.
- **Transaction Management**: Manage your listings, messages, and transactions within the app.


## Technologies
- **Python**: Programming language used for the backend development.
- **Django**: High-level Python web framework used for building the web application.
- **HTML/CSS**: Markup and styling languages used for the frontend design and layout.
- **Tailwind CSS**: Utility-first CSS framework used for rapid and flexible UI development.
- **PostgreSQL**: Open-source relational database used to store user and app data.
- **Docker**: Containerization platform used for packaging the application and its dependencies into containers for easy deployment and scalability.
- **Django Rest Framework**: Toolkit for building Web APIs used to develop the backend API endpoints.
- **Django Channels**: Library for handling WebSocket communication used for real-time messaging functionality.

## Requirements
* asgiref==3.6.0
* Django==4.2
* Pillow==9.5.0
* psycopg==3.1.8
* sqlparse==0.4.4
* typing_extensions==4.5.0


## Installation

Follow these steps to set up the Book Exchange Web App locally:

- Clone the repository: git clone https://github.com/adrien-dimitri/bookexchange-app.git
- Navigate to the project directory: ```cd bookexchange-app```
- Create a virtual environment: ```python -m venv venv```
- Activate the virtual environment:
  - On Windows: ```venv\Scripts\activate```
  - On macOS/Linux: ```source venv/bin/activate```
- Install the required dependencies: ```pip install -r requirements.txt```
- Set up the database:
  - Update the database settings in `settings.py` file.
  - Run migrations: ```python manage.py migrate```
- Start the development server: ```python manage.py runserver```
- Access the app in your browser at http://localhost:8000/


## Usage

- Create an account or log in to an existing account.
- List textbooks you want to sell or trade.
- Search for textbooks you need by title, author, or category.
- Communicate with other users through the messaging system to negotiate transactions.
- Manage your listings, messages, and transactions through the user interface.
