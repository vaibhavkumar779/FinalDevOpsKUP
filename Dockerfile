FROM python:3.8
COPY . /app
WORKDIR /app
ARG USERNAME=vk
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME 
#RUN groupadd -r $USERNAME && useradd -r $USERNAME -g $USERNAME
USER $USERNAME
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "wsgi:app"]