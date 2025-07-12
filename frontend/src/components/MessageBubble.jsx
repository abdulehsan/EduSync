import ReactMarkdown from "react-markdown";

export default function MessageBubble({ message, isUser }) {
  return (
    <div className={`bubble ${isUser ? "user" : "bot"}`}>
      <ReactMarkdown>{message}</ReactMarkdown>
    </div>
  );
}
