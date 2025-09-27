import { useState } from "react";

export default function App() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hello 👋 How are you feeling today?" },
  ]);
  const [input, setInput] = useState("");
  const [mood, setMood] = useState("");

  const sendMessage = async () => {
    if (!input) return;

    // User message
    const userMsg = { sender: "user", text: input };
    setMessages([...messages, userMsg]);

    // Call backend /chat API
    const res = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();
    const botMsg = { sender: "bot", text: data.reply };
    setMessages((prev) => [...prev, botMsg]);

    setInput("");
  };

  const submitMood = async () => {
    if (!mood) return;
    await fetch("http://127.0.0.1:5000/mood", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mood }),
    });
    alert("Mood recorded!");
    setMood("");
  };

  return (
    <div className="min-h-screen bg-blue-50 flex flex-col items-center p-6">
      <h1 className="text-3xl font-bold mb-4">AI Mental Health Buddy</h1>

      <div className="w-full max-w-md bg-white p-4 rounded-2xl shadow-lg">
        <div className="h-64 overflow-y-auto border p-2 rounded mb-4">
          {messages.map((m, i) => (
            <p
              key={i}
              className={`mb-2 ${
                m.sender === "bot" ? "text-blue-600" : "text-gray-800"
              }`}
            >
              <b>{m.sender}:</b> {m.text}
            </p>
          ))}
        </div>

        <div className="flex mb-4">
          <input
            className="flex-grow border rounded px-3 py-2 mr-2"
            placeholder="Type your message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <button
            onClick={sendMessage}
            className="bg-blue-500 text-white px-4 py-2 rounded-lg"
          >
            Send
          </button>
        </div>

        <div className="flex mb-2">
          <input
            type="number"
            min="1"
            max="10"
            placeholder="Rate your mood (1-10)"
            value={mood}
            onChange={(e) => setMood(e.target.value)}
            className="flex-grow border rounded px-3 py-2 mr-2"
          />
          <button
            onClick={submitMood}
            className="bg-green-500 text-white px-4 py-2 rounded-lg"
          >
            Submit Mood
          </button>
        </div>
      </div>
    </div>
  );
}
