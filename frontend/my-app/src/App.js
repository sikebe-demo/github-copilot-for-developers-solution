import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import catLogo from './cat-logo.png'; // 猫のロゴ画像をインポート

function App() {
  const [cats, setCats] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/cats')
      .then(response => {
        setCats(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the cats!', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={catLogo} className="App-logo" alt="cat logo" /> {/* 猫のロゴを表示 */}
        <h1>Cat List</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Age</th>
              <th>Breed</th>
            </tr>
          </thead>
          <tbody>
            {cats.map(cat => (
              <tr key={cat.id}>
                <td>{cat.id}</td>
                <td>{cat.name}</td>
                <td>{cat.age}</td>
                <td>{cat.breed}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </header>
    </div>
  );
}

export default App;