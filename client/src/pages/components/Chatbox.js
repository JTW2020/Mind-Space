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
      const res = await axios.post('http://localhost:5000/api/msgEliza', {
        userMessage: message
      });
      console.log(res.data);
      setMessageList([
        ...messageList,
        { user: "client", message: message },
        { user: "Eliza", message: res.data.message }
      ]);
      console.log(messageList);
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div className="chatbox">
      <div className="flex flex-col items-center justify-center absolute inset-0">
        <div className="">
          <div className="text-center">
            <h1 className="
            text-6xl 
            font-bold">
              Mind-Space
            </h1>
            <p className="mt-2">Welcome to Mind-Space. A modern take on Eliza.</p>
          </div>
        </div>
        <div className="container py-2 px-4 mt-10 w-8/12 text-black bg-zinc-100 h-4/12 rounded rounded-md">
          <a>Eliza: Is something troubling you?</a>
          <br />
          <a>You: I am depressed.</a>
          <br />
          <a>Eliza: What do you think is causing this?</a>
        </div>
        <form className="flex mt-6 items-center justify-center align-middle">
          <div className="mr-4">
            <label className="pr-3">You:</label>
            <input className="text-black w-full" onChange={handleMsgInputChange} />
          </div>
          <div>
            <button className="bg-purple-500 mt-4 rounded rounded-sm py-1 px-4" onClick={handleSubmitMsg}>
              Send to Eliza
            </button>
          </div>
        </form>
      </div>
    </div >
  )
}

export default Chatbox;