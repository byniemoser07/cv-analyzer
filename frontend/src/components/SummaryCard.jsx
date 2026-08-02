import Card from "./Card";

export default function SummaryCard({ summary }) {
  return (
    <Card title="AI Summary">
      <p>{summary}</p>
    </Card>
  );
}