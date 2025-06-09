# API Автотесты для Stellar Burgers
Тестовый проект по автоматизации тестирования API для сервиса **Stellar Burgers**.

## Ссылки
- [Документация API (PDF)](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89)
- [Веб-приложение](https://stellarburgers.nomoreparties.site/login)

## Стек технологий

- Python 3.10+
- `pytest` — фреймворк для запуска тестов
- `requests` — HTTP-клиент для взаимодействия с API
- `selenium` — автоматизация UI-тестирования (браузерное взаимодействие)
- `allure` — отчетность
- `pytest-html` — для генерации HTML-отчета

## Структура проекта
```bash
├── config/                  # Конфигурационные файлы
│   └── config.py            # Общие настройки (URLs, токены и т.д.)
│
├── locators/                # Локаторы для UI тестов
│   ├── __init__.py
│   ├── login_page.py        # Локаторы для страницы логина
│   └── registration_page.py # Локаторы для страницы регистрации
│
├── pages/                   # Страницы для UI тестов (Page Object Model)
│   ├── __init__.py
│   ├── login_page.py        # Класс страницы для логина
│   └── registration_page.py # Класс страницы для регистрации
│
├── tests/                   # Директория для тестов
│   ├── ui/                  # UI тесты (Selenium или Playwright)
│   │   ├── __init__.py
│   │   ├── test_login.py    # Пример UI теста для логина
│   │   └── test_registration.py # Пример UI теста для регистрации
│   │
│   ├── api/                 # API тесты (requests или Playwright)
│   │   ├── __init__.py
│   │   ├── test_user.py     # Пример API теста для пользователя
│   │   └── test_product.py  # Пример API теста для продукта
│   │
│   └── test_all.py          # Главный файл для запуска всех тестов
│
├── utils/                   # Утилиты для тестов
│   ├── __init__.py
│   ├── api_helper.py        # Вспомогательные функции для API тестов
│   └── ui_helper.py         # Вспомогательные функции для UI тестов
│
├── reports/                 # Папка для отчетов
│   └── allure-results/      # Результаты для Allure
│
├── requirements.txt         # Файл с зависимостями
├── pytest.ini               # Конфигурация для pytest
└── README.md                # Документация по проекту

## Установка зависимостей
pip install -r requirements.txt

## Запуск тестов
pytest -v tests/

