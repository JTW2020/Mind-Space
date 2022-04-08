import React from 'react';

import rocketIcon from '../../space-travel.png';

/* 
  This is the link to the rocketIcon: 
    <a href="https://www.flaticon.com/free-icons/space" title="space icons">Space icons created by amonrat rungreangfangsai - Flaticon</a> 
*/

function Navbar() {
  return (
    <nav className="flex items-center justify-between pt-2 pb-2">
      <div className="bg-white w-12 h-12 rounded-md">
        <img src={rocketIcon} alt="RocketIcon" />
      </div>
      <div>

      </div>
    </nav>
  )
}

export default Navbar;