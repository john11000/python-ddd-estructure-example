# Flask DDD Application with DTOs and Validation

This project is a Python web application using the _Flask_ framework, designed with the principles of _Domain-Driven Design (DDD). The application focuses on clean separation of concerns between the domain logic, application services, and infrastructure, with a strong emphasis on \*\*input validation_ through _Data Transfer Objects (DTOs)_.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Validations](#validations)
- [Domain Layer](#domain-layer)
- [Application Layer](#application-layer)
- [Infrastructure Layer](#infrastructure-layer)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project is organized into layers to maintain a clean separation of concerns, with each layer having specific responsibilities. The structure is as follows:

```bash
my_flask_app/
│
├── app/
│   ├── _init_.py         # Flask initialization and configuration
│   ├── routes.py           # Route definitions
│   ├── services.py         # Application service layer
│   ├── controllers/        # Request controllers
│   ├── dto/                # DTOs (Data Transfer Objects)
│   ├── validators/         # Input data validation logic
│   └── config.py           # Application configuration
│
├── domain/
│   ├── _init_.py
│   ├── models/             # Domain entities
│   ├── repositories/       # Domain repository interfaces
│   ├── services/           # Domain services
│   ├── exceptions/         # Domain-specific exceptions
│
├── infrastructure/
│   ├── repositories/       # Repository implementations (DB, etc.)
│   └── db.py               # Database configuration
│
└── tests/
    ├── test_routes.py      # Route tests
    ├── test_services.py    # Service tests
    └── test_dto.py         # DTO validation tests
```
