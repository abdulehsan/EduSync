const BACKEND_URL = "https://edusync-1iju.onrender.com/chat";
// const BACKEND_URL = "http://localhost:8000/chat";

export async function sendMessage(message, onChunk) {
    const response = await fetch(BACKEND_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        const chunk = decoder.decode(value, { stream: true });
        onChunk(chunk);
    }
}
