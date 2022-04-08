import React from 'react';

import Navbar from './Navbar';

const Layout = ({ children }) => {
  return (
    <>
      <div className="bg-black h-screen">
        <Navbar />
        <main className="">{children}</main>
      </div>
    </>
  )
}

export default Layout;