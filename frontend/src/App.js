import React from 'react';
import ChargeForm from './components/ChargeForm';
import logo from './assets/kanastra_logo.jpeg';
import './App.scss';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} alt="Logo" />
        <h1>Hello, Kanastra!</h1>
        <ChargeForm />
      </header>
    </div>
  );
}

export default App;