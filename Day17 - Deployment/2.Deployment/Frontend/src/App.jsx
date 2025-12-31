import { useEffect, useState } from "react";

function App() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("https://yogeshchavan.pythonanywhere.com/users")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Failed to fetch users");
        }
        return res.json();
      })
      .then((data) => setUsers(data))
      .catch((err) => {
        console.error(err);
        setError("Error fetching users");
      });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>User List</h2>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {users.length === 0 && !error && <p>No users found</p>}

      {users.map((user) => (
        <p key={user.id}>
          {user.name} - {user.email}
        </p>
      ))}
    </div>
  );
}

export default App;
