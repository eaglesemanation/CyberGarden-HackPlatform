package tg

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

const apiUrl = "https://api.telegram.org/bot"

type SDK struct {
	Token string
}

func (sdk *SDK) Push(chatId string, msg string) {
	url := fmt.Sprintf("%s%s/sendMessage", apiUrl, sdk.Token)
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
