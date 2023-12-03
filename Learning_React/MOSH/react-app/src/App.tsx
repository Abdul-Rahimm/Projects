import ListGroup from "./Components/ListGroup";

function App() {
  const items = ["new york", "pakistan", "karachi"];

  return (
    <div>
      <ListGroup items={items} heading="cities" />
    </div>
  );
}

export default App;
