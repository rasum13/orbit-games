# Orbit Games
A FastAPI game store app powered by PostgreSQL and Jinja2 Templates.
## Prerequisites
Before setting up the project, ensure that you have the following installed:
- Git
- Docker and Docker Compose
## Getting Started
### Clone the repository
```sh
git clone https://github.com/rasum13/orbit-games.git
cd orbit-games
```
### Configure environment variables
Create a `.env` file in the root directory based on `.env.example`;
```sh
cp .env.example .env
```
Update the values inside `.env`:
```sh
POSTGRES_USER=admin
POSTGRES_PASSWORD="your_secure_password"
POSTGRES_DB=orbit_games
POSTGRES_SERVER=db
POSTGRES_PORT=5432
```
Replace `your_secure_password` with a password of your choice.
## Running with Docker
### Start the Containers
Run the application services and the PostgreSQL database:
```sh
docker compose up -d --build
```
### Apply Database Migrations
```sh
docker exec server alebmic upgrade head
```
### Seed Initial Data
Populate the database withe example data:
```
docker exec server python -m scripts.seed
```
