# ReMeals Development Guide

Guidelines and best practices for contributing to the ReMeals project.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style](#code-style)
- [Backend Development](#backend-development)
- [Frontend Development](#frontend-development)
- [Testing](#testing)
- [Git Workflow](#git-workflow)
- [Common Tasks](#common-tasks)

---

## Getting Started

Before you begin development, ensure you have completed the setup process described in [SETUP.md](./SETUP.md).

### Test Users

For testing purposes, load the sample data fixtures which include test users for all roles:

```bash
# From backend directory
python manage.py loaddata fixtures/*.json
```

All test users use the password: `password123`

Available test accounts:
- **Admin**: `admin` / `password123`
- **Donors**: `donor1`, `donor2` / `password123`
- **Delivery Staff**: `delivery1`, `delivery2` / `password123`
- **Recipients**: `recipient1`, `recipient2` / `password123`

For complete details, see the [Test Users section in SETUP.md](./SETUP.md#test-users).

### Development Environment

```bash
# Backend - activate virtual environment
cd backend
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

# Frontend - in a separate terminal
cd frontend
npm run dev
```

---

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout main
git pull origin main
git checkout -b feat/your-feature-name
```

### 2. Make Your Changes

Follow the code style guidelines and best practices outlined below.

### 3. Test Your Changes

```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests (when implemented)
cd frontend
npm test
```

### 4. Commit Your Changes

Follow the commit convention:

```bash
git add .
git commit -m "feat: add user authentication"
```

### 5. Push and Create Pull Request

```bash
git push origin feat/your-feature-name
```

Then create a pull request on GitHub.

---

## Code Style

### Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks
- `style:` - Code style changes (formatting)
- `perf:` - Performance improvements

**Examples:**
```
feat: add donation approval workflow
fix: resolve food item expiry calculation bug
docs: update API documentation
refactor: optimize warehouse inventory queries
test: add delivery staff assignment tests
chore: update dependencies
```

### Python Code Style

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line length**: 100 characters
- **Indentation**: 4 spaces
- **Imports**: Organized (standard library, third-party, local)
- **Naming**:
  - Classes: `PascalCase`
  - Functions/Variables: `snake_case`
  - Constants: `UPPER_SNAKE_CASE`

**Example:**
```python
from django.db import models
from users.models import User

class Donation(models.Model):
    """Model representing a food donation."""

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
    ]

    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def approve(self):
        """Approve the donation."""
        self.status = 'approved'
        self.save()
```

### TypeScript/React Code Style

- **Indentation**: 2 spaces
- **Naming**:
  - Components: `PascalCase`
  - Functions/Variables: `camelCase`
  - Constants: `UPPER_SNAKE_CASE`
  - Types/Interfaces: `PascalCase`
- **File naming**: `kebab-case.tsx` for components

**Example:**
```typescript
interface DonationProps {
  id: number;
  status: string;
  onApprove: () => void;
}

export function DonationCard({ id, status, onApprove }: DonationProps) {
  const handleApprove = () => {
    onApprove();
  };

  return (
    <div className="donation-card">
      <h3>Donation #{id}</h3>
      <p>Status: {status}</p>
      <button onClick={handleApprove}>Approve</button>
    </div>
  );
}
```

---

## Backend Development

### Project Structure

```
backend/
├── re_meals_api/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── <app_name>/           # Django apps
│   ├── models.py         # Database models
│   ├── views.py          # API views
│   ├── serializers.py    # DRF serializers
│   ├── urls.py           # App URLs
│   ├── admin.py          # Admin configuration
│   ├── tests.py          # Unit tests
│   └── migrations/       # Database migrations
└── manage.py
```

### Creating a New Django App

```bash
python manage.py startapp new_app

# Add to INSTALLED_APPS in settings.py
```

### Models

Define database models in `models.py`:

```python
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
```

### Serializers

Create serializers in `serializers.py`:

```python
from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
```

### Views

Create API views in `views.py`:

```python
from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
```

### URLs

Configure URLs in `urls.py`:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration SQL
python manage.py sqlmigrate <app_name> <migration_number>

# Check for migration issues
python manage.py check
```

---

## Frontend Development

### Project Structure

```
frontend/
├── app/
│   ├── layout.tsx        # Root layout
│   ├── page.tsx         # Home page
│   └── globals.css      # Global styles
├── components/          # Reusable components
├── lib/                # Utilities and helpers
├── types/              # TypeScript types
└── public/             # Static assets
```

### Creating Components

```typescript
// components/donation-list.tsx
'use client';

import { useState, useEffect } from 'react';

interface Donation {
  id: number;
  donor: string;
  status: string;
  created_at: string;
}

export function DonationList() {
  const [donations, setDonations] = useState<Donation[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/donations/')
      .then(res => res.json())
      .then(data => {
        setDonations(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div className="space-y-4">
      {donations.map(donation => (
        <div key={donation.id} className="border p-4 rounded">
          <h3>Donation #{donation.id}</h3>
          <p>Status: {donation.status}</p>
        </div>
      ))}
    </div>
  );
}
```

### API Integration

Create API utilities in `lib/api.ts`:

```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

export async function fetchDonations() {
  const response = await fetch(`${API_URL}/donations/`);
  if (!response.ok) {
    throw new Error('Failed to fetch donations');
  }
  return response.json();
}

export async function createDonation(data: any) {
  const response = await fetch(`${API_URL}/donations/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    throw new Error('Failed to create donation');
  }
  return response.json();
}
```

### Styling with Tailwind

```typescript
export function Button({ children, onClick }: { children: React.ReactNode, onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      {children}
    </button>
  );
}
```

---

## Testing

### Backend Testing

Create tests in `tests.py`:

```python
from django.test import TestCase
from .models import Restaurant

class RestaurantModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            address="123 Test St"
        )

    def test_restaurant_creation(self):
        self.assertEqual(self.restaurant.name, "Test Restaurant")
        self.assertIsNotNone(self.restaurant.created_at)

    def test_string_representation(self):
        self.assertEqual(str(self.restaurant), "Test Restaurant")
```

Run tests:

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test donation

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Frontend Testing

(To be implemented - Jest and React Testing Library)

---

## Git Workflow

### Branch Naming

- `feat/feature-name` - New features
- `fix/bug-name` - Bug fixes
- `docs/doc-name` - Documentation
- `refactor/refactor-name` - Code refactoring

### Pull Request Process

1. Create a descriptive PR title following commit convention
2. Fill out the PR template with:
   - Description of changes
   - Related issues
   - Testing performed
   - Screenshots (if UI changes)
3. Request review from team members
4. Address review comments
5. Merge after approval

---

## Common Tasks

### Adding a New API Endpoint

1. Create model in `models.py`
2. Create serializer in `serializers.py`
3. Create viewset in `views.py`
4. Register route in `urls.py`
5. Run migrations
6. Add tests
7. Update API documentation

### Adding a New Frontend Page

1. Create page in `app/page-name/page.tsx`
2. Create components in `components/`
3. Add types in `types/`
4. Implement API integration
5. Style with Tailwind CSS
6. Test functionality

### Database Schema Changes

1. Modify model in `models.py`
2. Create migration: `python manage.py makemigrations`
3. Review migration file
4. Apply migration: `python manage.py migrate`
5. Update serializers if needed
6. Update tests
7. Document changes

### Environment Variables

Add new environment variables:

1. Add to `.env.example` with placeholder
2. Add to `.env` with actual value
3. Access in Django: `os.environ.get('VAR_NAME')`
4. Access in Next.js: `process.env.NEXT_PUBLIC_VAR_NAME`

---

## Code Review Checklist

Before submitting a PR, ensure:

- [ ] Code follows style guidelines
- [ ] Tests are written and passing
- [ ] No console.log or debug prints
- [ ] Environment variables properly configured
- [ ] Documentation updated if needed
- [ ] Migrations created and tested
- [ ] No sensitive data committed
- [ ] Commit messages follow convention
- [ ] Code is DRY (Don't Repeat Yourself)
- [ ] Error handling implemented

---

## Resources

### Django & DRF
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

### Next.js & React
- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/docs)

### Tools
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)

---

## Getting Help

- Review existing documentation
- Check [GitHub Issues](https://github.com/NapatKulnarong/Re-Meals/issues)
- Ask in team discussions
- Read the source code for examples
