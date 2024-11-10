import React from 'react';
import './ChatWindow.css';

function ChatWindow({ messages }) {
  return (
    <div className="chat-window">
      {messages.map((msg, index) => (
        <div
          key={index}
          className={`message ${msg.sender === 'user' ? 'user' : 'bot'}`}
        >
          {msg.content}
        </div>
      ))}
    </div>
  );
}

export default ChatWindow;
