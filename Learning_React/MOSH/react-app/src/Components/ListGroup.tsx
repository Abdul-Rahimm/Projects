import { MouseEvent } from "react";

function ListGroup() {
  const items = ["new york", "pakistan", "karachi"];
  // event handler
  const handleClick = (event: MouseEvent) => console.log(event);

  return (
    <>
      <h1>Unordered List</h1>
      <ul className="list-group">
        {items.map((item) => (
          <li key={item} className="list-group-item" onClick={handleClick}>
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
