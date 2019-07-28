import React from 'react';
import ReactDOM from 'react-dom';
import HomePage from './components/HomePage'
const appContainer = {
    width: '100%',
    height: '100%',
    display: 'flex',
    justifyContent: 'center',
    flexDirection: 'row',
    backgroundColor: '#f6f6f6'
}
ReactDOM.render(
    <div style={appContainer} >
        <HomePage />
    </div>
, document.getElementById('root'));


