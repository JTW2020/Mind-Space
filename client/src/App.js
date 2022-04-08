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

import Layout from './pages/components/layout';

function App() {
  return (
    <Router>
      <Layout>
        <div className="App">
          <Switch>
            <Route path="/signup" component={SignupPage} />
            <Route path="/"><HomePage /></Route>
          </Switch>
        </div>
      </Layout>
    </Router>
  );
}

export default App;
