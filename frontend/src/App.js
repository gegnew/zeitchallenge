import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";
import InputForm from "./routes/InputForm";
import Login from "./routes/Login";

function App() {
  return (
    <div className="h-screen">
      <Router>
        <div className="u-h-full-minus-top-nav">
          <Switch>
            <Route exact path="/login" component={Login} />
            <Route exact path="/count" component={InputForm} />
            <Route render={() => <Redirect to="/count" />} />
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;
