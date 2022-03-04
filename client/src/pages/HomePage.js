import React from 'react';

import Chatbox from "./components/chatbox_components/Chatbox";

function HomePage() {
  return (
    <div className="HomePage text-white font-bold">
      <div className="flex flex-col items-center justify-center absolute inset-0">
        <div className="text-center">
          <h1 className="
            text-6xl 
            font-bold">
            Mind-Space
          </h1>
          <p className="mt-2">Welcome to Mind-Space. A modern take on Eliza.</p>
        </div>
        <Chatbox />
      </div>
    </div>
  )
}

export default HomePage;