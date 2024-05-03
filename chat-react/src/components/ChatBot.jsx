import {
  MinChatUiProvider,
  MainContainer,
  MessageInput,
  MessageContainer,
  MessageList,
  TypingIndicator,
} from "@minchat/react-chat-ui";

import { useState } from "react";

const colorSet = {
  // input
  // "--input-background-color": "#FF0000",
  // "--input-text-color": "#fff",
  // "--input-element-color": "rgb(0, 0, 255)",
  // "--input-attach-color": "#fff",
  // "--input-send-color": "#fff",
  // "--input-placeholder-color": "rgb(255, 255, 255)",

  // // message header
  // "--message-header-background-color": "#FF0000",
  // "--message-header-text-color": "#fff",
  // "--message-header-last-active-color": "rgb(0, 0, 255)",
  // "--message-header-back-color": "rgb(255, 255, 255)",

  // // chat list header
  // "--chatlist-header-background-color": "#FF0000",
  // "--chatlist-header-text-color": "rgb(255, 255, 255)",
  // "--chatlist-header-divider-color": "rgb(0, 128, 0)",

  // //chatlist
  // "--chatlist-background-color": "blue",
  // "--no-conversation-text-color": "rgb(255, 255, 255)",

  // //chat item
  // "--chatitem-background-color": "rgb(0, 0, 255)",
  // "--chatitem-selected-background-color": "rgb(255, 255, 0)",
  // "--chatitem-title-text-color": "#FF0000",
  // "--chatitem-content-text-color": "#FF0000",
  // "--chatitem-hover-color": "#FF0000",

  // //main container
  // "--container-background-color": "rgb(255, 192, 203)",

  // //loader
  // "--loader-color": "rgb(0, 128, 0)",

  // //message list
  "--messagelist-background-color": "#222",
  // "--no-message-text-color": "rgb(255, 255, 255)",

  // // incoming message
  "--incoming-message-text-color": "white",
  // "--incoming-message-name-text-color": "rgb(255, 255, 255)",
  // "--incoming-message-background-color": "rgb(0, 128, 0)",
  // "--incoming-message-timestamp-color": "rgb(255, 255, 255)",
  // "--incoming-message-link-color": "#FF0000",

  // //outgoing message
  "--outgoing-message-text-color": "white",
  // "--outgoing-message-background-color": "rgb(255, 255, 0)",
  // "--outgoing-message-timestamp-color": "#FF0000",
  // "--outgoing-message-checkmark-color": "#FF0000",
  // "--outgoing-message-loader-color": "#FF0000",
  // "--outgoing-message-link-color": "rgb(0, 128, 0)",
};

export default function Chatbot(props) {
  const [messages, setMessages] = useState([
    {
      text: "Ask me any question",
      user: {
        id: "ai",
        name: "AI",
      },
    },
  ]);

  const [showTyping, setShowTyping] = useState(false);

  function handleSend(message) {
    setMessages((prevMessages) => [
      ...prevMessages,
      {
        text: message,
        user: {
          id: "self",
          name: "Self",
        },
      },
    ]);

    if (props.selectedFile.document_id === null) {
      setMessages((prevMessages) => [
        ...prevMessages,
        {
          text: "Please upload a document first",
          user: {
            id: "ai",
            name: "AI",
          },
        },
      ]);
      return;
    }

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
          {
            text: data.message,
            user: {
              id: "ai",
              name: "AI",
            },
          },
        ]);
        setShowTyping(false);
      })
      .catch((error) => {
        console.error("Error sending message:", error);
      });
  }

  return (
    <div className="chat-container">
      <MinChatUiProvider theme="grey" colorSet={colorSet} isTyping={true}>
        <MainContainer style={{ height: "50vh" }}>
          <MessageContainer>
            <MessageList currentUserId="self" messages={messages} />
            {showTyping && <TypingIndicator />}
            <MessageInput
              placeholder="Type message here"
              showAttachButton={false}
              onSendMessage={handleSend}
            />
          </MessageContainer>
        </MainContainer>
      </MinChatUiProvider>
    </div>
  );

}
