FROM python:2.7.13
MAINTAINER Carlos Huamani <carlos.hs.92@gmail.com>
ENV VERSION 1.0

# App name
ENV APP_NAME app

ENV APP_PATH /app

# Install SciKit Learn
RUN pip install -U scikit-learn
RUN pip install -U scipy

# App Folder
RUN mkdir -p $APP_PATH \
    && chmod -R 775 $APP_PATH

WORKDIR $APP_PATH

# Expose default port
EXPOSE 5000

# Expose default port
CMD python