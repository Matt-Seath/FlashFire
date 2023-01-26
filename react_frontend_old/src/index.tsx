import * as React from "react";
import * as ReactDOM from "react-dom";
import App from "./components/App";

function Root() {
    return (
        <div>
            <App />
        </div>
    )
}
ReactDOM.render(<Root />, document.getElementById('root'))