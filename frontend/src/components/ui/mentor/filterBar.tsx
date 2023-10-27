"use client"
import MentorSearchCard from './mentorSearchCard'
import mentorsData from '@/data/mentors.json';
import Image from 'next/image';

import { filterByLanguage, filterBySessionsRange, filterBySessions, filterBySessionsHour, filterBySessionsHourRange } from './functions/filterMentors'
import { Input } from '../input';

import { useState } from 'react';
import StarRating from '../starRating';
import LanguageIcon from '../languageIcon';
import { SearchIcon } from '@/components/icon/icons';

const FilterBar = () => {
    const [mentors, setMentors] = useState(mentorsData)
    return (
        <>
            <div className=' '>
                <div className='w-full h-40 bg-xmentor/10 flex-col  justify-center  flex items-center '>
                    <h1 className='mx-auto text-3xl font-semibold '> Rechercher le mentor qui vous convient</h1>
                    <div className='text-sm flex gap-5 mt-5 items-center '>
                        suggestion:
                        <div className='flex gap-2'>
                            <span className='px-2 text-sm rounded  py-1 bg-xmentor text-white '>HTML</span>
                            <span className='px-2 text-sm  rounded py-1 bg-xmentor text-white '>Javascript </span>
                        </div>
                    </div>
                </div>
                <div>
                    <div className='w-2/6 mx-auto flex -mt-5  mb-10 px-3 shadow-lg shadow-gray-500/10  rounded-md items-center bg-white '>
                        <SearchIcon />
                        <input className='h-14 px-5 border-0 group focus:outline-none focus:ring-0 ' type='text' placeholder="Rechercher" />
                    </div>
                </div>
                <div className=" w-8/12  mx-auto grid grid-cols-4   gap-6" >
                    <div className="w-full flex flex-col bg-white border p-8 rounded-md h-fit sticky">
                        <h1 className=" font-medium">Filtre</h1>
                        <div className="mt-8 mb-4">
                            <h2 className="text-lg">Session (par semaine)</h2>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='sessions' value='2' className="mr-2" onChange={() => {
                                        const tempMentors = filterBySessionsHour(mentorsData, 2, true)
                                        setMentors(tempMentors)
                                    }} />
                                    &lt; 2 heures
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='sessions' value='4' className="mr-2" onChange={() => {
                                        const tempMentors = filterBySessionsHourRange(mentorsData, 2, 6)
                                        setMentors(tempMentors)
                                    }} />
                                    2 - 6  heures
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='sessions' value='6' className="mr-2" onChange={() => {
                                        const tempMentors = filterBySessions(mentorsData, 6, false)
                                        setMentors(tempMentors)
                                    }} />
                                    &gt; 6 heures
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='sessions' value='0' className="mr-2" />
                                    Free
                                </label>
                            </div>
                        </div>
                        <div className="mt-8 mb-4">
                            <h2 className="text-lg">Nombre de sessions</h2>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='nombre' value='20' className="mr-2" onChange={() => {
                                        const tempMentors = filterBySessions(mentorsData, 20, true)
                                        setMentors(tempMentors)
                                    }} />
                                    &lt; 20
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='nombre' value='50' className="mr-2" onChange={() => {
                                        const tempMentors = filterBySessionsRange(mentorsData, 20, 50)
                                        setMentors(tempMentors)
                                    }} />
                                    20 - 50
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='nombre' value='150' className="mr-2" onChange={() => {
                                        const tempMentors = filterBySessionsRange(mentorsData, 50, 150)
                                        setMentors(tempMentors)
                                    }} />
                                    50 - 150
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='nombre' value='151' className="mr-2" onChange={() => {
                                        const tempMentors = filterBySessions(mentorsData, 150, false)
                                        setMentors(tempMentors)
                                    }} />
                                    &gt; 150
                                </label>
                            </div>
                        </div>
                        <div className="mt-8 mb-4">
                            <h2 className="text-lg">Langue</h2>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='langue' value='Francais' className="mr-2" onChange={() => {
                                        const tempMentors = filterByLanguage(mentorsData, 'Francais')
                                        setMentors(tempMentors)
                                    }} />
                                    Francais
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='langue' value='Anglais' className="mr-2" onChange={() => {
                                        const tempMentor = filterByLanguage(mentorsData, 'Anglais')
                                        setMentors(tempMentor)
                                    }} />
                                    Anglais
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='langue' value='Ewe' className="mr-2" onChange={() => {
                                        const tempMentor = filterByLanguage(mentorsData, 'Ewe')
                                        setMentors(tempMentor)
                                    }} />
                                    Ewe
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='langue' value='Kotokoli' className="mr-2" onChange={() => {
                                        const tempMentor = filterByLanguage(mentorsData, 'Kotokoli')
                                        setMentors(tempMentor)
                                    }} />
                                    Kotokoli
                                </label>
                            </div>
                        </div>
                    </div>
                    <div className='w-full col-span-3'>
                        {
                            mentors?.length === 0 ? (
                                <div>
                                    <h1 className="text-center mt-10  ">Aucun mentor à afficher</h1>
                                </div>
                            ) : (
                                <div>
                                    {mentors?.map((mentor, index) => (
                                        <div key={index} className='flex group bg-white hover:bg-blue-50 rounded-md duration-300 hover:cursor-pointer hover:border-xmentor hover:hover-2  border mb-6 px-5  py-6  '>
                                            <div className='w-5/6 '>
                                                <div className='flex gap-4   items-end pb-5  '>
                                                    <span className='text-2xl font-semibold group-hover:underline duraiton-300 group-hover:text-xmentor'> {mentor.name} </span>
                                                    <span className='flex '>
                                                        <StarRating rating={mentor.stars} /> {mentor.stars}
                                                    </span>
                                                    <span className='py-1 px-4 rounded-full  bg-xmentor text-sm text-white'>1000 reviews </span>
                                                </div>
                                                <div className=' text-xl font-medium'>
                                                    {mentor.profession}
                                                </div>
                                                <div className='flex gap-5 py-2 text-sm '>
                                                    <span className='flex gap-1 p-3'>   <LanguageIcon />
                                                        {
                                                            mentor?.languages?.map((language, index) => (
                                                                <p key={index} style={{
                                                                    padding: '5px',
                                                                    color: 'black',
                                                                    fontSize: '12px'
                                                                }} >{language}</p>
                                                            ))
                                                        }</span>
                                                    <span>Sessions</span>
                                                </div>
                                                <p className='text-sm '>
                                                    {mentor.description}
                                                </p>
                                                <div className="flex flex-wrap">

                                                    {
                                                        mentor?.stack?.map((skill, index) => (
                                                            <p key={index} style={{
                                                                padding: '5px',
                                                                color: 'black',
                                                                fontSize: '12px',
                                                                border: 'solid 1px purple',
                                                                marginLeft: '3px',
                                                                borderRadius: '2px'
                                                            }} >{skill}</p>
                                                        ))
                                                    }

                                                </div>
                                            </div>
                                            <div className='w-1/6 flex  justify-center items-center gap-5 flex-col'>
                                                <Image className='w-24 object-cover rounded-full h-24  ' width={100} height={100} alt="" src={mentor.image} />
                                                <div>
                                                    <span className={`py-1 px-4 rounded-full text-sm inline-flex items-center gap-2 ${mentor.isBusy ? 'bg-red-100' : 'bg-green-100'}`}>
                                                        <span className={`h-2 w-2 inline-block rounded-full ${mentor.isBusy ? 'bg-red-700' : 'bg-green-700'}`}></span>
                                                        <span>
                                                            {mentor.isBusy ? (
                                                                <p>Indisponible</p>
                                                            ) : (
                                                                <p>Disponible</p>
                                                            )}
                                                        </span>
                                                    </span>

                                                </div>
                                            </div>

                                        </div>
                                    ))}
                                </div>
                            )
                        }
                    </div>

                </div>
            </div >
        </>
    )
}

export default FilterBar