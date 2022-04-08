import React, { useState } from 'react';
import axios from 'axios';

function SignupPage() {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSignup = (e) => {
    e.preventDefault();
    if (password === confirmPassword) {
      try {

      } catch (err) {

      }
    }
  }

  return (
    <div className="flex justify-center text-white">
      <div className="space-y-2.5 border-2 px-8 py-4 rounded-md">
        <h1 className="text-center font-semibold text-3xl">
          Signup
        </h1>
        <form className="space-y-4" onSubmit={handleSignup}>
          <div className="space-y-1">
            <div className="font-semibold">
              <label className="">Username</label>
            </div>
            <input
              className="text-black text-xl py-2 px-2 rounded-md w-72"
              type="text"
              name="username"
              onChange={(e) => setUsername(e.target.value)} />
          </div>
          <div className="space-y-1">
            <div className="font-semibold">
              <label>Password</label>
            </div>
            <input
              className="text-black text-xl py-2 px-2 rounded-md w-72"
              type="password"
              name="password"
              onChange={(e) => setPassword(e.target.value)} />
          </div>
          <div>
            <div className="font-semibold">
              <label>Verify Password</label>
            </div>
            <input
              className="text-black text-xl py-2 px-2 rounded-md w-72"
              type="password"
              name="confirmPassword"
              onChange={(e) => setConfirmPassword(e.target.value)} />
          </div>
          <div className="flex justify-center">
            <input
              className="bg-green-600 hover:bg-green-700 hover:cursor-pointer py-2 px-8 rounded-md"
              type="submit"
              value="Signup"
              onSubmit={handleSignup} />
          </div>
        </form>
      </div>
    </div>
  )
}

export default SignupPage;