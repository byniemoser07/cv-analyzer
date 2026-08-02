import Card from "./Card";

export default function ResumeTips({ tips }) {

  return (

    <Card title="Resume Tips">

      <div className="tips-list">

        {tips.map((tip, index) => (

          <div
            key={index}
            className="tip-card"
          >

            <div className="tip-icon">

              ✔

            </div>

            <p>{tip}</p>

          </div>

        ))}

      </div>

    </Card>

  );

}