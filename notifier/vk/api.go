package vk

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

const key = "77789b9b77789b9b77789b9b82770f613c7777877789b9b17d49ced2a33f5f8d0a16b33"

type Response struct {
	Count int    `json:"count"`
	Items []Item `json:"items"`
}

type Item struct {
	Id      int    `json:"id"`
	FromId  int    `json:"from_id"`
	OwnerId int    `json:"owner_id"`
	Date    int    `json:"date"`
	Text    string `json:"text"`
}

type ResponseWrapper struct {
	Rsp Response `json:"response"`
}

//const url = 'https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN&v=V '
const apiUrl = "https://api.vk.com/method"

type SDK struct {
	Token string
}

func (sdk *SDK) WallGet(domain string) string{

	//r := req.New()
	url := fmt.Sprintf("%s/wall.get?"+
		"domain=%s&"+
		"count=2&"+
		"access_token=%s&"+
		"v=5.131",
		apiUrl, domain, sdk.Token)
	resp, err := http.Get(url + "wall.get/owner_id")
	if err != nil {
		log.Fatalln(err)
	}

	rspWpr := ResponseWrapper{}
	body, _ := ioutil.ReadAll(resp.Body)
	json.Unmarshal(body, &rspWpr)
	return rspWpr.Rsp.Items[1].Text
}

func (sdk *SDK) WallPost(owner string, message string) string{

	url := fmt.Sprintf("%s/wall.post?"+
		"owner_id=%s&"+
		"access_token=%s&"+
		"v=5.131&" +
		"from_group=1",
		apiUrl, owner, sdk.Token)
	//resp, err := http.Get(url)

	postBody, _ := json.Marshal(map[string]string{
		"message": message,
	})
	resp, err := http.Post(url, "application/json", bytes.NewBuffer(postBody))
	if err != nil {
		log.Fatalln(err)
	}

	//rspWpr := ResponseWrapper{}
	body, _ := ioutil.ReadAll(resp.Body)
	//json.Unmarshal(body, &rspWpr)
	log.Println(string(body))
	return "ss"
}