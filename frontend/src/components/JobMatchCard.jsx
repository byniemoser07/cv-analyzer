import Card from "./Card";
import AnimatedNumber from "./AnimatedNumber";

export default function JobMatchCard({ data }) {
  return (
    <Card title="Job Match">

      <div className="job-match-score">

        <AnimatedNumber
          value={data.overall_match}
          decimals={2}
        />

        <span>%</span>

      </div>

      <div className="match-section">

        <h4>Matched Skills</h4>

        <div className="pill-container">

          {data.keyword_match.matched_skills.map((skill) => (

            <span
              key={skill}
              className="pill success-pill"
            >
              {skill}
            </span>

          ))}

        </div>

      </div>

      <div className="match-section">

        <h4>Missing Skills</h4>

        <div className="pill-container">

          {data.keyword_match.missing_skills.map((skill) => (

            <span
              key={skill}
              className="pill danger-pill"
            >
              {skill}
            </span>

          ))}

        </div>

      </div>

      {data.recommendations?.length > 0 && (

        <div className="recommendation-box">

          <strong>Recommendation</strong>

          <p>{data.recommendations[0]}</p>

        </div>

      )}

    </Card>
  );
}