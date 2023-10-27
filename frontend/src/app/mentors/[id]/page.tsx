"use client"
import { LinkButtonSecondary } from "@/components/ui/linkButton"
import Image from "next/image"
import mentorsData from '@/data/mentors.json';
import useState from 'react'

export default function MentorDetails({ params }: {
    params: { id: string }
}) {
    const selectedMentor = mentorsData.filter((mentor) => mentor.id === parseInt(params.id))[0];
    return <section className="bg-gray-100 w-full h-screen ">
        <div className='w-full h-40 bg-xmentor/10 flex-col  justify-center  flex items-center '>

        </div>
        <div className="w-6/12 mx-auto -mt-20 p-5   bg-white">
            <div className="flex  justify-between items-center">
                <div className="flex items-center gap-10 ">
                    <div className="my-5 ">
                        <Image className='w-24 rounded-full h-24 object-cover  ' width={100} height={100} alt="" src={`${selectedMentor.image}`} />
                    </div>
                    <div>
                        <div className='text-2xl font-semibold group-hover:underline duraiton-300 group-hover:text-xmentor'>{selectedMentor.name} </div>
                        <div>{selectedMentor.profession} </div>
                        <div>
                            <span className={`py-1 px-4 rounded-full text-sm inline-flex items-center gap-2 ${selectedMentor.isBusy ? 'bg-red-100' : 'bg-green-100'}`}>
                                <span className={`h-2 w-2 inline-block rounded-full ${selectedMentor.isBusy ? 'bg-red-700' : 'bg-green-700'}`}></span>
                                <span>
                                    {selectedMentor.isBusy ? (
                                        <p>Indisponible</p>
                                    ) : (
                                        <p>Disponible</p>
                                    )}
                                </span>
                            </span>
                        </div>
                    </div>
                </div>
                <div>
                    <LinkButtonSecondary href={""}>
                        Méssage
                    </LinkButtonSecondary>
                </div>
            </div>
            <div>
                <span>Á PROPOS</span>
                <p className="text-sm text-gray-500">
                    {selectedMentor.description}
                </p>
                <button className="text-xmentor">Voir plus </button>
            </div>
            <div className="mt-5">
                <span>EXPERTISE</span>
                <div>
                    {selectedMentor.expertise.map((expertise, index) => (
                        <div key={index}>
                            <div className="text-md font-medium">{expertise.technology}</div>
                            <div className="text-sm flex gap-2 text-gray-500">
                                <span>{expertise.experienceYears} ans d'expérience</span> |
                                <span>{expertise.sessionNumbers} sessions</span>
                            </div>
                        </div>
                    ))}

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
