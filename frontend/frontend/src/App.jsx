import { useState } from "react";
import axios from "axios";

function App() {
  const [isSignup, setIsSignup] = useState(false);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [dashboard, setDashboard] = useState(null);
  const [error, setError] = useState("");

  const handleAuth = async () => {
    try {
      setError("");

      if (isSignup) {
        await axios.post("http://127.0.0.1:8000/api/auth/signup", {
          name,
          email,
          password,
          role: "admin",
        });

        alert("Signup success 🚀 Now login");
        setIsSignup(false);
        return;
      }

      const res = await axios.post(
        "http://127.0.0.1:8000/api/auth/login",
        { email, password }
      );

      const token = res.data.token;
      localStorage.setItem("token", token);

      alert("Login success 🚀");

      fetchDashboard(token);
    } catch (err) {
      console.log(err.response?.data);
      setError(err.response?.data?.detail || "Something went wrong");
    }
  };

  const fetchDashboard = async (token) => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/api/dashboard", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setDashboard(res.data);
    } catch (err) {
      setError("Failed to load dashboard");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>{isSignup ? "Signup" : "Login"}</h2>

      {isSignup && (
        <>
          <input
            placeholder="Name"
            onChange={(e) => setName(e.target.value)}
          />
          <br /><br />
        </>
      )}

      <input
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
      />
      <br /><br />

      <input
        placeholder="Password"
        type="password"
        onChange={(e) => setPassword(e.target.value)}
      />
      <br /><br />

      <button onClick={handleAuth}>
        {isSignup ? "Signup" : "Login"}
      </button>

      <p
        style={{ cursor: "pointer", color: "blue" }}
        onClick={() => setIsSignup(!isSignup)}
      >
        {isSignup
          ? "Already have an account? Login"
          : "New user? Signup"}
      </p>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {dashboard && (
        <div style={{ marginTop: 20 }}>
          <h3>Dashboard 📊</h3>
          <p>Total Tasks: {dashboard.total_tasks}</p>
          <p>Completed: {dashboard.completed_tasks}</p>
          <p>Pending: {dashboard.pending_tasks}</p>
          <p>Overdue: {dashboard.overdue_tasks}</p>
        </div>
      )}
    </div>
  );
}

export default App;