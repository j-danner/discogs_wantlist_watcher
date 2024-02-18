FROM python:3.12.1-alpine
WORKDIR /discogs_wantlist_watcher
COPY . /discogs_wantlist_watcher
ENV FLASK_APP=index.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN python3 -m pip install -r requirements.txt --break-system-packages && apk update && apk add cairo cups-libs dbus-libs eudev-libs expat flac gdk-pixbuf glib libgcc libjpeg-turbo libpng libwebp libx11 libxcomposite libxdamage libxext libxfixes tzdata libexif udev xvfb zlib-dev chromium chromium-chromedriver
EXPOSE 5000
CMD ["flask", "run"]

