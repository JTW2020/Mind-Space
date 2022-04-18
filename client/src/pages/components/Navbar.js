import React from 'react';
import { Link } from 'react-router-dom';

/* 
  This is the link to the rocketIcon: 
    <a href="https://www.flaticon.com/free-icons/space" title="space icons">Space icons created by amonrat rungreangfangsai - Flaticon</a> 
*/


function Navbar() {

  const navigation = [
    { name: 'Home', href: 'home', id:1 },
    { name: 'Chat', href: 'chat', id:2 },
    { name: 'About', href: 'about', id:3 }
  ]

  return (
    <nav className="flex justify-between w-full items-center py-4 px-6 text-white">
      <div className="text-2xl font-extrabold hover:cursor-pointer">
        <Link to="/">
          Mind-Space
        </Link>
      </div>
      <div className="flex space-x-4 text-white font-semibold px-4">
        {navigation.map((item) => (
          <Link
            key={item.id}
            className='items-center text-center w-20 py-1 hover:cursor-pointer'
            to={`/${item.href}`}
          >
            {item.name}
          </Link>
        ))}
      </div>
      <div className="flex space-x-4">
        <div className="hover:cursor-pointer">
            <Link className='bg-gray-600 py-2 px-10 text-center rounded-lg hover:bg-gray-800' to='/signup'>Signup</Link>
        </div>
        <div className="hover:cursor-pointer">
            <Link className="bg-purple-600 py-2 px-10 text-center rounded-lg hover:bg-purple-700" to="/login">Login</Link>
        </div>
      </div>
    </nav>
  )
}

export default Navbar;
