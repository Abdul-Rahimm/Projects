import './App.css';

// functional component
const App = () => { 

  const name = "Rahim";
  const isNameShowing = 1; 
  // different display based on different dynamic nice

  return (
    // classname is a different
    //class is reserved in java
    <div className="App">
      <h1>Hello, {isNameShowing ? (
        <>
          <h3>{name}!</h3>
        </>
      ) : (
        <>
          <h2>There is no name!</h2>
        </>
      )} </h1>
    </div>
  );
}

export default App;

// dynamcally rendering real data inside browser
// react frarment
// things need to be wrapped in react fragmenets
