FROM nginx:alpine

COPY build/index.html /usr/share/nginx/html/index.html
COPY build/copper-wire-and-starlight.txt build/copper-wire-and-starlight.pdf /usr/share/nginx/html/
COPY chapters/ /usr/share/nginx/html/chapters/
COPY appendices/ /usr/share/nginx/html/appendices/
COPY audiobook/ /usr/share/nginx/html/audiobook/
COPY docker/audiobook-index.html /usr/share/nginx/html/audiobook/index.html
COPY docker/favicon.svg /usr/share/nginx/html/favicon.svg
