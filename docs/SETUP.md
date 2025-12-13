# ReMeals Setup Guide

Complete setup instructions for getting ReMeals running on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** >= 20.9 (for Next.js and React 19)
- **Python** 3.12 or higher
- **PostgreSQL** 15 or higher
- **Docker** and **Docker Compose** (optional, for containerized setup)
- **Git** (for version control)

### Check Your Versions

```bash
node --version    # Should be >= 20.9
python --version  # Should be >= 3.12
psql --version    # Should be >= 15
docker --version  # Optional
```

## Installation Methods

You can set up ReMeals using either:
1. **Docker** (Recommended for quick start)
2. **Local Setup** (Recommended for active development)

---

## Method 1: Docker Setup (Recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/NapatKulnarong/Re-Meals.git
cd Re-Meals
```

### Step 2: Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
# Database
POSTGRES_DB=remeals
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

### Step 3: Build and Start Services

```bash
docker-compose up -d
```

This will start:
- Frontend at http://localhost:3000
- Backend API at http://localhost:8000
- PostgreSQL at localhost:5432
- pgAdmin at http://localhost:5050

### Step 4: Run Database Migrations

```bash
docker-compose exec backend python manage.py migrate
```

### Step 5: Create Superuser (Optional)

```bash
docker-compose exec backend python manage.py createsuperuser
```

If you've already set `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, and `DJANGO_SUPERUSER_PASSWORD` in your `.env`, you can auto-create the admin account without prompts (note the extra shell so the container expands the env vars, not your host shell):

```bash
docker-compose exec backend bash -c '
  python manage.py createsuperuser \
    --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL"
'
```

### Step 6: Load Sample Data (Optional)

```bash
docker-compose exec backend python manage.py loaddata fixtures/*.json
```

### Step 7: Access the Application

- **Frontend**: http://localhost:3000
- **Backend Admin**: http://localhost:8000/admin
- **API Documentation**: http://localhost:8000/swagger/
- **pgAdmin**: http://localhost:5050

---

## Method 2: Local Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/NapatKulnarong/Re-Meals.git
cd Re-Meals
```

### Step 2: PostgreSQL Setup

Create a database for ReMeals:

```bash
# Login to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE remeals;

# Create user (optional)
CREATE USER remealsuser WITH PASSWORD 'your_password';

# Grant privileges
GRANT ALL PRIVILEGES ON DATABASE remeals TO remealsuser;

# Exit psql
\q
```

### Step 3: Backend Setup

#### 3.1 Create Virtual Environment

```bash
cd backend
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

#### 3.2 Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3.3 Configure Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Database
POSTGRES_DB=remeals
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Django
SECRET_KEY=your-django-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

#### 3.4 Run Migrations

```bash
python manage.py migrate
```

#### 3.5 Create Superuser

```bash
python manage.py createsuperuser
```

#### 3.6 Load Sample Data (Optional)

```bash
python manage.py loaddata fixtures/*.json
```

This will load test users, restaurants, warehouses, communities, donations, and other sample data.

#### 3.7 Start Development Server

```bash
python manage.py runserver
```

Backend will be available at http://localhost:8000

### Step 4: Frontend Setup

Open a new terminal window.

#### 4.1 Navigate to Frontend Directory

```bash
cd frontend
```

#### 4.2 Install Dependencies

```bash
npm install
```

#### 4.3 Configure Environment Variables

Create a `.env.local` file in the `frontend/` directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

#### 4.4 Start Development Server

```bash
npm run dev
```

Frontend will be available at http://localhost:3000

---

## Test Users

After loading the sample data fixtures, the following test users will be available for testing different roles:

### Administrator
| Field | Value |
|-------|-------|
| **Username** | `admin` |
| **Password** | `password123` |
| **Email** | admin@remeals.com |
| **Role** | System Administrator |
| **Name** | System Administrator |

### Donors
| Username | Password | Email | Restaurant | Name |
|----------|----------|-------|------------|------|
| `donor1` | `password123` | findlay.kl@gmail.com | RES0000001 | Findlay Kline |
| `donor2` | `password123` | lili.byrd@gmail.com | RES0000003 | Lili Byrd |

### Delivery Staff
| Username | Password | Email | Assigned Area | Name |
|----------|----------|-------|---------------|------|
| `delivery1` | `password123` | cordelia.ly@gmail.com | Bangkok Central | Cordelia Lynn |
| `delivery2` | `password123` | gideon.cu@gmail.com | Samut Prakan | Gideon Curry |

### Recipients
| Username | Password | Email | Community | Name | Address |
|----------|----------|-------|-----------|------|---------|
| `recipient1` | `password123` | aston.me@gmail.com | COM0000001 | Aston Merritt | 123 Klong Toey, Bangkok 10110 |
| `recipient2` | `password123` | keeley.br@gmail.com | COM0000002 | Keeley Bradford | 456 Bang Khen, Bangkok 10220 |

### Using Test Users

1. **Login to Admin Panel**
   ```
   URL: http://localhost:8000/admin
   Username: admin
   Password: password123
   ```

2. **Test API Authentication**
   ```bash
   # Login via API
   curl -X POST http://localhost:8000/api/users/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "donor1", "password": "password123"}'
   ```

3. **Test Different User Roles**
   - Use donor accounts to test donation creation
   - Use delivery staff accounts to test delivery coordination
   - Use recipient accounts to test donation requests
   - Use admin account for full system access

### Password Information

All test users use the same password: `password123`

To generate a new password hash for fixtures, run:
```bash
cd backend/fixtures
python generate_password_hash.py
```

**Note**: These are test credentials for development only. Never use these in production!

---

## Verification

### Test Backend API

```bash
# Check API health
curl http://localhost:8000/api/

# Access Swagger documentation
open http://localhost:8000/swagger/
```

### Test Frontend

Open http://localhost:3000 in your browser

### Access Admin Panel

1. Navigate to http://localhost:8000/admin
2. Login with your superuser credentials
3. Explore the data models

---

## Common Issues and Troubleshooting

### Database Connection Issues

**Problem**: `psycopg2.OperationalError: could not connect to server`

**Solution**:
- Verify PostgreSQL is running: `pg_isready`
- Check database credentials in `.env`
- Ensure database exists: `psql -l`

### Port Already in Use

**Problem**: `Error: Port 8000 is already in use`

**Solution**:
```bash
# Find process using port
lsof -ti:8000

# Kill process
kill -9 <PID>

# Or use a different port
python manage.py runserver 8001
```

### Node Version Mismatch

**Problem**: `The engine "node" is incompatible with this module`

**Solution**:
```bash
# Use nvm to install correct version
nvm install 20
nvm use 20
```

### Migration Issues

**Problem**: `django.db.migrations.exceptions.InconsistentMigrationHistory`

**Solution**:
```bash
# Reset migrations (WARNING: This will delete all data)
python manage.py migrate --fake <app_name> zero
python manage.py migrate
```

### Docker Issues

**Problem**: `docker-compose: command not found`

**Solution**:
```bash
# Use docker compose (newer syntax)
docker compose up -d
```

**Problem**: Container won't start

**Solution**:
```bash
# View logs
docker-compose logs backend
docker-compose logs frontend

# Rebuild containers
docker-compose down
docker-compose up --build
```

---

## Development Tools

### Recommended VS Code Extensions

- Python
- Django
- ESLint
- Prettier
- Tailwind CSS IntelliSense
- Docker
- PostgreSQL

### Database Management Tools

- **pgAdmin**: http://localhost:5050 (if using Docker)
- **DBeaver**: Desktop application
- **TablePlus**: macOS application
- **psql**: Command-line interface

### API Testing Tools

- **Swagger UI**: http://localhost:8000/swagger/
- **Postman**: Desktop application
- **curl**: Command-line tool
- **HTTPie**: User-friendly command-line tool

---

## Next Steps

After successful setup:

1. Read [DEVELOPMENT.md](./DEVELOPMENT.md) for development guidelines
2. Explore [API.md](./API.md) for API documentation
3. Check [ARCHITECTURE.md](./ARCHITECTURE.md) for system architecture
4. Review the database schema in [db-diagram.png](./db-diagram.png)

---

## Additional Commands

### Backend Commands

```bash
# Create new Django app
python manage.py startapp <app_name>

# Make migrations
python manage.py makemigrations

# Run specific migration
python manage.py migrate <app_name> <migration_number>

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Shell
python manage.py shell
```

### Frontend Commands

```bash
# Development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Lint code
npm run lint

# Type check
npm run type-check
```

### Docker Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild containers
docker-compose up --build

# Execute command in container
docker-compose exec backend python manage.py migrate

# Access shell
docker-compose exec backend bash
```

---

## Getting Help

If you encounter issues:

1. Check this setup guide
2. Review existing [GitHub Issues](https://github.com/NapatKulnarong/Re-Meals/issues)
3. Create a new issue with:
   - Your operating system
   - Python and Node versions
   - Error messages
   - Steps to reproduce
