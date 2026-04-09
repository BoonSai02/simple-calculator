FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy backend code
COPY backend/ ./backend/

# Install dependencies
RUN cd backend && uv pip install -e .

# Expose port
EXPOSE 8000

# Run API
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]