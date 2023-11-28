import './App.css';

// functional component
const App = () => { 

  const name = "Rahim";
  const isNameShowing = 0; 
  // different display based on different dynamic nice

  return (
    // classname is a different
    //class is reserved in java
    <div className="App">
      <h1>Hello, {isNameShowing ? name : "someone"}! </h1>
    </div>
  );
}

export default App;

// dynamcally rendering real data inside browser
