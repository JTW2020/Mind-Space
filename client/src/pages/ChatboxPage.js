import React from 'react';

import Chatbox from "./components/chatbox_components/Chatbox"

const ChatboxPage = () => {
  
  return(
    <div className="HomePage text-white font-bold">
      <div className="flex flex-col items-center justify-center w-100">
        <div className="text-center">
          <h1 className="
            text-6xl 
            font-bold">
            Eliza
          </h1>
          <p className="mt-2">Mind-Space. A modern take on human emotional interaction.</p>
        </div>
        <Chatbox/>
      </div>
    </div>
  )
}

export default ChatboxPage;
