FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    openjdk-17-jdk zip unzip build-essential \
    git git-lfs \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev libncurses5-dev libncursesw5-dev \
    libffi-dev liblzma-dev \
    libjpeg-dev libpng-dev \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up Python environment
RUN python3 -m pip install --upgrade pip setuptools wheel

# Install buildozer and build tools
RUN python3 -m pip install --no-cache-dir \
    buildozer \
    cython==0.29.34 \
    kivy==2.2.0 \
    kivymd==0.104.2

WORKDIR /app

# Copy project files
COPY . /app

# Build the APK
CMD ["buildozer", "-v", "android", "debug"]
