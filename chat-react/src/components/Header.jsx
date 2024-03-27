import React, { useState } from 'react';

const Header = (props) => {
  return (
    <div>
      <input type="file" onChange={props.handleFileChange} />
      <button onClick={props.handleSubmit}>Upload</button>
    </div>
  );
};

export default Header;