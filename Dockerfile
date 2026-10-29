
FROM python:3.12-slim

WORKDIR /app

COPY ["Student Grading.py", "/app/Student Grading.py"]
COPY test_student_grading.py /app/test_student_grading.py

CMD ["python", "-m", "unittest", "-v", "test_student_grading.py"]
