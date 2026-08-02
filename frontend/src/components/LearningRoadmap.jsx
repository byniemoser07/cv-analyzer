import Card from "./Card";

export default function LearningRoadmap({ roadmap }) {

  return (

    <Card title="Learning Roadmap">

      <div className="roadmap">

        {roadmap.map((step) => (

          <div
            key={step.step}
            className="roadmap-item"
          >

            <div className="roadmap-circle">

              {step.step}

            </div>

            <div className="roadmap-content">

              <h3>{step.skill}</h3>

              <span className="roadmap-status">

                {step.status}

              </span>

            </div>

          </div>

        ))}

      </div>

    </Card>

  );

}