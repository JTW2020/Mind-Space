import React from 'react';

// This will serve as a general layout for the entire site
// It is made to be reused in potentially all pages
const Layout = ({ children }) => {
  <div className="Layout bg-black">
    <main>{children}</main>
  </div>
}

export default Layout;