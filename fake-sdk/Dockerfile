FROM alpine:3.12 as base

RUN apk add --no-cache build-base cmake git linux-headers python3 python3-dev swig
RUN git clone https://github.com/eclipse/mraa
RUN mkdir mraa/build && cd mraa/build \
	&& cmake -DBUILDSWIGPYTHON=ON .. \
	&& make all install

FROM alpine:3.12

RUN apk add --no-cache build-base cmake git python3
RUN mkdir /examples
WORKDIR /examples
COPY --from=base /usr/local/include/* /usr/include/
COPY --from=base /usr/local/lib64/* /usr/lib/
COPY --from=base /usr/local/lib/python3.8/site-packages /usr/lib/python3.8/site-packages
COPY ./entrypoint /entrypoint

ENTRYPOINT /entrypoint
