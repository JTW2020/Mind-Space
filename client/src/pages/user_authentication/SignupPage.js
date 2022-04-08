import React from 'react';

function SignupPage() {
  return (
    <div className="">
      <div>
        <h1>Signup</h1>
        <form>
          <label>Username</label>
          <input type="text" />
          <label>Password</label>
          <input type="password" />
          <input type="submit" />
        </form>
      </div>
    </div>
  )
}

export default SignupPage;