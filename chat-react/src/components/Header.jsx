// Header.js
import React from 'react';

const Header = (props) => {
  return (
    <div className="header-container">
      <input type="file" onChange={props.handleFileChange} />
      <button onClick={props.handleSubmit}>Upload</button>
    </div>
  );
};

export default Header;
