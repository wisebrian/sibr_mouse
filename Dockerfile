FROM python:3.10
WORKDIR /app
ADD . ./app
RUN git clone https://github.com/pimoroni/explorer-hat
RUN cd explorer-hat/library && python setup.py install
RUN pip install flask websockets explorerhat smbus
EXPOSE 5001:5000
EXPOSE 6316:6316
CMD [ "python3", "./app.py" ]
CMD [ "python3", "./server.py" ]