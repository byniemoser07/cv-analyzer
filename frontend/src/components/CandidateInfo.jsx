import Card from "./Card";

export default function CandidateInfo({ data }) {

  return (

    <Card title="Candidate Profile">

      <div className="candidate-profile">

        <div className="candidate-avatar">

          {data.name?.charAt(0)}

        </div>

        <div className="candidate-info">

          <h2>{data.name}</h2>

          <p>{data.email}</p>

          <p>{data.phone}</p>

        </div>

      </div>

      <div className="skills-section">

        <h3>Technical Skills</h3>

        <div className="pill-container">

          {data.skills.map((skill) => (

            <span
              key={skill}
              className="skill-pill"
            >
              {skill}
            </span>

          ))}

        </div>

      </div>

      <div className="candidate-grid">

        <div>

          <h3>Education</h3>

          <ul>

            {data.education.map((item) => (

              <li key={item}>{item}</li>

            ))}

          </ul>

        </div>

        <div>

          <h3>Projects</h3>

          <ul>

            {data.projects.slice(0,4).map((item) => (

              <li key={item}>{item}</li>

            ))}

          </ul>

        </div>

      </div>

    </Card>

  );

}