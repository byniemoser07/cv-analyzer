import Card from "./Card";

export default function SalaryCard({ salary }) {
  return (
    <Card title="Salary Prediction">

      <h2>{salary.range}</h2>

      <p>
        <strong>Experience Level:</strong> {salary.level}
      </p>

    </Card>
  );
}