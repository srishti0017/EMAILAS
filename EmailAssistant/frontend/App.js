import React, { useState } from 'react';

function App() {
  const [email, setEmail] = useState('');
  const [summary, setSummary] = useState('');
  const [actions, setActions] = useState('');
  const [reply, setReply] = useState('');
  const [isSpam, setIsSpam] = useState(null);

  const handleSummarize = async () => {
    const response = await fetch('http://localhost:5000/summarize', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email }),
    });
    const data = await response.json();
    setSummary(data.summary);
  };

  const handleDetectActions = async () => {
    const response = await fetch('http://localhost:5000/detect_action', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email }),
    });
    const data = await response.json();
    setActions(data.actions);
  };

  const handleGenerateReply = async () => {
    const response = await fetch('http://localhost:5000/generate_reply', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email }),
    });
    const data = await response.json();
    setReply(data.reply);
  };

  const handleDetectSpam = async () => {
    const response = await fetch('http://localhost:5000/detect_spam', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email }),
    });
    const data = await response.json();
    setIsSpam(data.is_spam);
  };

  return (
    <div className="App">
      <h1>Email Assistant</h1>
      <textarea
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Paste your email here"
      ></textarea>
      <button onClick={handleSummarize}>Summarize</button>
      <button onClick={handleDetectActions}>Detect Actions</button>
      <button onClick={handleGenerateReply}>Generate Reply</button>
      <button onClick={handleDetectSpam}>Detect Spam</button>

      <h2>Summary:</h2>
      <p>{summary}</p>

      <h2>Actions:</h2>
      <p>{actions}</p>

      <h2>Suggested Reply:</h2>
      <p>{reply}</p>

      <h2>Spam Detection:</h2>
      <p>{isSpam === null ? '' : isSpam ? 'This is spam!' : 'This is not spam.'}</p>
    </div>
  );
}

export default App;
