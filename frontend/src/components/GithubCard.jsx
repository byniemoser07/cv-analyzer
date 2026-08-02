import Card from "./Card";
import AnimatedNumber from "./AnimatedNumber";

export default function GithubCard({ data }) {
  const profile = data.profile;

  return (
    <Card title="GitHub Profile">

      <div className="github-profile">

        <img
          src={profile.avatar}
          alt={profile.username}
          className="github-avatar"
        />

        <h3>{profile.username}</h3>

        <a
          href={profile.profile_url}
          target="_blank"
          rel="noreferrer"
          className="github-link"
        >
          View Profile →
        </a>

      </div>

      <div className="github-stats">

        <div className="github-stat">

          <h2>
            <AnimatedNumber
              value={profile.public_repositories}
            />
          </h2>

          <p>Repositories</p>

        </div>

        <div className="github-stat">

          <h2>
            <AnimatedNumber
              value={profile.followers}
            />
          </h2>

          <p>Followers</p>

        </div>

        <div className="github-stat">

          <h2>
            <AnimatedNumber
              value={profile.following}
            />
          </h2>

          <p>Following</p>

        </div>

      </div>

      <div className="languages-section">

        <h4>Top Languages</h4>

        <div className="pill-container">

          {data.top_languages.map((lang) => (

            <span
              key={lang}
              className="language-pill"
            >
              {lang}
            </span>

          ))}

        </div>

      </div>

      <div className="repo-section">

        <h4>Repositories</h4>

        {data.repositories.map((repo) => (

          <div
            key={repo.name}
            className="repo-card"
          >

            <div>

              <strong>{repo.name}</strong>

              <p>{repo.language}</p>

            </div>

            <span>
                ⭐ {repo.stars}
            </span>

          </div>

        ))}

      </div>

    </Card>
  );
}