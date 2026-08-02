import Card from "./Card";
import AnimatedNumber from "./AnimatedNumber";

export default function ATSCard({ data }) {

  const items = [
    {
      label: "Contact",
      value: data.breakdown.contact,
      max: 10,
    },
    {
      label: "Skills",
      value: data.breakdown.skills,
      max: 25,
    },
    {
      label: "Education",
      value: data.breakdown.education,
      max: 10,
    },
    {
      label: "Experience",
      value: data.breakdown.experience,
      max: 25,
    },
    {
      label: "Projects",
      value: data.breakdown.projects,
      max: 20,
    },
    {
      label: "Keywords",
      value: data.breakdown.keywords,
      max: 10,
    },
  ];

  return (

    <Card title="ATS Score">

      <div className="ats-score">

        <AnimatedNumber
          value={data.overall_score}
        />

        <span>/100</span>

      </div>

      {items.map((item) => (

        <div
          key={item.label}
          className="progress-item"
        >

          <div className="progress-header">

            <span>{item.label}</span>

            <span>{item.value}</span>

          </div>

          <div className="progress-track">

            <div
              className="progress-fill"
              style={{
                width: `${(item.value / item.max) * 100}%`,
              }}
            />

          </div>

        </div>

      ))}

    </Card>

  );

}