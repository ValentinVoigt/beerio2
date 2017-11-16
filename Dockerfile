FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip install -e ".[testing]"
RUN nodeenv node_env
ENV PATH="/app/node_env/bin:${PATH}"
RUN npm install
RUN /app/node_modules/webpack/bin/webpack.js
RUN pytest

EXPOSE 6543

CMD ["pserve", "production.ini"]
