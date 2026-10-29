
FROM python:3.12-slim

WORKDIR /app

COPY ["Student Grading.py", "/app/Student Grading.py"]

CMD ["python", "/app/Student Grading.py"]
