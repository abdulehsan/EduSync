import { marked } from "marked";

export default function MessageBubble({ sender, text }) {
  const isUser = sender === "user";

  return (
    <div
      className={`message ${sender}`}
      dangerouslySetInnerHTML={{ __html: marked.parse(text) }}
    />
  );
}
