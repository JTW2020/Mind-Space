import logo from './logo.svg';
import './App.css';
import './index.css'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from 'react-router-dom';

import HomePage from './pages/HomePage';

function App() {
  return (
    <Router>
      <div className="App">
      </div>
      <Switch>
        <Route path="/"><HomePage /></Route>
      </Switch>
    </Router>
  );
}

export default App;
