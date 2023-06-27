package main

import (
	"encoding/json"
    "fmt"
    "log"
    "net/http"
	"os"
)

func main() {
    fmt.Println("Server started")
    http.HandleFunc("/", hello)
    log.Fatal(http.ListenAndServe(":9999", nil))
}

func getMessageFromENV() string {
	message, exists := os.LookupEnv("MESSAGE")
	if exists {
		return message
	}
	return "No Message defined. You can set environment variable 'MESSAGE'"
}


func hello(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)

	your_message := getMessageFromENV()

	response := struct {
		AppType string `json:"app_type"`
		Message string `json:"message"`
	}{
		AppType:  "golang-backend",
		Message: your_message,
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	err := json.NewEncoder(w).Encode(response)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}