# CodeMentor Python Lab

A simple Task Management REST API built using FastAPI and SQLite.

## Features

- Create tasks
- Retrieve tasks
- Update tasks
- Delete tasks
- SQLite database

## Technologies

- Python
- FastAPI
- SQLite
- Uvicorn

## Installation

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run

uvicorn app.main:app --reload

## API Documentation

http://127.0.0.1:8000/docs

## Purpose

This project is used to evaluate an AI coding agent's ability
to inspect a GitHub repository, identify potential bugs,
and recommend fixes.