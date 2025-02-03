# Faculty Hours Faculty Service

## Overview
The Faculty Hours Faculty Service is a microservice component of the Faculty Hours system, responsible for managing faculty-related operations. It provides RESTful API endpoints for handling faculty data and interactions.

## Tech Stack
- **Python 3.11+**
- **FastAPI**: Modern web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **PostgreSQL**: Database backend
- **RabbitMQ**: Message broker for service communication
- **Docker**: Containerization
- **Poetry**: Dependency management
- **Uvicorn**: ASGI server
- **Authlib**: Authentication library

## Prerequisites
- Python 3.11 or higher
- Docker and Docker Compose
- Poetry package manager
- PostgreSQL database
- RabbitMQ server

## Setup and Installation

### Local Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd faculty-hours-faculty
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Configure the required environment variables

4. Run the service:
```bash
poetry run uvicorn faculty.main:app --host 0.0.0.0 --port 8100 --reload
```

### Docker Setup

1. Build and run using Docker Compose:
```bash
docker-compose -f .docker/docker-compose.yml up --build
```

The service will be available at `http://localhost:8100`

## Service Connections

The service interacts with:
- **PostgreSQL Database**: Stores faculty data and related information
- **RabbitMQ**: Message broker for inter-service communication
- **Report Service**: Connects via port 8200 for report generation
- **Other Faculty Hours System Services**: Through API endpoints

## API Endpoints

The service exposes RESTful API endpoints under the `/faculty` prefix:
- Faculty data management
- Integration with other system components

## Environment Variables

Key environment variables required:
- Database connection settings
- RabbitMQ configuration
- Authentication settings
- Service URLs and ports
