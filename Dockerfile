# Node.jsの公式イメージをベースにする
FROM node:14
USER root

# Pythonをインストールする
RUN apt-get update && apt-get install -y python3 python3-pip python3-setuptools

# ロケールの設定
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

# vimとlessのインストール
RUN apt-get install -y vim less
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

# Pythonの依存関係をインストール
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# 作業ディレクトリの設定
WORKDIR /app

# Node.jsの依存関係をインストール
COPY package*.json ./
RUN npm install

# アプリケーションコードをコピー
COPY . .

# デフォルトコマンドとしてシェルを起動
CMD ["sh"]