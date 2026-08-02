import Card from "./Card";
import AnimatedNumber from "./AnimatedNumber";

export default function DashboardStats({ stats }) {

  const cards = [

    {
      title: "Technical Skills",
      value: stats.technical_skills,
      icon: "💻",
    },

    {
      title: "Projects",
      value: stats.projects,
      icon: "🚀",
    },

    {
      title: "Experience",
      value: stats.experience_entries,
      icon: "📈",
    },

    {
      title: "Education",
      value: stats.education_entries,
      icon: "🎓",
    },

    {
      title: "Repositories",
      value: stats.github_repositories,
      icon: "📦",
    },

  ];

  return (

    <Card title="Dashboard Statistics">

      <div className="stats-grid">

        {cards.map((item) => (

          <div
            className="stat-box"
            key={item.title}
          >

            <div className="stat-icon">

              {item.icon}

            </div>

            <h2>

              <AnimatedNumber
                value={item.value}
              />

            </h2>

            <p>{item.title}</p>

          </div>

        ))}

      </div>

    </Card>

  );

}