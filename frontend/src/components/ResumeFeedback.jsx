import Card from "./Card";

export default function ResumeFeedback({ feedback }) {

  return (

    <Card title="AI Resume Feedback">

      <div className="feedback-grid">

        <div className="feedback-box success">

          <h3>✅ Strengths</h3>

          <ul>

            {feedback.strengths.map((item) => (

              <li key={item}>{item}</li>

            ))}

          </ul>

        </div>

        <div className="feedback-box warning">

          <h3>⚠ Weaknesses</h3>

          <ul>

            {feedback.weaknesses.map((item) => (

              <li key={item}>{item}</li>

            ))}

          </ul>

        </div>

        <div className="feedback-box info">

          <h3>🚀 Improvements</h3>

          <ul>

            {feedback.improvements.map((item) => (

              <li key={item}>{item}</li>

            ))}

          </ul>

        </div>

      </div>

    </Card>

  );

}