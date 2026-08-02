import { useState } from "react";
import Card from "./Card";

export default function InterviewQuestions({ questions }) {

  const [open, setOpen] = useState(null);

  return (

    <Card title="Interview Questions">

      <div className="questions-list">

        {questions.map((question, index) => (

          <div
            key={index}
            className="question-card"
          >

            <button
              className="question-header"
              onClick={() =>
                setOpen(open === index ? null : index)
              }
            >

              <span>

                {index + 1}. {question}

              </span>

              <span>

                {open === index ? "−" : "+"}

              </span>

            </button>

            {open === index && (

              <div className="question-body">

                <p>

                  Think about how you would answer this
                  using your own projects, internship,
                  achievements and practical experience.

                </p>

              </div>

            )}

          </div>

        ))}

      </div>

    </Card>

  );

}