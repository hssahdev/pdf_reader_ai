import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  Avatar,
} from "@chatscope/chat-ui-kit-react";

import { useState } from "react";

export default function Chatbot() {
  const [messages, setMessages] = useState([
    {
      message: "Ask me any question",
      isAI: true,
    },
  ]);

  const messageElements = messages.map((message, index) => {
    return (
      <Message
        key={index}
        model={{
          message: message.message,
          direction: message.isAI ? "incoming" : "outgoing",
        }}
      >
        {message.isAI && (
          <Avatar
            name="Emily"
            src="https://chatscope.io/storybook/react/assets/emily-xzL8sDL2.svg"
          />
        )}
      </Message>
    );
  });

  function handleSend(message) {
    setMessages((prevMessages) => [...prevMessages, { message, isAI: false }]);

    fetch(`http://localhost:8000/invoke/`, {
        method: 'POST',
        body: JSON.stringify({
            'message' : message
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
      })
      .then((response) => response.json())
      .then((data) => {
        setMessages((prevMessages) => [
          ...prevMessages,
          { message: data.message, isAI: true },
        ]);
      })
      .catch((error) => {
        console.error("Error sending message:", error);
      });
  }

  return (
    <div>
      <MainContainer>
        <ChatContainer>
          <MessageList>{messageElements}</MessageList>
          <MessageInput
            placeholder="Type message here"
            onSend={(msg) => handleSend(msg)}
            attachButton={false}
          />
        </ChatContainer>
      </MainContainer>
    </div>
  );
}
