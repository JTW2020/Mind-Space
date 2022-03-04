import React, { useState, useEffect } from 'react';
import axios from 'axios';

import TextBubble from './textbubbles';

function Chatbox() {
  const [message, setMessage] = useState("");
  const [messageList, setMessageList] = useState([]);

  function handleMsgInputChange(e) {
    e.preventDefault();
    setMessage(e.target.value);
  }

  /*
    This is the handler method that sends 
    the user's message to the backend
  */
  async function handleSubmitMsg(e) {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:5000/api/msgEliza', {
        userMessage: message
      });
      setMessageList([
        ...messageList,
        { user: "You", message: message },
        { user: "Eliza", message: res.data.message }
      ]);
      console.log(messageList);
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div className="chatbox grid grid-cols-1 w-3/6">
      <div className="p-2 mt-5 text-black h-60 bg-zinc-100 rounded-md overflow-auto">
        <a className="text-sm italic">Type something to talk to Eliza.</a>
        <br />
        <div>
          {messageList.map((message) => <TextBubble key={message.id} sender={message.user} message={message.message} />)}
        </div>
      </div>
      <form
        className="flex mt-6 items-center justify-center align-middle"
        onSubmit={e => handleSubmitMsg(e)}>
        <div className="w-full">
          <label className="">You:</label>
          <input
            className="text-black rounded-sm w-full p-2"
            onChange={e => { handleMsgInputChange(e) }}
          />
        </div>
      </form>
      <button className="bg-purple-500 mt-4 rounded-sm py-1 px-4" onClick={e => { handleSubmitMsg(e) }}>
        Send to Eliza
      </button>
    </div>
  )
}

export default Chatbox;