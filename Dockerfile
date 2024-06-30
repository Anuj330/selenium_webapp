ARG PORT=443
FROM cypress/included:latest
RUN apt-get update && apt-get install -y python3
RUN echo $(python3 -m site --user-base)
COPY requirements.txt .
ENV PATH /home/root/.local/bin:${path}
RUN apt-get update && apt-get install -y gcc python3-dev libffi-dev libssl-dev && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
