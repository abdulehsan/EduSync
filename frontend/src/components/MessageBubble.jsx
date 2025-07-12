import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function MessageBubble({ text, sender }) {
  return (
    <div className={`message ${sender}`}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          p: ({ children }) => <p className="markdown-text">{children}</p>,
        }}
      >
        {text}
      </ReactMarkdown>
    </div>
  );
}
