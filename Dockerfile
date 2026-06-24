# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --upgrade pip


RUN pip install -r requirements.txt


COPY . .


CMD ["python","bot.py"]

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
