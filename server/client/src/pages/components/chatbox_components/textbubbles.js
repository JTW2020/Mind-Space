import React from 'react';

function TextBubble(props) {
  return (
    <div className="textbubble">
      <div>
        <div className="p-1 bg-purple-700 text-white rounded-lg w-7/12">
          <a>{props.id}</a>
          <a>{props.sender}: </a>
          <a>{props.message}</a>
        </div>
      </div>
    </div>
  )
}

export default TextBubble;