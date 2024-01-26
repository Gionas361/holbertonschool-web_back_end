#!/usr/bin/node
function getResponseFromAPI() {
    function getResponseFromAPI() {
        return new Promise((resolve, reject) => {
          // Simulating an asynchronous operation, like an API call
          setTimeout(() => {
            const success = true; // Change this based on your actual API response

            if (success) {
              // Resolve the promise with the desired data
              resolve({ data: "API response data" });
            } else {
              // Reject the promise with an error
              reject(new Error("API request failed"));
            }
          }, 1000); // Simulating a 2-second delay
        });
      }
}
