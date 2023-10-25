"use client"
import MentorSearchCard from './mentorSearchCard'
import mentorsData from '@/data/mentors.json';

import { filterByLanguage, filterBySessionsRange, filterBySessions } from './functions/filterMentors'
import { Input } from '../input';

import { useState } from 'react';

const FilterBar = () => {
    let [mentors, setMentors] = useState(mentorsData)
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
                                    <input type='checkbox' name='sessions' value='2' className="mr-2" />
                                    &lt; 2 heures
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='checkbox' name='sessions' value='4' className="mr-2" />
                                    4 heures
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='checkbox' name='sessions' value='6' className="mr-2" />
                                    &gt; 6 heures
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='checkbox' name='sessions' value='0' className="mr-2" />
                                    Free
                                </label>
                            </div>
                        </div>
                        <div className="mt-8 mb-4">
                            <h2 className="text-lg">Nombre de sessions</h2>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='nombre' value='20' className="mr-2" />
                                    &lt; 20
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='nombre' value='50' className="mr-2" />
                                    20 - 50
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='nombre' value='150' className="mr-2" />
                                    50 - 150
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='nombre' value='151' className="mr-2" />
                                    &gt; 150
                                </label>
                            </div>
                        </div>
                        <div className="mt-8 mb-4">
                            <h2 className="text-lg">Langue</h2>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='langue' value='Francais' className="mr-2" />
                                    Francais
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='langue' value='Anglais' className="mr-2" />
                                    Anglais
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='langue' value='Ewe' className="mr-2" />
                                    Ewe
                                </label>
                            </div>
                            <div>
                                <label className="flex items-center">
                                    <input type='radio' name='langue' value='Kotokoli' className="mr-2" />
                                    Kotokoli
                                </label>
                            </div>
                        </div>
                    </div>


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

                        {
                            mentors?.map((mentor) => (
                                <MentorSearchCard mentor={mentor} key={mentor.id} />
                            ))
                        }

                    </div>
                </div>
            </div>
        </>
    )
}

export default FilterBar