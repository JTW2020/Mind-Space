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
            Eliza
          </h1>
          <p className="mt-2">Mind-Space. A modern take on human emotional interaction.</p>
        </div>
        <Chatbox />
      </div>
    </div>
  )
}

export default HomePage;