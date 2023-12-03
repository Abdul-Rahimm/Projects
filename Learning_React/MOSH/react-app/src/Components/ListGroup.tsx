function ListGroup() {
  const items = ["new york", "pakistan", "karachi"];

  return (
    <>
      <h1>Unordered List</h1>
      <ul className="list-group">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
