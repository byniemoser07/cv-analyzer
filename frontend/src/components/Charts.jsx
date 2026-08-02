import Card from "./Card";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  CartesianGrid,
  XAxis,
  YAxis,
} from "recharts";

export default function Charts({ data }) {

  const ats = [
    {
      name: "Contact",
      value: data.ats.breakdown.contact,
    },
    {
      name: "Skills",
      value: data.ats.breakdown.skills,
    },
    {
      name: "Education",
      value: data.ats.breakdown.education,
    },
    {
      name: "Experience",
      value: data.ats.breakdown.experience,
    },
    {
      name: "Projects",
      value: data.ats.breakdown.projects,
    },
    {
      name: "Keywords",
      value: data.ats.breakdown.keywords,
    },
  ];

  const comparison = [
    {
      name: "ATS",
      score: data.ats.overall_score,
    },
    {
      name: "Job Match",
      score: data.job_match.overall_match,
    },
    {
      name: "GitHub",
      score: data.github.github_score,
    },
    {
      name: "Overall",
      score: data.overall_score,
    },
  ];

  const COLORS = [
    "#2563eb",
    "#0ea5e9",
    "#22c55e",
    "#f59e0b",
    "#ef4444",
    "#8b5cf6",
  ];

  return (

    <div className="charts-grid">

      <Card title="ATS Breakdown">

        <ResponsiveContainer
          width="100%"
          height={300}
        >

          <PieChart>

            <Pie
              data={ats}
              dataKey="value"
              outerRadius={100}
              label
            >

              {ats.map((entry, index) => (

                <Cell
                  key={index}
                  fill={COLORS[index]}
                />

              ))}

            </Pie>

            <Tooltip />

          </PieChart>

        </ResponsiveContainer>

      </Card>

      <Card title="Score Comparison">

        <ResponsiveContainer
          width="100%"
          height={300}
        >

          <BarChart data={comparison}>

            <CartesianGrid
              strokeDasharray="3 3"
            />

            <XAxis dataKey="name" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="score"
              fill="#2563eb"
              radius={[8,8,0,0]}
            />

          </BarChart>

        </ResponsiveContainer>

      </Card>

    </div>

  );

}