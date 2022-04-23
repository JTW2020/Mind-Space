import React from 'react';

import Navbar from './Navbar';

const Layout = ({ children }) => {
  return (
    <>
      <div className="">
        <Navbar />
        <main className="pt-12 pb-10">{children}</main>
      </div>
    </>
  )
}

export default Layout;
