package main

import (
	tgModule "./tg"
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
)

type Keys struct {
	Vk string `json:"vk"`
	Tg string `json:"tg"`
}

func sendUpdate(keys Keys, text chan string) chan interface{} {
	tg := tgModule.SDK{Token: keys.Tg}
	go func() {
		for {
			tg.Push("-1001369787313", <-text)
			log.Println("Successfully pushed")
		}
	}()
	return make(chan interface{})
}

type Post struct {
	Message string `json:message`
}

func main() {
	file, err := ioutil.ReadFile("notifier/keys.json")
	if err != nil {
		log.Panic("Can't read file")
	}
	keys := Keys{}
	_ = json.Unmarshal([]byte(file), &keys)
	messages := make(chan string)
	sendUpdate(keys, messages)
	post := Post{}
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		reqBody, _ := ioutil.ReadAll(r.Body)
		_ = json.Unmarshal(reqBody, &post)
		messages<-post.Message
	})

	log.Fatal(http.ListenAndServe(":8080", nil))
}

