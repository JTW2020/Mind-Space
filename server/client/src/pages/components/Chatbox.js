import React, { useState } from 'react';
import axios from 'axios';

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
      const res = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/api/msgEliza`, {
        userMessage: message
      });
      console.log(res.data);
      setTimeout(function () {
        setMessageList([
          ...messageList,
          { user: "client", message: message },
          { user: "Eliza", message: res.data.message }
        ]);
      }, 3000)
      console.log(messageList);
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div className="chatbox grid grid-cols-1 w-3/6">
      <div className="py-2 px-4 mt-5 text-black h-60 bg-zinc-100 rounded-md overflow-auto">
        <a>Eliza: How are you?</a>
        <br />
        <a>You: I am depressed.</a>
        {/**
         * This is just testing the overflox attribute of the chatbox
         * Thankfully, it works
         */}
      </div>
      <form className="flex mt-6 items-center justify-center align-middle">
        <div className="w-full">
          <label className="">You:</label>
          <input className="text-black rounded-sm w-full p-2" onChange={handleMsgInputChange} />
        </div>
      </form>
      <button className="bg-purple-500 mt-4 rounded-sm py-1 px-4" onClick={handleSubmitMsg}>
        Send to Eliza
      </button>
    </div>
  )
}

export default Chatbox;