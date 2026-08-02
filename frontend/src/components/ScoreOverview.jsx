import Card from "./Card";
import AnimatedNumber from "./AnimatedNumber";

export default function ScoreOverview({
  score,
  grade,
  hiring,
}) {
  return (
    <div className="score-overview">

      <Card title="Overall Score">
        <div className="score-big">
          <AnimatedNumber value={score} decimals={2} />
        </div>
      </Card>

      <Card title="Grade">
        <div className="grade-big">
          {grade}
        </div>
      </Card>

      <Card title="Hiring Decision">
        <div
          className={`hiring-pill ${
            hiring === "Strong Hire"
              ? "success"
              : hiring === "Consider"
              ? "warning"
              : "danger"
          }`}
        >
          {hiring}
        </div>
      </Card>

    </div>
  );
}