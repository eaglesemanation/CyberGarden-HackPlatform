FROM golang:alpine AS builder
RUN apk update && apk add --no-cache git
WORKDIR $GOPATH/src/mypackage/myapp/
COPY . .
#less MB then the last
#RUN GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o /go/bin/hello
RUN ls -la
#RUN go build main.go

#FROM alpine
#COPY --from=builder /go/bin/hello /go/bin/hello
ENTRYPOINT ["/go/bin/hello"]