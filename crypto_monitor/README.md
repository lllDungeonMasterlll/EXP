# Crypto Monitor

## 🚀 Запуск

```bash
docker-compose up --build
```

## 🌐 Доступ

- Django Admin: http://localhost:8000/admin
- FastAPI Docs: http://localhost:8000/docs

## 📡 API

- GET `/blocks` — список блоків (фільтр: currency, пагінація: skip, limit)
- GET `/blocks/{id}` — перегляд конкретного блоку

---

🔁 Дані оновлюються кожну хвилину за допомогою Celery Task `fetch_latest_blocks`

---

Готово до продакшну 😎