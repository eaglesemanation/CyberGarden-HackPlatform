package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)


const tgUrl = "https://api.telegram.org/bot"
type tgSDK struct {
	Token string
}

func (sdk *tgSDK) Push(chatId string, msg string) {
	url := fmt.Sprintf("%s%s/sendMessage", tgUrl, sdk.Token)
	postBody, _ := json.Marshal(map[string]string{
		"chat_id": chatId,
		"text":    msg,
	})

	body, err := http.Post(url, "application/json", bytes.NewBuffer(postBody))
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(body)
}


type Keys struct {
	Vk string `json:"vk"`
	Tg string `json:"tg"`
}

func sendUpdate(keys Keys, text chan string) chan interface{} {
	tg := tgSDK{Token: keys.Tg}
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
	file, err := ioutil.ReadFile("keys.json")
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
        fmt.Fprintf(w, "Sends message: %s", post.Message)
	})
	port := ":8080"
	log.Println("Starting server on http://0.0.0.0" + port)
	log.Fatal(http.ListenAndServe("0.0.0.0:8080", nil))
}

