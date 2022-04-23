import './App.css';
import './index.css'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';

import HomePage from './pages/HomePage';
import ChatboxPage from './pages/ChatboxPage';
import SignupPage from './pages/user_authentication/SignupPage';
import LoginPage from './pages/user_authentication/LoginPage';
import AboutPage from './pages/AboutPage';

import Layout from './pages/components/layout';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-black">
        <Layout>
          <Switch>
            <Route path="/about" component={AboutPage}/>
            <Route path="/chat" component={ChatboxPage}/>
            <Route path="/signup" component={SignupPage} />
            <Route path="/login" component={LoginPage} />
            <Route path="/"><HomePage /></Route>
          </Switch>
        </Layout>
      </div>
    </Router>
  );
}

export default App;
