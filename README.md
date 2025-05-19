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
- `playwright` — современный инструмент для end-to-end тестов (API + UI)
- `allure` — отчетность
- `pytest-html` — для генерации HTML-отчета

## Структура проекта
project/
│
├── tests/
│   ├── api/                # Тесты API
│   │   ├── test_auth.py
│   │   ├── test_orders.py
│   │   └── ...
│   │
│   └── ui/                 # Тесты UI (Selenium / Playwright)
│       ├── test_login.py
│       ├── test_order_flow.py
│       └── ...
│
├── pages/                  # Page Object Model для UI
│   ├── login_page.py
│   ├── order_page.py
│   └── ...
│
├── data/                   # Тестовые данные, фикстуры
│   └── users.py
│
├── utils/                  # Вспомогательные модули
│   ├── api_client.py       # Клиент для API-запросов
│   ├── browser_utils.py    # Браузерные утилиты
│   └── ...
│
├── conftest.py             # Общие фикстуры для pytest
├── requirements.txt
└── README.md

## Установка зависимостей
pip install -r requirements.txt

## Запуск тестов
pytest -v tests/

