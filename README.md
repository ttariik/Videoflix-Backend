# VideoFlix Backend

[English](#english) | [Deutsch](#deutsch)

## English

### Overview
VideoFlix is a powerful video streaming backend built with Django and Django REST Framework. It provides a robust API for video management, user authentication, and video processing capabilities.

### Author
This project was created by Tarik Sabanovic.

### Features
- User Authentication and Authorization
- Video Upload and Management
- Video Processing and Thumbnail Generation
- RESTful API Endpoints
- Background Task Processing with RQ
- Redis Caching
- PostgreSQL Database Support

### Prerequisites
- Python 3.8 or higher
- PostgreSQL
- Redis
- FFmpeg

### Installation

#### macOS Installation

1. Install Homebrew (if not already installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install required system dependencies:
```bash
# Install PostgreSQL
brew install postgresql
brew services start postgresql

# Install Redis
brew install redis
brew services start redis

# Install FFmpeg
brew install ffmpeg
```

3. Clone the repository:
```bash
git clone [repository-url]
cd VideoFlix-Backend
```

4. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/videoflix
REDIS_URL=redis://localhost:6379/0
```

7. Run migrations:
```bash
python manage.py migrate
```

8. Create a superuser:
```bash
python manage.py createsuperuser
```

### Running the Project on macOS

1. Start Redis server (if not running):
```bash
brew services start redis
```

2. Start RQ worker:
```bash
python manage.py rqworker default
```

3. Run the development server:
```bash
python manage.py runserver
```

### API Endpoints

- Authentication:
  - `/api/auth/register/` - User registration
  - `/api/auth/login/` - User login
  - `/api/auth/logout/` - User logout

- Videos:
  - `/api/videos/` - List and create videos
  - `/api/videos/<id>/` - Retrieve, update, and delete specific video
  - `/api/videos/<id>/thumbnail/` - Get video thumbnail

### Development

The project uses:
- Django 5.1.7
- Django REST Framework
- Redis for caching and background tasks
- PostgreSQL as the database
- RQ for background job processing

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 Tarik Sabanovic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Deutsch

### Übersicht
VideoFlix ist ein leistungsstarkes Video-Streaming-Backend, das mit Django und Django REST Framework entwickelt wurde. Es bietet eine robuste API für Videoverwaltung, Benutzerauthentifizierung und Videoverarbeitung.

### Autor
Dieses Projekt wurde von Tarik Sabanovic erstellt.

### Funktionen
- Benutzerauthentifizierung und -autorisierung
- Video-Upload und -Verwaltung
- Videoverarbeitung und Thumbnail-Generierung
- RESTful API-Endpunkte
- Hintergrundaufgabenverarbeitung mit RQ
- Redis-Caching
- PostgreSQL-Datenbankunterstützung

### Voraussetzungen
- Python 3.8 oder höher
- PostgreSQL
- Redis
- FFmpeg

### Installation

#### macOS Installation

1. Homebrew installieren (falls noch nicht installiert):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Erforderliche Systemabhängigkeiten installieren:
```bash
# PostgreSQL installieren
brew install postgresql
brew services start postgresql

# Redis installieren
brew install redis
brew services start redis

# FFmpeg installieren
brew install ffmpeg
```

3. Repository klonen:
```bash
git clone [repository-url]
cd VideoFlix-Backend
```

4. Virtuelle Umgebung erstellen und aktivieren:
```bash
python -m venv env
source env/bin/activate
```

5. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

6. Umgebungsvariablen einrichten:
Erstellen Sie eine `.env`-Datei im Hauptverzeichnis mit folgenden Variablen:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/videoflix
REDIS_URL=redis://localhost:6379/0
```

7. Migrationen ausführen:
```bash
python manage.py migrate
```

8. Superuser erstellen:
```bash
python manage.py createsuperuser
```

### Projekt auf macOS starten

1. Redis-Server starten (falls nicht läuft):
```bash
brew services start redis
```

2. RQ-Worker starten:
```bash
python manage.py rqworker default
```

3. Entwicklungsserver starten:
```bash
python manage.py runserver
```

### API-Endpunkte

- Authentifizierung:
  - `/api/auth/register/` - Benutzerregistrierung
  - `/api/auth/login/` - Benutzeranmeldung
  - `/api/auth/logout/` - Benutzerabmeldung

- Videos:
  - `/api/videos/` - Videos auflisten und erstellen
  - `/api/videos/<id>/` - Bestimmtes Video abrufen, aktualisieren und löschen
  - `/api/videos/<id>/thumbnail/` - Video-Thumbnail abrufen

### Entwicklung

Das Projekt verwendet:
- Django 5.1.7
- Django REST Framework
- Redis für Caching und Hintergrundaufgaben
- PostgreSQL als Datenbank
- RQ für die Verarbeitung von Hintergrundjobs

### Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

Copyright (c) 2024 Tarik Sabanovic

Hiermit wird jeder Person, die eine Kopie dieser Software und der zugehörigen Dokumentationsdateien (die "Software") erhält, kostenlos die Erlaubnis erteilt, mit der Software ohne Einschränkung zu handeln, einschließlich und ohne Einschränkung der Rechte zur Nutzung, Kopierung, Änderung, Zusammenführung, Veröffentlichung, Verbreitung, Unterlizenzierung und/oder zum Verkauf von Kopien der Software, und Personen, denen die Software zur Verfügung gestellt wird, diese unter den folgenden Bedingungen zu gestatten:

Der obige Copyright-Hinweis und dieser Erlaubnishinweis müssen in allen Kopien oder wesentlichen Teilen der Software enthalten sein.

DIE SOFTWARE WIRD "WIE BESEHEN" OHNE JEGLICHE AUSDRÜCKLICHE ODER IMPLIZIERTE GARANTIE BEREITGESTELLT, EINSCHLIESSLICH, ABER NICHT BESCHRÄNKT AUF DIE GARANTIEN DER MARKTGÄNGIGKEIT, EIGNUNG FÜR EINEN BESTIMMTEN ZWECK UND NICHTVERLETZUNG VON RECHTEN DRITTER. IN KEINEM FALL SIND DIE AUTOREN ODER COPYRIGHT-INHABER HAFTBAR FÜR JEGLICHE ANSPRÜCHE, SCHÄDEN ODER ANDERE HAFTUNG, OB IN EINER VERTRAGLICHEN HANDLUNG, UNERLAUBTER HANDLUNG ODER ANDERWEITIG, DIE AUS ODER IN VERBINDUNG MIT DER SOFTWARE ODER DER NUTZUNG ODER ANDEREN GESCHÄFTEN MIT DER SOFTWARE ENTSTEHEN.
