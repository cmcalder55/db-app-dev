import Versions from './components/Versions'
// import electronLogo from './assets/electron.svg'
import ChooseLevel from './components/Dropdowns'
import Graph from './components/Graph'
import { data } from './data/test'

function App() {
  const ipcHandle = () => window.electron.ipcRenderer.send('ping')

  return (
    <>
      {/* <img alt="logo" className="logo" src={electronLogo} /> */}
      <div className="text">Labyrinth Map</div>
      <div>
        <Graph data={data} />
      </div>
      <ChooseLevel></ChooseLevel>
      <div className="actions">
        <div className="action">
          <a href="https://electron-vite.org/" target="_blank" rel="noreferrer">
            Documentation
          </a>
        </div>

        <div className="action">
          <a target="_blank" rel="noreferrer" onClick={ipcHandle}>
            Send IPC
          </a>
        </div>
      </div>
      <Versions></Versions>
    </>
  )
}

export default App
