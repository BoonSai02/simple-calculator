FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy only required files
COPY backend/pyproject.toml ./backend/
COPY backend/app.py ./backend/

# Install dependencies (IMPORTANT CHANGE)
RUN cd backend && uv pip install --system -e .

# Expose port
EXPOSE 8000

# Run app
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]