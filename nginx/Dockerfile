FROM debian:stretch-slim

ARG buildDeps="nginx"

RUN apt-get update && apt-get install -y $buildDeps nano curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy nginx configs
COPY ./confs/nginx.conf /etc/nginx/nginx.conf
COPY ./confs/nginx/ /etc/nginx/conf.d/

CMD ["/bin/bash", "-c", "service nginx start && tail -f /var/log/nginx/*.log"]
