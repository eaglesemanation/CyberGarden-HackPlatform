FROM golang:alpine AS builder
RUN apk update && apk add --no-cache git
WORKDIR $GOPATH/src/mypackage/myapp/

COPY . .
#RUN GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o /go/bin/hello
#RUN go build -o /go/bin/hello
ENTRYPOINT ["go", "run", "main.go"]
#FROM alpine
#COPY --from=builder /go/bin/hello /go/bin/hello
#COPY --from=builder /go/bin/hello/keys.json /go/bin/hello/keys.json
#ENTRYPOINT ["/go/bin/hello"]