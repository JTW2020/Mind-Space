import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';

import TextBubble from './textbubbles';

function Chatbox() {
  const [message, setMessage] = useState("");
  const [messageList, setMessageList] = useState([
    {user: "Eliza", message: "Hello. How do you do?"}
  ]);

  function handleMsgInputChange(e) {
    e.preventDefault();
    setMessage(e.target.value);
  }

  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({behavior:"smooth"})
  }

  useEffect(() => {
    scrollToBottom()
  }, [messageList])

  /*
    This is the handler method that sends 
    the user's message to the backend
  */
  async function handleSubmitMsg(e) {
    e.preventDefault();
    try {
      const res = await axios.post('/api/msgEliza', {
        userMessage: message
      });
      setMessageList([
        ...messageList,
        { user: "Me", message: message },
        { user: "Eliza", message: res.data.message }
      ]);
      console.log(messageList);
      setMessage("");
    } catch (err) {
      console.error(err);
    }
  }


  return (
    <div className="chatbox grid grid-cols-1 w-2/6">
      <div className="p-2 mt-5 text-black h-96 bg-zinc-100 rounded-md overflow-y-scroll">
        <div className="flex flex-col h-full py-1">
          <a className="text-sm italic">Type something to talk to Eliza.</a>
          <div className="space-y-2">
            {messageList.map((message) => <TextBubble key={message.id} sender={message.user} message={message.message} />)}
          </div>
        </div>
        <div ref={messagesEndRef}/>
      </div>
      <form
        className="flex mt-6 items-center justify-center align-middle"
        onSubmit={e => handleSubmitMsg(e)}>
        <div className="w-full">
          <label className="">You:</label>
          <input
            className="text-black rounded-sm w-full p-2"
            onChange={e => { handleMsgInputChange(e) }}
            value={message}
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
