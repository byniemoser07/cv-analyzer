import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import UploadForm from "../components/UploadForm";
import Dashboard from "./Dashboard";
import useResume from "../hooks/useResume";

export default function Home() {

  const { resumeData } = useResume();

  return (
    <>
      <Navbar />

      <Hero />

      <section id="upload">
        <UploadForm />
      </section>

      {resumeData && (
        <section id="dashboard">
          <Dashboard />
        </section>
      )}
    </>
  );
}