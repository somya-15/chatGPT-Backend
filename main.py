import json
import os
from unittest import mock
import quart
import quart_cors
from quart import request
import openai

# Note: Setting CORS to allow chat.openapi.com is only required when running a localhost plugin
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

user_input = {"userPhoneNumber": "91...", "message": "Hi"}

openai.api_key = os.getenv("OPENAI_API_KEY")


# this is a post request to OpenAI API for sending the user input to the text completion model
@app.post("/incomingMessage")
async def incoming_message():
    request_body = await request.get_json(force=True)
    user_input["message"] = request_body.get(
        "message"
    )  # Update the user_input message with the request body value

    if user_input["message"].lower() == "hi":
        # Generate a response from the chatbot as a user greeting
        response_text = "Hello! How can I assist you today?"
    else:
        # Mocking the API response
        mock_response = mock.Mock()
        mock_response.choices[0].text.strip.return_value = "Mocked response"
        mock_response.status_code = 200

        # Mocking the OpenAI API call
        with mock.patch("openai.Completion.create") as mock_create:
            mock_create.return_value = mock_response

            response = (
                incoming_message_mock()
            )  # Call the modified method for mocking purposes

        response_text = response[
            "response"
        ]  # Extract the generated response from the mocked API response

    return quart.jsonify({"response": response_text, "status_code": 200})


# Modified method for mocking purposes
def incoming_message_mock():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"User: {user_input['message']}\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " User:"],
    )

    return {
        "response": response.choices[0].text.strip(),
        "status_code": response.status_code,
    }


def main():
    app.run(debug=True, host="0.0.0.0", port=5002)


if __name__ == "__main__":
    main()
