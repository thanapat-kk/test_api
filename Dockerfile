# ใช้ Python image
FROM python:3.9

# ตั้งค่า working directory
WORKDIR /app

# คัดลอกไฟล์ requirements.txt เพื่อระบุ dependencies
COPY requirements.txt requirements.txt

# ติดตั้ง dependencies
RUN pip install -r requirements.txt

# คัดลอกไฟล์ทั้งหมดไปยัง container
COPY . .

# เปิด port สำหรับ Flask
EXPOSE 5000

# ระบุให้ container รองรับการรัน Flask หรือ unittest ได้
CMD ["python", "api_test.py"]