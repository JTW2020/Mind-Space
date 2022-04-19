import React from 'react';

import Navbar from './Navbar';

const Layout = ({ children }) => {
  return (
    <>
      <div className="">
        <Navbar />
        <main className="pt-6">{children}</main>
      </div>
    </>
  )
}

export default Layout;
