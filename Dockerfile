FROM alpine:latest

RUN apk update && apk upgrade
RUN apk add --no-cache gcc python3-dev musl-dev linux-headers git py3-pip ffmpeg
# Install megatools from edge/testing repo and verify it exists
RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ megatools && \
    which megadl && \
    which megaget && \
    which megals

WORKDIR /app/
COPY . .
RUN pip3 install -U -r requirements.txt

# Print debug info
RUN python3 --version && \
    ls -la /app/megadl/modules/

CMD ["python3", "-m", "megadl"]
