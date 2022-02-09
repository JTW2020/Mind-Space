import React from 'react';

function HomePage() {
  return (
    <div className="HomePage text-white font-bold">
      <div className="flex flex-col items-center justify-center absolute inset-0">
        <div className="">
          <body className="text-center">
            <h1 className="
            text-6xl 
            font-bold">
              Mind-Space
            </h1>
            <p className="mt-2">Welcome to Mind-Space. A modern take on Eliza.</p>
          </body>
        </div>
        <div className="container py-2 px-4 mt-10 w-4/12 text-black bg-zinc-100 h-4/12 rounded rounded-md">
          <a>Eliza: Is something troubling you?</a>
          <br />
          <a>You: I am depressed.</a>
          <br />
          <a>Eliza: What do you think is causing this?</a>
        </div>
        <div className="flex mt-6 items-center justify-center align-middle">
          <div className="mr-4">
            <label className="pr-3">You:</label>
            <input className="text-black w-full" />
          </div>
          <div className="">
            <button className="bg-purple-500 mt-4 rounded rounded-sm py-1 px-4">
              Send to Eliza
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default HomePage;