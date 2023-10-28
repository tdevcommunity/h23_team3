import { LinkButton, LinkButtonOutline, LinkButtonSecondary } from "@/components/ui/linkButton";
import Image from "next/image";
import MentorProfileFrame from "@/components/ui/mentorprofileFrame"
import mentorsData from '@/data/mentors.json';
import SliderCard from "@/components/ui/sliderCard";
import StarRating from "@/components/ui/starRating";
import Link from "next/link";
import { LanguageIcon } from "@/components/icon/icons";
const BlockMentor: React.FC = () => {
  return (
    <section className="w-10/12 mx-auto border-black mb-20">
      <div>
        <h5 className="text-4xl font-medium py-8 text-center">
          Plus de 1000 <span className="text-xmentor">experts</span> à votre <br/> disposition
        </h5>
        <div className="grid grid-cols-2 place-items-center gap-4">
          {mentorsData.map((mentor,index ) => (
             <Link key={index} passHref href={"/mentors/1"}>
             <div key="index" className='flex group bg-white hover:bg-blue-50 rounded-md duration-300 hover:cursor-pointer hover:border-xmentor hover:hover-2  border mb-6 px-5  py-6  '>
                 <div className='w-5/6 '>
                     <div className='flex gap-4   items-end pb-5  '>
                         <span className='text-2xl font-semibold group-hover:underline duraiton-300 group-hover:text-xmentor'> {mentor.name} </span>
                         <span className='flex '>
                             <StarRating rating={mentor.stars} /> {mentor.stars}
                         </span>
                         <span className='py-1 px-4 rounded-full  bg-xmentor/10 text-sm text-black'>1000 reviews </span>
                     </div>
                     <div className=' text-xl font-medium'>
                         {mentor.profession}
                     </div>
                     <div className='flex gap-5 py-2 text-sm '>
                         <span className='flex gap-1'>   <LanguageIcon /> Français,Anglais</span>
                         <span> 10 Sessions</span>
                     </div>
                     <p className='text-sm '>
                         I am an experienced full stack developer 15 years in the field with consistent knowledge in developing web portals with expertise in all opensource of PHP like Wordpress , Opencart, Oscommerce...
                     </p>
                     <div className='flex gap-3 pt-4 '>
                         {
                             mentor?.stack?.map((skill, index) => (
                                 <p key={index} className="px-2 text-sm   py-1 bg-gray-200 ">{skill}</p>
                             ))
                         }


                     </div>
                 </div>
                 <div className='w-1/6 flex  justify-center items-center gap-5 flex-col'>
                     <Image className='w-24 object-cover rounded-full h-24  ' width={100} height={100} alt="" src={mentor.image} />
                     <div>
                         {mentor.isBusy ? (
                             <span className='py-1 px-4 bg-green-100 rounded-full text-sm  inline-flex items-center gap-2 '>
                                 <span className='h-2 w-2 inline-block  rounded-full  bg-green-600'>
                                 </span>
                                 <span>
                                     Disponible
                                 </span>
                             </span>
                         ) : (
                             <span className='py-1 px-4 bg-red-100 rounded-full text-sm  inline-flex items-center gap-2 '>
                                 <span className='h-2 w-2 inline-block  rounded-full  bg-red-600'>
                                 </span>
                                 <span>
                                     Occupée
                                 </span>
                             </span>
                         )}

                     </div>
                 </div>

             </div>
        </Link>
          ))}
        </div>
        <div className="flex justify-center gap-4">
                    <LinkButton href="/mentors">
                       Voir plus
                    </LinkButton>
                    <LinkButtonOutline href="">
                        Devenir Mentor
                    </LinkButtonOutline>
                </div>
      </div>
    </section>
  );
};

export default BlockMentor;
