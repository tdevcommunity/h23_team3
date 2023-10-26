import { LinkButtonSecondary } from "@/components/ui/linkButton"
import Image from "next/image"

export default function MentorDetails() {
    return <section className="bg-gray-100 w-full h-screen ">
        <div className='w-full h-40 bg-xmentor/10 flex-col  justify-center  flex items-center '>

        </div>
        <div className="w-6/12 mx-auto -mt-20 p-5   bg-white">
            <div className="flex  justify-between items-center">
                <div className="flex items-center gap-10 ">
                    <div className="my-5 ">
                        <Image className='w-24 rounded-full h-24 object-cover  ' width={100} height={100} alt="" src="/assets/mentors/mentor1.jpg" />
                    </div>
                    <div>
                        <div className='text-2xl font-semibold group-hover:underline duraiton-300 group-hover:text-xmentor'> ODANOU Massahoud </div>
                        <div>Full stack developer </div>
                        <div>
                            <span className='py-1 px-4 mt-2 bg-green-100 rounded-full text-sm  inline-flex items-center gap-2 '>
                                <span className='h-2 w-2 inline-block  rounded-full  bg-green-600'>
                                </span>
                                <span>
                                    Disponbile
                                </span>
                            </span>
                        </div>
                    </div>
                </div>
                <div>
                    <LinkButtonSecondary href={""}>
                        Message
                    </LinkButtonSecondary>
                </div>
            </div>
            <div>
                <span>ABOUT</span>
                <p className="text-sm text-gray-500">
                    Experienced (15+ years) developer and friendly Ruby on Rails and React/Next.js/Redux Developer/Mentor (with passion for helping others learn) | ★ 3,520+ 5 ★ sessions/jobs. 7+ years on top of the Codementor Ranking ★
                </p>
                <button className="text-xmentor">Voir plus </button>
            </div>
            <div className="mt-5">
                <span>EXPERTISE</span>
                <div>
                    <div className="mt-2">
                        <div className="text-md font-medium"> Flutter</div>
                        <div className="text-sm flex gap-2  text-gray-500 ">
                            <span>11 ans d'expérience </span> |
                            <span>10 sessions </span>
                        </div>
                        <div className="mt-2">
                            <div className="text-md font-medium   "> Node js</div>
                            <div className="text-sm flex gap-2  text-gray-500 ">
                                <span>11 ans d'expérience </span> |
                                <span>10 sessions </span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <div className="mt-5">
                <span>AViS  </span>
                <div>


                </div>

            </div>
        </div>
    </section>

}
