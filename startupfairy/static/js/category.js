import React from 'react';
import ReactDOM from 'react-dom';
import {EntityLink, TwitterLink, WebsiteLink} from 'links';

function displayCategories() {
  ReactDOM.render(
    <Griddle results={data} showSettings={false} columns={columns} columnMetadata={columnMetadata}/>,
      document.getElementById('table-content')
  );
}

module.exports = displayCategories;
  