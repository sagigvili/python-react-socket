import './App.css';
import React, { useState, useEffect } from 'react';


function MyComponent() {
  const [name, setName] = useState(0);

    useEffect(() => {
      const socket = new WebSocket('ws://127.0.0.1:5000/echo');
        socket.addEventListener('message', ({ data }) => {
        const parsed = JSON.parse(data)
        setName(parsed.Count);
      });
      return () => socket.close();
    }, []);
  
    return (
      <p>The number is {name}</p>
    );
}

function App() {
  return (
    <MyComponent></MyComponent>
  );
}

export default App;
