# 🧾 PDF to Text API

**API-сервис для извлечения текста из PDF-файлов**, развёрнутый с использованием FastAPI, Docker и Caddy. Поддерживает мониторинг (Uptime Kuma) и готов к деплою с SSL-сертификатом.

## 🚀 Функциональность

- Загружайте PDF — получайте текст в ответе.
- Эндпоинт `/extract` с методом `POST` и параметром `file`.
- Подходит для интеграции в бэкенды, автоматизации и data-пайплайны.

---

## 🔧 Быстрый запуск (локально)

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/RgbScan/pdf-to-text-api.git
cd pdf-to-text-api
```

### 2. Настройте `.env`

Создайте `.env` на основе шаблона:

```bash
cp .env.example .env
```

### 3. Соберите и запустите проект

```bash
docker compose up --build -d
```

### 4. Проверьте работу

Откройте:
- 🌐 `http://localhost/docs` — Swagger UI
- ✅ `http://localhost/health` — Health check

---

## 🧪 Тестирование

Проект использует `pytest`. Для запуска тестов:

```bash
pip install -r requirements.txt
pytest
```

Пример проверки `/health`:

```python
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

---

## ⚙️ Стек

- **FastAPI** — backend-фреймворк.
- **Uvicorn** — ASGI-сервер.
- **Docker / Docker Compose** — контейнеризация.
- **Caddy** — обратный прокси и SSL.
- **Uptime Kuma** — мониторинг доступности.

---

## 🗂️ Структура проекта

```
.
├── src/                  # Исходный код FastAPI
│   └── main.py
├── tests/                # Тесты (pytest)
├── Dockerfile            # Docker-образ API
├── docker-compose.yml    # Стек: API + Caddy + Kuma
├── Caddyfile             # Reverse proxy правила
├── .env                  # Переменные окружения (в .gitignore)
├── .env.example          # Шаблон .env
├── .gitignore
├── .dockerignore
└── README.md
```

---

## 📦 Развёртывание на сервере

1. Установите Docker и Docker Compose.
2. Укажите свой `DOMAIN` в `.env`.
3. Пробросьте 80/443 порты.
4. Запустите `docker compose up --build -d`.

---

## 📡 Мониторинг (по желанию)

После запуска откройте:
```
http://localhost:3001
```
Интерфейс Uptime Kuma поможет отслеживать работу сервиса.
