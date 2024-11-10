import React, { useState } from 'react';
import ChatWindow from './ChatWindow';
import MessageInput from './MessageInput';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);

  const sendMessage = async (content) => {
    if (content.trim()) {
      // Add the user's message to the chat
      setMessages([...messages, { sender: 'user', content }]);
  
      try {
        // Make the API call asynchronously
        const response = await fetch('http://127.0.0.1:5001/api/message', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: content }),
        });
        console.log(response);
        // Check if the response is successful
        if (!response.ok) {
          throw new Error('Server error');
        }
  
        // Parse the JSON response
        const data = await response.json();
        console.log(data);
        // Update messages with the bot's response
        setMessages((prevMessages) => [
          ...prevMessages,
          { sender: 'bot', content: data.response },
        ]);
      } catch (error) {
        console.error('Error:', error);
  
        // Handle error (e.g., server error or fetch issue)
        setMessages((prevMessages) => [
          ...prevMessages,
          { sender: 'bot', content: error.message },
        ]);
      }
    }
  };
  

  return (
    <div className="App">
      <ChatWindow messages={messages} />
      <MessageInput sendMessage={sendMessage} />
    </div>
  );
}

export default App;
