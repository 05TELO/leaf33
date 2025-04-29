# 🌍 Geo App на Django + Leaflet

Простое веб-приложение, позволяющее пользователю выделять области на карте (с помощью [Leaflet](https://leafletjs.com)), сохранять их координаты в базу данных PostgreSQL (`JSONB`) и просматривать сохраненные зоны.

Приложение разворачивается с помощью **Docker Compose**.

---

## 🧱 Требования

Для запуска приложения вам понадобится установленный:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 📦 Установка и запуск

### 1. Склонируйте репозиторий:
```bash
git clone https://github.com/yourusername/django-leaflet-geoapp.git
cd django-leaflet-geoapp
```

### 2. Создайте `.env` файл:
Создайте файл `.env` в корне проекта, основываясь на примере:

```bash
cp .env.example .env
```

Откройте файл `.env` и укажите актуальные данные для подключения к БД, Django и т.п.

---

## 🔧 Запуск приложения

Выполните команду:

```bash
docker-compose up -d --build
```

---

## 🌐 Функционал приложения

- **[http://localhost:8000](http://localhost:8000)** — форма для добавления новых областей.
  - Кнопка "Add Another Area" позволяет динамически добавлять новые поля.
  - Координаты выбираются кликом на карте.
- **POST-запрос** сохраняет данные в PostgreSQL в поле типа JSONB.
- **[http://localhost:8000/data/](http://localhost:8000/data/)** — отображает все сохраненные области.

---

## 🛑 Остановка приложения

Чтобы остановить работу сервисов:

```bash
docker-compose down
```

