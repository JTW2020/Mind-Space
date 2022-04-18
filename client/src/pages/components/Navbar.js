import React, { Fragment } from 'react';
import rocketIcon from '../../space-travel.png';
import { Link } from 'react-router-dom';

/* 
  This is the link to the rocketIcon: 
    <a href="https://www.flaticon.com/free-icons/space" title="space icons">Space icons created by amonrat rungreangfangsai - Flaticon</a> 
*/

const navigation = [
  { name: 'Home', href: '#' },
  { name: 'Chat', href: '#' },
  { name: 'About', href: '#' },
  { name: 'Filler', href: '#' }
]

function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}

function Navbar() {
  return (
    <nav className="flex w-full items-center py-2 px-2 hover:cursor-pointer">
      <div>
        <div className="text-white text-2xl font-extrabold hover:cursor-pointer hover:bg-blue-500">Mind-Space</div>
      </div>
      <div className="">
        <div className="flex space-x-4 text-white font-semibold px-4">
          {navigation.map((item) => (
            <Link
              key={item.name}
              className='items-center text-center w-20 hover:cursor-pointer'
              to={`/${item.href}`}
            >
              {item.name}
            </Link>
          ))}
        </div>
      </div>

    </nav>
  )
}

export default Navbar;
