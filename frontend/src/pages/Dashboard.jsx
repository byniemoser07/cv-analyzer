import useResume from "../hooks/useResume";

import CandidateInfo from "../components/CandidateInfo";
import ATSCard from "../components/ATSCard";
import GithubCard from "../components/GithubCard";
import JobMatchCard from "../components/JobMatchCard";
import SummaryCard from "../components/SummaryCard";
import DashboardStats from "../components/DashboardStats";
import StrengthMeter from "../components/StrengthMeter";
import ResumeFeedback from "../components/ResumeFeedback";
import LearningRoadmap from "../components/LearningRoadmap";
import SalaryCard from "../components/SalaryCard";
import ResumeTips from "../components/ResumeTips";
import InterviewQuestions from "../components/InterviewQuestions";
import ScoreOverview from "../components/ScoreOverview";
import Charts from "../components/Charts";

export default function Dashboard() {
  const { resumeData } = useResume();

  if (!resumeData) return null;

  return (
    <div className="dashboard">

      {/* ================= Dashboard Header ================= */}

      <div className="dashboard-header">

        <div>

          <h1 className="dashboard-title">
            Resume Analysis Dashboard
          </h1>

          <p className="dashboard-subtitle">
            AI Powered Resume Evaluation & Career Insights
          </p>

        </div>

      </div>

      {/* ================= Overall Score ================= */}

      <ScoreOverview
        score={resumeData.overall_score}
        grade={resumeData.grade}
        hiring={resumeData.hiring_recommendation}
      />

      {/* ================= Candidate Information ================= */}

      <CandidateInfo
        data={resumeData.candidate}
      />

      {/* ================= ATS • Job Match • GitHub ================= */}

      <div className="grid-three">

        <ATSCard
          data={resumeData.ats}
        />

        <JobMatchCard
          data={resumeData.job_match}
        />

        <GithubCard
          data={resumeData.github}
        />

      </div>

      {/* ================= AI Summary ================= */}

      <SummaryCard
        summary={resumeData.summary}
      />

      {/* ================= Analytics Charts ================= */}

      <Charts
        data={resumeData}
      />

      {/* ================= Strength + Dashboard ================= */}

      <div className="grid-two">

        <StrengthMeter
          meter={resumeData.strength_meter}
        />

        <DashboardStats
          stats={resumeData.dashboard}
        />

      </div>

      {/* ================= Salary + Learning Roadmap ================= */}

      <div className="grid-two">

        <SalaryCard
          salary={resumeData.salary_prediction}
        />

        <LearningRoadmap
          roadmap={resumeData.learning_roadmap}
        />

      </div>

      {/* ================= Resume Feedback ================= */}

      <ResumeFeedback
        feedback={resumeData.resume_feedback}
      />

      {/* ================= Resume Tips ================= */}

      <ResumeTips
        tips={resumeData.resume_tips}
      />

      {/* ================= Interview Questions ================= */}

      <InterviewQuestions
        questions={resumeData.interview_questions}
      />

    </div>
  );
}