# Constroi o frontend
FROM node:14 AS frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Constroi o backend
FROM python:3.8 AS backend
WORKDIR /app/backend
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt
COPY backend/ .

COPY --from=frontend /app/frontend/build /app/backend/static

EXPOSE 8000

# Variáveis de ambiente
ENV DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@localhost:5432/${DB_NAME}

# Comando para iniciar o app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]