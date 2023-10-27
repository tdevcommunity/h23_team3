import { LinkButton, LinkButtonOutline, LinkButtonSecondary } from "@/components/ui/linkButton";
import Image from "next/image";
import MentorProfileFrame from "@/components/ui/mentorprofileFrame"
import mentorsData from '@/data/mentors.json';

const BlockMentor: React.FC = () => {
  return (
    <section className="w-10/12 mx-auto border-black mb-20">
      <div>
        <h5 className="text-4xl font-medium py-6 text-center">
          Plus de 1000 experts à votre disposition
        </h5>
        <div className="grid grid-cols-4 gap-4">
          {mentorsData.map((mentor) => (
            <div key={mentor.id} className="h-80 w-60">
              <MentorProfileFrame
                name={mentor.name}
                profession={mentor.profession}
                stars={mentor.stars}
                image={mentor.image}
              />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default BlockMentor;
