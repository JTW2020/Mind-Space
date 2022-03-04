import logo from './logo.svg';
import rocketIcon from './space-travel.png';
import './App.css';
import './index.css'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from 'react-router-dom';

import Navbar from './pages/components/Navbar';
import HomePage from './pages/HomePage';

function App() {
  return (
    <Router>
      <div className="App bg-black h-screen">
        <Navbar />
        <Switch>
          <Route path="/"><HomePage /></Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
