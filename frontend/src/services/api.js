import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 120000,
});

export const analyzeResume = async (
  file,
  jobDescription,
  githubUsername
) => {
  const formData = new FormData();

  formData.append("file", file);
  formData.append("job_description", jobDescription);
  formData.append("github_username", githubUsername);

  const response = await API.post(
    "/analyze-profile",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

export default API;