FROM alpine:latest

# Update and install required packages
RUN apk update && apk upgrade
RUN apk add --no-cache gcc python3-dev musl-dev linux-headers git py3-pip ffmpeg

# Install megatools and verify its presence
RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ megatools && \
    megadl --version && \
    megals --version && \
    megaget --version

WORKDIR /app/
COPY . .

# Install Python dependencies
RUN pip3 install -U -r requirements.txt

# Debug information
RUN echo "Python version:" && python3 --version && \
    echo "Module structure:" && \
    ls -la /app && \
    ls -la /app/megadl && \
    ls -la /app/megadl/modules && \
    echo "Megatools version:" && megadl --version

# Set environment variable to ensure module imports work
ENV PYTHONPATH=/app

# Run the bot
CMD ["python3", "-m", "megadl"]
