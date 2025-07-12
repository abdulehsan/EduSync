import { useState, useRef, useEffect } from "react";
import { sendMessage } from "./api/chatApi";
import MessageBubble from "./components/MessageBubble";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);

    setInput("");
    setLoading(true);

    const botMessage = { sender: "bot", text: "" };
    setMessages((prev) => [...prev, botMessage]);

    await sendMessage(input, (chunk) => {
      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1].text += chunk;
        return updated;
      });
    });

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="chat-container">
        {messages.map((msg, idx) => (
          <MessageBubble key={idx} sender={msg.sender} text={msg.text} />
        ))}
        <div ref={chatEndRef} />
      </div>

      <div className="input-container">
        <input
          placeholder="Send a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          disabled={loading}
        />
        <button onClick={handleSend} disabled={loading}>
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
