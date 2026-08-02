export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        🤖 AI Resume Analyzer
      </div>

      <ul className="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#upload">Analyze</a></li>
        <li><a href="#dashboard">Dashboard</a></li>
      </ul>
    </nav>
  );
}