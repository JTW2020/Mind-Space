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
        <div className="mt-6">
          <label>Your input:</label>
          <br />
          <input className="text-black w-full mt-5" />
        </div>
      </div>
    </div>
  )
}

export default HomePage;