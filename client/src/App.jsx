import { useState, useEffect } from 'react'
import axios from "axios"
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  // Get user location upon browser load and send to server
  useEffect(() => {
    if ("geolocation" in navigator){
    navigator.geolocation.getCurrentPosition(async (position) => {
      const userLatitude = position.coords.latitude
      const userLongitude = position.coords.longitude
      console.log(userLatitude, userLongitude)
      await axios.post('http://127.0.0.1:8080/user_location', {
        userLatitude, userLongitude
      })
      console.log("Sent user location to backend")
    })
  }
  }, [])

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
