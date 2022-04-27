import React from 'react';

function TextBubble(props) {
  return (
    <div className="textbubble">
      <div>
        <div className="py-1 px-2 bg-purple-700 text-white rounded-lg w-fit">
          <a>{props.id}</a>
          <a>{props.sender}: </a>
          <a>{props.message}</a>
        </div>
      </div>
    </div>
  )
}

export default TextBubble;
