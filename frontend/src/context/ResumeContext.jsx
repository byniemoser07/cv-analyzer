import { createContext, useState } from "react";

export const ResumeContext = createContext();

export function ResumeProvider({ children }) {

  const [resumeData, setResumeData] = useState(null);

  const [loading, setLoading] = useState(false);

  return (
    <ResumeContext.Provider
      value={{
        resumeData,
        setResumeData,
        loading,
        setLoading,
      }}
    >
      {children}
    </ResumeContext.Provider>
  );
}