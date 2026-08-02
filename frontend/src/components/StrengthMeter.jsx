import Card from "./Card";
import AnimatedNumber from "./AnimatedNumber";

export default function StrengthMeter({ meter }) {

  return (

    <Card title="Strength Analysis">

      {Object.entries(meter).map(([skill, value]) => (

        <div
          key={skill}
          className="strength-item"
        >

          <div className="strength-header">

            <span>{skill}</span>

            <span>

              <AnimatedNumber
                value={value}
              />

              %

            </span>

          </div>

          <div className="progress-bar">

            <div
              className="progress-fill"
              style={{
                width: `${value}%`
              }}
            />

          </div>

        </div>

      ))}

    </Card>

  );

}