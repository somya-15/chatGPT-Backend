# chatGPT-Backend
This code provides a Python backend implementation for a text completion chatbot API using the OpenAI API. It receives user input through a POST request and generates a response using OpenAI's text completion model. Additionally, it includes a mock functionality to simulate the API call and response for testing purposes.

Setup and Dependencies
To run this code, you need to install the required dependencies. Ensure you have Python installed on your system and follow these steps:

Install the necessary packages by running the following command:

```pip install quart quart-cors openai```

Set up your OpenAI API key by assigning it to the OPENAI_API_KEY environment variable.

### Usage
1. Import the required modules and set up the necessary configurations.

2. Define the user_input object that holds the user's phone number and message.

3. Set the OpenAI API key using openai.api_key.

4. Define the /incomingMessage endpoint as a POST request handler in Quart.

5. Inside the incoming_message function, retrieve the user's input from the request body and update the user_input object.

6. If the user's message is "Hi", generate a response from the chatbot as a user greeting. Otherwise, proceed with mocking the API response.

7. When mocking the API response, create a mock object to simulate the API response with desired attributes such as choices and status_code.

8. Use the mock.patch context manager to patch the openai.Completion.create method and return the mock response.

9. Call the incoming_message_mock function to generate the response based on the mocked API call.

10. Extract the generated response from the mocked API response.

11. Return the response and the status code in the JSON format.

12. Define the incoming_message_mock function that handles the mocked API call using openai.Completion.create. It generates a response based on the provided input and returns the response text and status code.

13. Define the main function to start the Quart application.

14. Run the application by executing the main function.

### Endpoint
The API exposes the following endpoint:

POST /incomingMessage
This endpoint receives user input as a JSON payload in the request body. The input should contain a "message" field representing the user's message. It returns a JSON response with the generated chatbot response and a status code.

If the user's message is "Hi", the chatbot responds with a greeting. Otherwise, it generates a response using the OpenAI API or returns a mocked response based on the mocking configuration.

Running the Application
To run the application, execute the Python script. The API server will start running on http://0.0.0.0:5002.

```python main.py```

Note: The API server should be accessible from the configured allow_origin URL, which is set to https://chat.openai.com in this code. Modify the allow_origin parameter if you want to use a different URL.

Mocking the API
The code includes a mocking functionality for testing purposes. The API call to openai.Completion.create is intercepted and replaced with a mock response. The mock response is configured with a predefined response text and a status code. To use the actual OpenAI API, you can replace the mocked code with the original API call.

Ensure that you use the mocking functionality responsibly and respect OpenAI's terms of use.
