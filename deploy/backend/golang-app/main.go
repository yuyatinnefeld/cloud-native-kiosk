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

func getAppNameFromENV() string {
	app_name, exists := os.LookupEnv("APP_NAME")
	if exists {
		return app_name
	}
	return "DEMO APP"
}


func hello(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)

	app_name := getAppNameFromENV()

	response := struct {
		AppName string `json:"app_name"`
		Message string `json:"message"`
	}{
		AppName:  app_name,
		Message: "message 123!",
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	err := json.NewEncoder(w).Encode(response)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}