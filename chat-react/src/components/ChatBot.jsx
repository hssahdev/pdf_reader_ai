import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  Avatar,
  TypingIndicator,
} from "@chatscope/chat-ui-kit-react";

import { useState } from "react";

export default function Chatbot(props) {
  const [messages, setMessages] = useState([
    {
      message: "Ask me any question",
      isAI: true,
    },
  ]);


  const [showTyping, setShowTyping] = useState(false);
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
            src="https://img.icons8.com/papercut/60/bot.png"
          />
        )}
      </Message>
    );
  });

  function handleSend(message) {
    setMessages((prevMessages) => [...prevMessages, { message, isAI: false }]);
    setShowTyping(true);
    fetch(`http://localhost:8000/invoke/`, {
      method: "POST",
      body: JSON.stringify({
        message: message,
        document_id: props.selectedFile?.document_id,
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        setMessages((prevMessages) => [
          ...prevMessages,
          { message: data.message, isAI: true },
        ]);
        setShowTyping(false);
      })
      .catch((error) => {
        console.error("Error sending message:", error);
      });
  }

  return (
    <div>
      <MainContainer>
        <ChatContainer>
          <MessageList typingIndicator={showTyping && <TypingIndicator/>}>{messageElements}</MessageList>
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
