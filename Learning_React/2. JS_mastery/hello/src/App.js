import { useState, useEffect } from "react";
import "./App.css";

// using hooks for states
// events

const App = () => {
    const [counter, setCounter] = useState(0);
    const [ count, setCount ] = useState(0);

    useEffect(() => {
        // alert("This happens as soon as this component is rendered")
        setCounter(10);
    }, [count])
    // dependency array will make sure that the code only happens at the initiation
    //whenever count is changed. it will set counter to 0
    
  return (
    <div className="App">
        <button onClick = {() => setCounter((prev) => prev - 1 )}>-</button>
        <h1>{counter}</h1>
        <button onClick = {() => setCounter((prev) => prev + 1 )}>+</button>
        <br></br>
        <button onClick = {() => setCount((prev) => prev - 1 )}>-</button>
        <h1>{count}</h1>
        <button onClick = {() => setCount((prev) => prev + 1 )}>+</button>
    </div>
  );
};

export default App;
