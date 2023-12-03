// import { MouseEvent } from "react";

import { useState } from "react";

function ListGroup() {
  const items = ["new york", "pakistan", "karachi"];

  // event handler
  // const handleClick = (event: MouseEvent) => console.log(event);

  // data or state that might change over time
  const [selectedIndex, setSelectedIndex] = useState(-1);

  return (
    <>
      <h1>Unordered List</h1>
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            key={item}
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            onClick={() => {
              setSelectedIndex(index);
            }}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
