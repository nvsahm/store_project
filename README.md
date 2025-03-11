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
   docker-compose exec django-web python manage.py migrate
   ```
4. Erstelle einen Admin-Benutzer:
   ```sh
   docker-compose exec django-web python manage.py createsuperuser
   ```
5. Statische Dateien sammeln:
   ```sh
   docker-compose exec django-web python manage.py collectstatic --noinput
   ```

## Zugriff auf das Projekt
- **Admin-Bereich:** [http://localhost:8000/admin](http://localhost:8000/admin)
- **API-Dokumentation (Swagger):** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## Authentifizierungs-Token im Django Admin erstellen
1. Melde dich im Django Admin unter [http://localhost:8000/admin](http://localhost:8000/admin) mit deinem Admin-Benutzer an.
2. Navigiere zu **Tokens** (unter "Auth Token").
3. Erstelle einen neuen Token für deinen Benutzer.

## Token für API-Anfragen in Swagger nutzen
1. Öffne die Swagger-Dokumentation unter [http://localhost:8000/swagger/](http://localhost:8000/swagger/).
2. Klicke oben rechts auf "Authorize".
3. Gib deinen Token im Format `Token <dein-token>` ein.
4. Bestätige die Eingabe, um authentifizierte API-Anfragen auszuführen.

## Projekt stoppen
Container stoppen:
```sh
docker-compose down
```
