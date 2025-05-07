# VideoFlix Backend

[English](#english) | [Deutsch](#deutsch)

## English

### What is VideoFlix?
VideoFlix is a modern, feature-rich video streaming backend platform built with Django and Django REST Framework. It provides a robust API for video management, user authentication, and video processing capabilities, making it perfect for building video streaming applications.

### Key Features
- **User Management**
  - Secure user authentication
  - Email verification
  - Password reset functionality
  - User profile management

- **Video Management**
  - Video upload and storage
  - Automatic video processing
  - Multiple quality versions (120p, 360p, 720p, 1080p)
  - Thumbnail generation
  - Video categorization

- **API Features**
  - RESTful API endpoints
  - Token-based authentication
  - CORS support
  - Rate limiting
  - Pagination

- **Background Processing**
  - Asynchronous video processing
  - Queue management with Redis
  - Progress tracking

### Technology Stack
- **Backend Framework**: Django 5.1.7
- **API Framework**: Django REST Framework
- **Database**: PostgreSQL
- **Cache & Queue**: Redis
- **Video Processing**: FFmpeg, MoviePy
- **Task Queue**: RQ (Redis Queue)
- **Development Tools**: Black, Flake8, Pytest

### Prerequisites
- Python 3.8 or higher
- PostgreSQL
- Redis
- FFmpeg
- Git

### Installation

#### macOS Installation

1. **Install Homebrew** (if not already installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. **Install System Dependencies**:
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

3. **Clone the Repository**:
```bash
git clone [repository-url]
cd VideoFlix-Backend
```

4. **Set Up Python Environment**:
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

5. **Configure Environment Variables**:
```bash
# Copy the template file
cp .env.template .env

# Edit the .env file with your settings
nano .env  # or use your preferred editor
```

6. **Set Up Database**:
```bash
# Create database
createdb videoflix

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

#### Windows Installation

1. **Install Required Software**:
   - Install [Python](https://www.python.org/downloads/)
   - Install [PostgreSQL](https://www.postgresql.org/download/windows/)
   - Install [Redis for Windows](https://github.com/microsoftarchive/redis/releases)
   - Install [FFmpeg](https://ffmpeg.org/download.html)

2. **Clone the Repository**:
```bash
git clone [repository-url]
cd VideoFlix-Backend
```

3. **Set Up Python Environment**:
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

4. **Configure Environment Variables**:
```bash
# Copy the template file
copy .env.template .env

# Edit the .env file with your settings
notepad .env  # or use your preferred editor
```

5. **Set Up Database**:
```bash
# Create database using pgAdmin or psql
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Running the Project

#### macOS
```bash
# Start Redis (if not running)
brew services start redis

# Start RQ worker
python manage.py rqworker default

# Run development server
python manage.py runserver
```

#### Windows
```bash
# Start Redis server
redis-server

# Start RQ worker
python manage.py rqworker default

# Run development server
python manage.py runserver
```

### API Documentation
The API documentation is available at `/api/docs/` when running the development server.

### Development
- Use `black` for code formatting
- Use `flake8` for linting
- Run tests with `pytest`

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Deutsch

### Was ist VideoFlix?
VideoFlix ist eine moderne, funktionsreiche Video-Streaming-Backend-Plattform, die mit Django und Django REST Framework entwickelt wurde. Sie bietet eine robuste API für Videoverwaltung, Benutzerauthentifizierung und Videoverarbeitung, was sie perfekt für den Aufbau von Video-Streaming-Anwendungen macht.

### Hauptfunktionen
- **Benutzerverwaltung**
  - Sichere Benutzerauthentifizierung
  - E-Mail-Verifizierung
  - Passwort-Reset-Funktionalität
  - Benutzerprofilverwaltung

- **Videoverwaltung**
  - Video-Upload und -Speicherung
  - Automatische Videoverarbeitung
  - Mehrere Qualitätsversionen (120p, 360p, 720p, 1080p)
  - Thumbnail-Generierung
  - Video-Kategorisierung

- **API-Funktionen**
  - RESTful API-Endpunkte
  - Token-basierte Authentifizierung
  - CORS-Unterstützung
  - Rate-Limiting
  - Paginierung

- **Hintergrundverarbeitung**
  - Asynchrone Videoverarbeitung
  - Warteschlangenverwaltung mit Redis
  - Fortschrittsverfolgung

### Technologie-Stack
- **Backend-Framework**: Django 5.1.7
- **API-Framework**: Django REST Framework
- **Datenbank**: PostgreSQL
- **Cache & Queue**: Redis
- **Videoverarbeitung**: FFmpeg, MoviePy
- **Task-Queue**: RQ (Redis Queue)
- **Entwicklungstools**: Black, Flake8, Pytest

### Voraussetzungen
- Python 3.8 oder höher
- PostgreSQL
- Redis
- FFmpeg
- Git

### Installation

#### macOS Installation

1. **Homebrew installieren** (falls noch nicht installiert):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. **Systemabhängigkeiten installieren**:
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

3. **Repository klonen**:
```bash
git clone [repository-url]
cd VideoFlix-Backend
```

4. **Python-Umgebung einrichten**:
```bash
# Virtuelle Umgebung erstellen
python -m venv env

# Virtuelle Umgebung aktivieren
source env/bin/activate

# Abhängigkeiten installieren
pip install -r requirements.txt
```

5. **Umgebungsvariablen konfigurieren**:
```bash
# Template-Datei kopieren
cp .env.template .env

# .env-Datei mit Ihren Einstellungen bearbeiten
nano .env  # oder Ihren bevorzugten Editor verwenden
```

6. **Datenbank einrichten**:
```bash
# Datenbank erstellen
createdb videoflix

# Migrationen ausführen
python manage.py migrate

# Superuser erstellen
python manage.py createsuperuser
```

#### Windows Installation

1. **Erforderliche Software installieren**:
   - [Python](https://www.python.org/downloads/) installieren
   - [PostgreSQL](https://www.postgresql.org/download/windows/) installieren
   - [Redis for Windows](https://github.com/microsoftarchive/redis/releases) installieren
   - [FFmpeg](https://ffmpeg.org/download.html) installieren

2. **Repository klonen**:
```bash
git clone [repository-url]
cd VideoFlix-Backend
```

3. **Python-Umgebung einrichten**:
```bash
# Virtuelle Umgebung erstellen
python -m venv env

# Virtuelle Umgebung aktivieren
env\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt
```

4. **Umgebungsvariablen konfigurieren**:
```bash
# Template-Datei kopieren
copy .env.template .env

# .env-Datei mit Ihren Einstellungen bearbeiten
notepad .env  # oder Ihren bevorzugten Editor verwenden
```

5. **Datenbank einrichten**:
```bash
# Datenbank mit pgAdmin oder psql erstellen
# Migrationen ausführen
python manage.py migrate

# Superuser erstellen
python manage.py createsuperuser
```

### Projekt starten

#### macOS
```bash
# Redis starten (falls nicht läuft)
brew services start redis

# RQ-Worker starten
python manage.py rqworker default

# Entwicklungsserver starten
python manage.py runserver
```

#### Windows
```bash
# Redis-Server starten
redis-server

# RQ-Worker starten
python manage.py rqworker default

# Entwicklungsserver starten
python manage.py runserver
```

### API-Dokumentation
Die API-Dokumentation ist unter `/api/docs/` verfügbar, wenn der Entwicklungsserver läuft.

### Entwicklung
- `black` für Code-Formatierung verwenden
- `flake8` für Linting verwenden
- Tests mit `pytest` ausführen

### Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.
