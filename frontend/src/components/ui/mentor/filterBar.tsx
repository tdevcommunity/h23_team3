"use client"
import MentorSearchCard from './mentorSearchCard'
import mentorsData from '@/data/mentors.json';

import { filterByLanguage, filterBySessionsRange, filterBySessions, filterBySessionsHour, filterBySessionsHourRange } from './functions/filterMentors'
import { Input } from '../input';

import { useState } from 'react';

const FilterBar = () => {
    const [mentors, setMentors] = useState(mentorsData)
    return (
        <>
            <div style={{
                width: '100vw',
                height: '70vh',
                paddingLeft: '30px',
                paddingRight: '30px',
                flexDirection: 'column',
                marginTop: '36px',
                display: 'flex'
            }}>

                <div className="flex  gap-6" style={{
                    width: '95%',
                    height: '70%',
                    display: 'flex',
                    flexDirection: 'row',
                    justifyContent: "space-between",
                    overflow: 'hidden',
                    position: 'fixed',
                }} >
                    <div className="w-1/4 flex flex-col shadow-md p-8 rounded-md fixed">
                        <h1 className="text-xl font-bold">Filtre</h1>
                        <div className="mt-8 mb-4">
                            <h2 className="text-lg">Session (par semaine)</h2>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='sessions' value='2' className="mr-2"  onChange={() => {
                                        const tempMentors = filterBySessionsHour(mentorsData, 2, true)
                                        setMentors(tempMentors)
                                    }} />
                                    &lt; 2 heures
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='sessions' value='4' className="mr-2"  onChange={() => {
                                        const tempMentors = filterBySessionsHourRange(mentorsData, 2, 6)
                                        setMentors(tempMentors)
                                    }}  />
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
                    {
                        mentors?.length === 0 ? (
                            <div
                                style={{
                                    width: '65%',
                                    height: '100%',
                                    marginLeft: '32%',
                                    paddingTop: '30px',
                                    display: 'flex',
                                    flexDirection: 'column',
                                    position: 'absolute',
                                    overflow: 'auto',
                                    alignItems:'center',
                                    justifyContent:'center'
                                }}
                            >
                                <h1 className="text-center text-4xl">Aucun mentor a afficher</h1>
                            </div>
                        ) : (
                            <div
                                style={{
                                    width: '65%',
                                    height: '100%',
                                    marginLeft: '32%',
                                    paddingTop: '30px',
                                    display: 'flex',
                                    flexDirection: 'column',
                                    position: 'absolute',
                                    overflow: 'auto',
                                }}
                            >
                                {mentors?.map((mentor) => (
                                    <MentorSearchCard mentor={mentor} key={mentor.id} />
                                ))}
                            </div>
                        )
                    }
            </div>
        </div >
        </>
    )
}

export default FilterBar