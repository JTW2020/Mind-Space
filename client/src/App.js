import './App.css';
import './index.css'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';

import HomePage from './pages/HomePage';
import SignupPage from './pages/user_authentication/SignupPage';
import LoginPage from './pages/user_authentication/LoginPage';

import Layout from './pages/components/Navbar';

function App() {
  return (
    <Layout>
      <div className="App bg-black h-screen">
        <Router>
          <Switch>
            <Route path="/signup"><SignupPage /></Route>
            <Route path="/"><HomePage /></Route>
          </Switch>
        </Router>
      </div>
    </Layout>
  );
}

export default App;
