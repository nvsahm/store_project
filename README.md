# Store Project - Nutzung mit Docker Compose

Diese Anleitung beschreibt, wie du das **Store Project** mit Docker Compose startest und nutzt.

## Voraussetzungen
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Projekt starten
1. Erstelle eine `.env` Datei basierend auf `.env.example`:
   ```sh
   cp .env.example .env
   ```
2. Starte die Container:
   ```sh
   docker-compose up --build
   ```
   Oder im Hintergrund:
   ```sh
   docker-compose up -d --build
   ```
3. Führe Migrationen durch:
   ```sh
   docker-compose exec web python manage.py migrate
   ```
4. Erstelle einen Admin-Benutzer:
   ```sh
   docker-compose exec web python manage.py createsuperuser
   ```
5. Statische Dateien sammeln:
   ```sh
   docker-compose exec web python manage.py collectstatic --noinput
   ```

## Zugriff auf das Projekt
- **Web-App:** [http://localhost:8000](http://localhost:8000)
- **Admin-Bereich:** [http://localhost:8000/admin](http://localhost:8000/admin)
- **API-Dokumentation (Swagger):** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## Projekt stoppen
Container stoppen:
```sh
docker-compose down
```
