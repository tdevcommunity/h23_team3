
export const filterByLanguage = (mentors, language) =>{
    return mentors.filter(mentor => mentor.languages.includes(language))
}

export const filterBySessionsRange = (mentors, minSessions,  maxSessions) =>{
        return mentors.filter(mentor => mentor.sessions >= minSessions && mentor.sessions <= maxSessions)
}

export const  filterBySessions =(mentors, sessionsThreshold, isLessThan)=> {
    if (isLessThan) {
        return mentors.filter(mentor => mentor.sessions < sessionsThreshold);
    } else {
        return mentors.filter(mentor => mentor.sessions > sessionsThreshold);
    }
}

export const filterBySessionsHourRange = (mentors, minSessionsHour,  maxSessionsHour) =>{
    return mentors.filter(mentor => mentor.sessionHour >= minSessionsHour && mentor.sessionHour <= maxSessionsHour)
}

export const  filterBySessionsHour =(mentors, sessionsThreshold, isLessThan)=> {
    if (isLessThan) {
        return mentors.filter(mentor => mentor.sessionHour < sessionsThreshold);
    } else {
        return mentors.filter(mentor => mentor.sessionHour > sessionsThreshold);
    }
}