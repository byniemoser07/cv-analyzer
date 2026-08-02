import { useState } from "react";
import { analyzeResume } from "../services/api";
import useResume from "../hooks/useResume";
import LoadingSpinner from "./LoadingSpinner";

export default function UploadForm() {

  const {
    setResumeData,
    loading,
    setLoading,
  } = useResume();

  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [githubUsername, setGithubUsername] = useState("");
  const [error, setError] = useState("");

  async function submit(e) {

    e.preventDefault();

    setError("");

    if (!file) {
      setError("Please upload a PDF resume.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please paste the job description.");
      return;
    }

    try {

      setLoading(true);

      const data = await analyzeResume(
        file,
        jobDescription,
        githubUsername
      );

      setResumeData(data);

    } catch (err) {

      console.error(err);

      let message = "Unable to analyze your resume.";

      if (err.response) {

        switch (err.response.status) {

          case 400:
            message =
              "Please upload a valid PDF and complete all required fields.";
            break;

          case 404:
            message =
              "GitHub username not found. Resume analysis completed without GitHub data.";
            break;

          case 413:
            message =
              "The uploaded PDF is too large.";
            break;

          case 422:
            message =
              "Please complete all required fields before submitting.";
            break;

          default:
            if (err.response.status >= 500) {
              message =
                "Server error. Please try again after a few moments.";
            }

        }

      } else if (err.request) {

        message =
          "Cannot connect to the backend server. Please ensure it is running.";

      }

      setError(message);

    } finally {

      setLoading(false);

    }

  }

  return (

    <section className="upload-wrapper">

      <div className="upload-card">

        <h2>Upload Resume</h2>

        {error && (
          <div className="error-box">
            {error}
          </div>
        )}

        <form onSubmit={submit}>

          <label>Resume (PDF)</label>

          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setFile(e.target.files[0])}
          />

          <label>GitHub Username (Optional)</label>

          <input
            type="text"
            placeholder="e.g. torvalds"
            value={githubUsername}
            onChange={(e) =>
              setGithubUsername(e.target.value)
            }
          />

          <label>Job Description</label>

          <textarea
            placeholder="Paste the job description here..."
            value={jobDescription}
            onChange={(e) =>
              setJobDescription(e.target.value)
            }
          />

          <button
            type="submit"
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Analyze Resume"}
          </button>

          {loading && <LoadingSpinner />}

        </form>

      </div>

    </section>

  );

}