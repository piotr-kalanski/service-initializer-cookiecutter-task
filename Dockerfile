FROM piotrkalanski/service-initializer-base-docker

COPY task.py .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt